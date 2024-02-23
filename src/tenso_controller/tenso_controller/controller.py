from simba_interfaces.msg import SensorState
from simba_interfaces.msg import HeartBeat
from simba_interfaces.srv import SetState

import rclpy
from rclpy.node import Node

import board
from cedargrove_nau7802 import NAU7802


class TensoService(Node):

    def __init__(self):
        super().__init__('tenso_service')
        self.service_id=100

        self.hb_pub=self.create_publisher(HeartBeat,"/Engine/HB",10)
        self.hb_timer=self.create_timer(1,self.hb_callback)
        self.hb_count=0

        self.tenso_pub=self.create_publisher(SensorState,"/Engine/Tenso",9)
        self.tenso_timer=self.create_timer(0.1,self.tenso_callback)
        self.nau7802=NAU7802(board.I2C(),address=0x2A,active_channels=8)
        self.nau7802.calibrate("INTERNAL")  
        self.tenso_srv=self.create_service(SetState,"/Engine/Tenso/Cal",self.cal_callback)

    def cal_callback(self,request,response):
        response.ok=self.nau7802.calibrate("OFFSET")
        return response

    def tenso_callback(self):
        msg=SensorState()
        msg.sensor_id=1
        msg.sensor_value=self.nau7802.read()
        self.tenso_pub.publish(msg)


    def hb_callback(self):
        msg=HeartBeat()
        msg.service_id=self.service_id
        msg.timestamp=self.hb_count
        self.hb_count+=1
        self.hb_pub.publish(msg)



def main():
    rclpy.init()
    tenso_service = TensoService()

    rclpy.spin(tenso_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()