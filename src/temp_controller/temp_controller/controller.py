from w1thermsensor import W1ThermSensor

from simba_interfaces.msg import SensorState
from simba_interfaces.msg import HeartBeat

import rclpy
from rclpy.node import Node

class TempService(Node):

    def __init__(self):
        super().__init__('temp_service')
        self.service_id=101
        self.tempMap={}
        self.hb_pub=self.create_publisher(HeartBeat,"/Engine/HB",10)
        self.hb_timer=self.create_timer(1,self.hb_callback)
        self.hb_count=0      

        self.temp_timer=self.create_timer(0.1,self.temp_callback)
        self.temp_pub=self.create_publisher(SensorState,"/Engine/Temp",6)
        self.sensors = W1ThermSensor.get_available_sensors()
        for sensor in self.sensors:
            sensor.set_resolution(9)

    def hb_callback(self):
        msg=HeartBeat()
        msg.service_id=self.service_id
        msg.timestamp=self.hb_count
        self.hb_count+=1
        self.hb_pub.publish(msg)

    def temp_callback(self):
        for sensor in self.sensors:
            msg=SensorState()
            msg.sensor_id=self.tempMap.get(sensor.id,0)
            msg.sensor_value=sensor.get_temperature()
            self.temp_pub.publish(msg)


def main():
    rclpy.init()
    temp_service = TempService()

    rclpy.spin(temp_service)

    rclpy.shutdown()


if __name__ == '__main__':
    main()

