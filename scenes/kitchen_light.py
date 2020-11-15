from homedaemon.scenes import BaseAutomation

class Scene(BaseAutomation):
    def __init__(self,sid:str):
        super().__init__(sid)
        self.name = 'Kitchen Strip'
        self.add_trigger('report.158d000200a020.status.click', self.toggle_strip)
        self.add_trigger('report.158d000200a020.status.double_click', self.toggle_light)
    
    def toggle_light(self):
        self.kitchen_lamp = self.get_device('158d0002bffe5a')
        if self.kitchen_lamp:
            self.kitchen_lamp.on('left')
            self.kitchen_lamp.off('right')
        
    def toggle_strip(self):
        self.strip_switch = self.get_device('158d00027d0065')
        if self.strip_switch:
            self.strip_switch.toggle()