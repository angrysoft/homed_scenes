from homedaemon.scenes import BaseAutomation

class Scene(BaseAutomation):
    def __init__(self,sid, daemon):
        super().__init__(sid, daemon)
        self.name = 'Bathroom fan'
        self.add_trigger('report.158d0002abac97.channel_1.on', self.on_on)
        self.add_trigger('report.158d0002abac97.channel_1.off', self.on_off)
        self.wallsw = self.get_device('158d0002abac97')
        
    def on_on(self):
        self.sleep(240)
        if self.wallsw.channel_1.is_on():
            self.wallsw.channel_0.on()
    
    def on_off(self):   
        self.sleep(5)
        if self.wallsw.channel_1.is_off():
            self.wallsw.channel_0.off()
                