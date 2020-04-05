from homedaemon.scenes import BaseScene

class Scene(BaseScene):
    def __init__(self, sid, daemon):
        super().__init__(sid, daemon)
        self.name = 'Movie'
        self.reversible = True
        self.place = 'Living room'
    
    def on(self):
        dev_to_off = ['158d00027d0065', '158d00029b1929', '158d0002bffe5a']
        self.store_device_state('158d00027d0065', '158d00029b1929', '158d0002bffe5a', 'rgb01', '0x0000000007e7bae0')
        tvrgb = self.get_device('rgb01')
        color = self.get_device('0x0000000007e7bae0')
        tvrgb.set_rgb({'red':255 ,'green':38, 'blue': 0})
        tvrgb.set_bright(100)
        color.on()
        color.bright(1)
        # color.set_rgb({'red':0 ,'green':0, 'blue': 255})
        color.set_ct_abx(1700)
        self.sleep(1)
        for _sid in dev_to_off:
            dev = self.get_device(_sid)
            if dev.model == 'plug':
                dev.power.off()
            elif dev.model == 'ctrl_neutral1':
                dev.channel_0.off()
            elif dev.model in ('bslamp1', 'color', 'rgbstrip', 'bravia', 'ctrl_neutral2'):
                dev.off()
    
    def off(self):
        tvrgb = self.get_device('rgb01')
        color = self.get_device('0x0000000007e7bae0')
        tvrgb.off()
        color.bright(70)
        color.set_ct_abx(3100)
    
    
    # TODO : zapisać stan lamp i innych urządzeń a przy off wczytać