from simba_interfaces.srv import SetState
from simba_interfaces.msg import HeartBeat
import RPi.GPIO as GPIO


import rclpy
from rclpy.node import Node

class GpioConfig:
    def __init__(self,actuator_id,actuator_pin) -> None:
        self.actuator_id=actuator_id
        self.actuator_pin=actuator_pin

class GpioService(Node):

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        super().__init__('gpio_service')
        self.service_id=104

        self.hb_pub=self.create_publisher(HeartBeat,"/Engine/HB",10)
        self.hb_timer=self.create_timer(1,self.hb_callback)
        self.hb_count=0

        self.gpio_srv = self.create_service(SetState, '/Engine/GPIO/Set', self.gpio_callback)
        self.gpioConfigs=[GpioConfig(112,17)]
        for config in self.gpioConfigs:
            GPIO.setup(config.actuator_pin,GPIO.OUT)
            

    def hb_callback(self):
        msg=HeartBeat()
        msg.service_id=self.service_id
        msg.timestamp=self.hb_count
        self.hb_count+=1
        self.hb_pub.publish(msg)

    def gpio_callback(self, request, response):
        self.get_logger().info(str(request.actuator_id))
        self.get_logger().info(str(request.position))
        for config in self.gpioConfigs:
            if config.actuator_id==request.actuator_id:
                response.ok=True
                GPIO.output(config.actuator_pin,GPIO.HIGH if request.position==1 else GPIO.LOW)
        return response


def main():
    rclpy.init()
    gpio_service = GpioService()

    rclpy.spin(gpio_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()