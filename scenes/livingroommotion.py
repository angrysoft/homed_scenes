from homedaemon.scenes import BaseAutomation
from homedaemon.scenes import TimeRange
from pyiot.software import Time

class Scene(BaseAutomation):
    def __init__(self,sid:str):
        super().__init__(sid)
        self.name = 'Livingroom motion'
        self.add_trigger('report.0x00158d0002ec2fa6.occupancy.True', self.on_motion)
        self.add_trigger('report.0x0000000007e7bae0.power.on', self.on_power_on)
        self.add_trigger('report.0x00158d0002ec2fa6.no_occupancy_since.240', self.power_off)
        self.place = 'Living room'
    
    def on_motion(self):
        lamp = self.get_device('0x0000000007e7bae0')
        light = self.get_device('0x04cf8cdf3c8a0236')
        if int(light.status.illuminance) < 9500:
            lamp.on()
        else:
            lamp.off()
    
    def power_off(self):
        lamp = self.get_device('0x0000000007e7bae0')
        lamp.off()
    
    def on_power_on(self):
        lamp = self.get_device('0x0000000007e7bae0')
        clock = self.get_device('clock')
        _range = TimeRange(Time(23), clock.status.sunrise)
        _now = Time()
        _now.set_now()
        if _now in _range:
            lamp.set_bright(1)
            lamp.set_ct_pc(0)
        else:
            lamp.set_bright(30)
            lamp.set_ct_pc(50)
            
