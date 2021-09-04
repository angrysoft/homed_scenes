from homedaemon.scenes import BaseAutomation

class Scene(BaseAutomation):
    def __init__(self,sid:str):
        super().__init__(sid)
        self.name = 'Light Switch'
        self.add_trigger('report.0x00158d00033ef2d8.click.long', self.off_others)
        self.add_trigger('report.0x00158d00033ef2d8.click.single', self.lamp_toggle)
        self.add_trigger('report.0x00158d00033ef2d8.click.double', self.toggle_bright)
        self.place = 'Bedroom'
    
    def off_others(self):
        dev_to_off = ['0x00158d00024e2e5b',
                      '0x00158d00027d0065', 
                    #   '158d000283b219',
                      '0x00158d00029b1929',
                      '0x00158d0002a16338',
                      '0x00158d0002a18c2b',
                      '0x00158d0002abac97',
                      '0x00158d0002bffe5a',
                      '0x0000000007e7bae0']
        
        for _sid in dev_to_off:
            dev = self.get_device(_sid)
            if _sid == '0x00158d0002a18c2b':
                dev.off('left')
            elif dev.status.model == 'ctrl_neutral2':
                dev.off('left')
                dev.off('right')
            else:
                dev.off()
       
    def lamp_toggle(self):
        self.lamp = self.get_device('235444403')
        # self.lamp = self.get_device('0x0000000007e7bae0')
        if self.lamp:
            self.lamp.toggle()
            if self.lamp.is_on:
                self.lamp.set_bricct(1,1)
    
    def toggle_bright(self):
        self.lamp = self.get_device('235444403') 
        if self.lamp:
            if self.lamp.bright < 100:
                self.lamp.set_bricct(100,100)
            elif self.lamp.bright > 1:
                self.lamp.set_bricct(1,1)