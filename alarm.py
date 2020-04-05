from homedaemon.scenes import BaseAutomation

class Scene(BaseAutomation):
    def __init__(self,sid, daemon):
        super().__init__(sid, daemon)
        self.name = 'alarm'
        self.add_trigger('report.158d00029a49ba.status.motion', self.log)
        self.add_trigger('report.158d0002ec03fe.status.motion', self.log)
    
    def log(self):
        self.daemon.logger.debug('Alarm triggerd')