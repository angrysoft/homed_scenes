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
    
    def on_motion(self):
        clock = self.get_device('clock')
        sunrise = Time(time_str=clock.sunrise)
        sunset = Time(time_str=clock.sunset)
        _range = TimeRange(sunset, sunrise)
        _now = self.now()
        if _now in _range:
            self.lamp.on()
        else:
            self.lamp.off()
    
    def on_power_on(self):
        sunrise = self.daemon.config['datetime']['sunrise']
        if TimeCheck('<>', '23:00', sunrise).status:
            self.lamp.set_bright(1)
            self.lamp.set_ct_pc(0)
        else:
            self.lamp.set_bright(30)
            self.lamp.set_ct_pc(50)
            
