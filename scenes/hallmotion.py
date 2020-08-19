from homedaemon.scenes import BaseAutomation
from homedaemon.scenes import Time, TimeRange


class Scene(BaseAutomation):
    def __init__(self, sid:str):
        super().__init__(sid)
        self.name = 'hall motion'
        self.add_trigger('report.158d00029a49ba.status.motion', self.on_motion)
        self.add_trigger('report.158d00029a49ba.no_motion.120', self.on_no_motion)
    
    def on_motion(self):
        clock = self.get_device('clock')
        sunrise = Time(time_str=clock.sunrise)
        sunset = Time(time_str=clock.sunset)
        _range = TimeRange(sunset, sunrise)
        _now = self.now()
        if _now in _range:
            entrance = self.get_device('158d0002b74c28')
            wallsw = self.get_device('158d0002a18c2b')
            lamp = self.get_device('0x0000000007e7bae0')
            if entrance.status == 'open':
                wallsw.on()
                lamp.on()
                self.sleep(25)
                wallsw.channel_0.off()
                self.sleep(10)
                wallsw.channel_1.off()
            elif _now in TimeRange(Time(23), sunrise) and lamp.is_on:
                return
            else:
                wallsw.channel_1.on()
                self.sleep(25)
                wallsw.channel_1.off()
                
    def on_no_motion(self):
        wallsw = self.get_device('158d0002a18c2b')
        wallsw.channel_0.off()
        wallsw.channel_1.off()
