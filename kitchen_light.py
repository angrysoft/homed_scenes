from homedaemon.scenes import BaseAutomation

class Scene(BaseAutomation):
    def __init__(self,sid, daemon):
        super().__init__(sid, daemon)
        self.name = 'Kitchen Strip'
        self.add_trigger('report.158d000200a020.status.click', self.toggle_strip)
        self.add_trigger('report.158d000200a020.status.double_click', self.toggle_light)
        self.kitchen_lamp = self.get_device('158d0002bffe5a')
        self.strip_switch = self.get_device('158d00027d0065')
    
    def toggle_light(self):
        if self.kitchen_lamp:
            self.kitchen_lamp.channel_0.toggle()
        
    def toggle_strip(self):
        if self.strip_switch:
            self.strip_switch.power.toggle()