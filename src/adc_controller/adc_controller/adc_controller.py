from simba_interfaces.msg import SensorState
from simba_interfaces.msg import HeartBeat

import rclpy
from rclpy.node import Node


class ADCService(Node):

    def __init__(self):
        super().__init__('adc_service')
        self.service_id=105
        self.hb_pub=self.create_publisher(HeartBeat,"/Engine/HB",10)
        self.hb_timer=self.create_timer(1,self.hb_callback)
        self.hb_count=0
        self.adc_pub=self.create_publisher(SensorState,'/Engine/ADC',7)
        self.adc_timer=self.create_timer(0.1,self.adc_callback)

            

    def hb_callback(self):
        msg=HeartBeat()
        msg.service_id=self.service_id
        msg.timestamp=self.hb_count
        self.hb_count+=1
        self.hb_pub.publish(msg)

    def adc_callback(self):
        pass


def main():
    rclpy.init()
    adc_service = ADCService()

    rclpy.spin(adc_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()