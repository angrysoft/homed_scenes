from homedaemon.scenes import BaseAutomation

class Scene(BaseAutomation):
    def __init__(self,sid, daemon):
        super().__init__(sid, daemon)
        self.name = 'Light Switch'
        self.add_trigger('report.158d00033ef2d8.status.long_click_press', self.off_others)
        self.add_trigger('report.158d00033ef2d8.status.click', self.lamp_toggle)
        self.add_trigger('report.158d00033ef2d8.status.double_click', self.toggle_bright)
        self.place = 'Bedroom'
        self.lamp = self.get_device('235444403') 
    
    def off_others(self):
        dev_to_off = ['158d00024e2e5b',
                      '158d00027d0065', 
                    #   '158d000283b219',
                      '158d00029b1929',
                      '158d0002a16338',
                      '158d0002a18c2b',
                      '158d0002abac97',
                      '158d0002bffe5a',
                    #   'rgb01',
                      '0x0000000007e7bae0']
        # self.lamp.on()
        # self.lamp.set_bricct(100,1)
        for _sid in dev_to_off:
            dev = self.get_device(_sid)
            print(dev.model)
            if dev.model == 'plug':
                dev.power.off()
            elif dev.model == 'ctrl_neutral2':
                dev.channel_0.off()
                dev.channel_1.off()
            elif dev.model == 'ctrl_neutral1':
                dev.channel_0.off()
            elif dev.model in ('bslamp1', 'color', 'rgbstrip', 'bravia'):
                dev.off()
        # self.sleep(10)
        # self.lamp.set_bricct(1,1)
    
    def lamp_toggle(self):
        if self.lamp:
            self.lamp.toggle()
            if self.lamp.is_on:
                self.lamp.set_bricct(1,1)
    
    def toggle_bright(self):
        if self.lamp:
            if self.lamp.bright < 100:
                self.lamp.set_bricct(100,100)
            elif self.lamp.bright > 1:
                self.lamp.set_bricct(1,1)