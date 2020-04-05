from homedaemon.scenes import BaseScene

class Scene(BaseScene):
    def __init__(self,sid, daemon):
        super().__init__(sid, daemon)
        self.name = 'goodbye'
        self.place = 'All'
    
    def on(self):
        dev_to_off = ['158d00024e2e5b', '158d00027d0065', '158d000283b219',
                      '158d00029b1929', '158d0002a16338', '158d0002a18c2b', '158d0002abac97',
                      '158d0002bffe5a', 'rgb01', 'tv01', '0x000000000545b741', '0x0000000007e7bae0']
        for _sid in dev_to_off:
            dev = self.get_device(_sid)
            if dev.model == 'plug':
                dev.power.off()
            elif dev.model == 'ctrl_neutral2':
                dev.channel_0.off()
                dev.channel_1.off()
            elif dev.model == 'ctrl_neutral1':
                dev.channel_0.off()
            elif dev.model in ('bslamp1', 'color', 'rgbstrip', 'bravia'):
                dev.off()
                
        
        