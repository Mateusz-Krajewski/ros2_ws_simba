import rclpy
from rclpy.node import Node
from adafruit_servokit import ServoKit

from simba_interfaces.srv import SetState
from simba_interfaces.msg import ActuatorState
from simba_interfaces.msg import HeartBeat

class ServoConfig:
    def __init__(self,actuator_id,servo_channel,openPos,closePos,mosfet_pin) -> None:
        self.actuator_id=actuator_id
        self.servo_channel=servo_channel
        self.openPos=openPos
        self.closePos=closePos
        self.mosfetPin=mosfet_pin
        pass
class ServoHistory:
    def __init__(self,actuator_id,position) -> None:
        self.actuator_id=actuator_id
        self.position=position



class ServoController(Node):
    def __init__(self):
        super().__init__("servo_controller")
        self.pwm_srv=self.create_service(SetState,"/Engine/Servo/Set",self.pwm_callback)
        self.kit=ServoKit(channels=16,address=0x70)
        self.servoConfigs=self.init_configs()
        self.servoHistory=[]
        self.service_id=103
        self.servo_timer=self.create_timer(1,self.servo_actuator_callback)
        self.servo_pub=self.create_publisher(ActuatorState,"/Engine/Servo",10)

        self.hb_pub=self.create_publisher(HeartBeat,"/Engine/HB",10)
        self.hb_timer=self.create_timer(1,self.hb_callback)
        self.hb_count=0


    def hb_callback(self):
        msg=HeartBeat()
        msg.service_id=self.service_id
        msg.timestamp=self.hb_count
        self.hb_count+=1
        self.hb_pub.publish(msg)

    def find_servo_by_id(self,actuator_id):
        for servo in self.servoConfigs:
            if servo.actuator_id==actuator_id:
                return servo
        return None

    def servo_actuator_callback(self):
        for servo in self.servoHistory:
            msg=ActuatorState()
            msg.actuator_id=servo.actuator_id
            msg.position=servo.position
            self.servo_pub.publish(msg)


    def init_configs(self):
        #TODO wczytywanie configow z plikow json
        return [ServoConfig(101,1,28,120,-1)] 
    def init_history(self):
        for servo in self.servoConfigs:
            self.servoHistory.append(ServoHistory(servo.actuator_id,0))

    
    def pwm_callback(self,request,response):
        conf=self.find_servo_by_id(request.actuator_id)
        print(request.actuator_id)
        print(request.position)
        if conf==None:
            response.ok=False
            return response
        self.kit.servo[conf.servo_channel].angle=conf.closePos if request.position==0 else conf.openPos
        response.ok=True
        return response



def main():
    rclpy.init()
    pwmGenerator=ServoController()
    rclpy.spin(pwmGenerator)
    rclpy.shutdown()

if __name__=='__main__':
    main()