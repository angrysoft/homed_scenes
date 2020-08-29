from homedaemon.scenes import BaseAutomation
from homedaemon.scenes import Time, TimeRange

class Scene(BaseAutomation):
    def __init__(self,sid:str):
        super().__init__(sid)
        self.name = 'Livingroom motion'
        self.add_trigger('report.158d0002ec2fa6.status.motion', self.on_motion)
        self.add_trigger('report.0x0000000007e7bae0.power.on', self.on_power_on)
        self.place = 'Living room'
    
    def on_motion(self):
        lamp = self.get_device('0x0000000007e7bae0')
        clock = self.get_device('clock')
        sunrise = Time(time_str=clock.sunrise)
        sunset = Time(time_str=clock.sunset)
        _range = TimeRange(sunset, sunrise)
        _now = self.now()
        if _now in _range:
            lamp.on()
        else:
            lamp.off()
    
    def on_power_on(self):
        lamp = self.get_device('0x0000000007e7bae0')
        clock = self.get_device('clock')
        sunrise = Time(time_str=clock.sunrise)
        _range = TimeRange(Time(23), sunrise)
        if self.now() in _range:
            lamp.set_bright(1)
            lamp.set_ct_pc(0)
        else:
            lamp.set_bright(30)
            lamp.set_ct_pc(50)
            
