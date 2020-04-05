from homedaemon.scenes import BaseAutomation
from homedaemon.scenes import TimeCheck
from datetime import datetime

class Scene(BaseAutomation):
    def __init__(self,sid, daemon):
        super().__init__(sid, daemon)
        self.name = 'Livingroom motion'
        self.add_trigger('report.158d0002ec2fa6.status.motion', self.on_motion)
        self.place = 'Living room'
    
    def on_motion(self):
        sunrise = self.daemon.config['datetime']['sunrise']
        sunset = self.daemon.config['datetime']['sunset']
        if TimeCheck('<>', sunset, sunrise).status:
            lamp = self.get_device('0x0000000007e7bae0')
            lamp.on()
        else:
            lamp = self.get_device('0x0000000007e7bae0')
            lamp.off()
            