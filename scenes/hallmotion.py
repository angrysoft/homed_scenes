from homedaemon.scenes import BaseAutomation
from homedaemon.scenes import TimeCheck


class Scene(BaseAutomation):
    def __init__(self, sid, daemon):
        super().__init__(sid, daemon)
        self.name = 'hall motion'
        self.add_trigger('report.158d00029a49ba.status.motion', self.on_motion)
        self.add_trigger('report.158d00029a49ba.no_motion.120', self.on_no_motion)
    
    def on_motion(self):
        sunrise = self.daemon.config['datetime']['sunrise']
        sunset = self.daemon.config['datetime']['sunset']
        if TimeCheck('<>', sunset, sunrise).status:
            entrance = self.get_device('158d0002b74c28')
            wallsw = self.get_device('158d0002a18c2b')
            if entrance.status == 'open':
                wallsw.on()
                lamp = self.get_device('0x0000000007e7bae0')
                lamp.on()
                self.sleep(25)
                wallsw.channel_0.off()
                self.sleep(10)
                wallsw.channel_1.off()
            else:
                wallsw.channel_1.on()
                self.sleep(25)
                wallsw.channel_1.off()
                
    def on_no_motion(self):
        wallsw = self.get_device('158d0002a18c2b')
        wallsw.channel_0.off()
        wallsw.channel_1.off()
