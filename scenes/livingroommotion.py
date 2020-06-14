from homedaemon.scenes import BaseAutomation
from homedaemon.scenes import Time, TimeRange
from datetime import datetime

class Scene(BaseAutomation):
    def __init__(self,sid, daemon):
        super().__init__(sid, daemon)
        self.name = 'Livingroom motion'
        self.add_trigger('report.158d0002ec2fa6.status.motion', self.on_motion)
        self.add_trigger('report.0x0000000007e7bae0.power.on', self.on_power_on)
        self.place = 'Living room'
        self.lamp = self.get_device('0x0000000007e7bae0')
        self.clock = self.get_device('clock')
    
    def on_motion(self):
        sunrise = Time(time_str=self.clock.sunrise)
        sunset = Time(time_str=self.clock.sunset)
        _range = TimeRange(sunset, sunrise)
        _now = self.now()
        if _now in _range:
            self.lamp.on()
        else:
            self.lamp.off()
    
    def on_power_on(self):
        sunrise = Time(time_str=self.clock.sunrise)
        _range = TimeRange(Time(23), sunrise)
        if self.now() in _range:
            self.lamp.set_bright(1)
            self.lamp.set_ct_pc(0)
        else:
            self.lamp.set_bright(30)
            self.lamp.set_ct_pc(50)
            
