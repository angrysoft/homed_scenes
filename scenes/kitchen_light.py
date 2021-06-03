from homedaemon.scenes import BaseAutomation

class Scene(BaseAutomation):
    def __init__(self,sid:str):
        super().__init__(sid)
        self.name = 'Kitchen Strip'
        self.add_trigger('report.0x00158d000200a020.click.single', self.toggle_strip)
        self.add_trigger('report.0x00158d000200a020.click.double', self.toggle_light)
    
    def toggle_light(self):
        self.kitchen_lamp = self.get_device('0x00158d0002bffe5a')
        if self.kitchen_lamp:
            self.kitchen_lamp.toogle('left')
            self.kitchen_lamp.off('right')
        
    def toggle_strip(self):
        print('exec toogle')
        self.strip_switch = self.get_device('0x00158d00027d0065')
        if self.strip_switch:
            self.strip_switch.toggle()