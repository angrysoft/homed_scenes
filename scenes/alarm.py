from homedaemon.scenes import BaseAutomation
import os

class Scene(BaseAutomation):
    def __init__(self,sid):
        super().__init__(sid)
        self.name = 'alarm'
        self.add_trigger('report.158d00029a49ba.status.motion', self.alarm_fired)
        self.add_trigger('report.158d0002ec03fe.status.motion', self.alarm_fired)
        self.add_trigger('report.158d0002ec2fa6.status.motion', self.alarm_fired)
        self.add_trigger('report.158d0002a67612.status.open', self.alarm_fired)
        self.add_trigger('report.158d0002a13819.status.open', self.alarm_fired)
        self.add_trigger('report.158d0002b74c28.status.open', self.alarm_fired)
        self.add_trigger('report.158d0002ec2fa6.status.open', self.alarm_fired)
    
    def log(self):
        self.logger.debug('Alarm triggerd')
        
    
    
    def alarm_fired(self):
        if not os.path.exists('/etc/angryghome/armed'):
            return
        dev_to_off = ['158d00024e2e5b',
                      '158d00027d0065', 
                      '158d000283b219',
                      '158d00029b1929',
                      '158d0002a16338',
                      '158d0002a18c2b',
                      '158d0002abac97',
                      '158d0002bffe5a',
                      '0x0000000007e7bae0']
        
        for _sid in dev_to_off:
            dev = self.get_device(_sid)
            if dev.model == 'plug':
                dev.power.on()
            elif dev.model == 'ctrl_neutral2':
                dev.channel_0.on()
                dev.channel_1.on()
            elif dev.model == 'ctrl_neutral1':
                dev.channel_0.on()
            elif dev.model in ('bslamp1', 'color', 'rgbstrip', 'bravia'):
                dev.on()
        print('on everything')