from homedaemon.scenes import BaseAutomation
from datetime import datetime

class Scene(BaseAutomation):
    def __init__(self,sid, daemon):
        super().__init__(sid, daemon)
        self.name = 'Lamp color temp'
        self.add_trigger('report.clock.time.sunset', self.on_time)
        self.place = 'Living room'
        self.lamp = self.get_device('0x0000000007e7bae0')
    
    def calc_ct(self, ct, delta, ts):
        if delta <= 0:
            return 0
        return int(ct / (delta / ts))
    
    def on_time(self):
        _ts = 600
        _sunset = datetime.now()
        _target_time = datetime(_sunset.year, _sunset.month, _sunset.day, 23, 0, 0)
        _delta = _target_time - _sunset
        _delta = _delta.seconds
        _ct = 50
        
        while _delta >= 1:
            _delta -= _ts
            _ct -= self.calc_ct(_ct, _delta, _ts)
            if _ct < 0:
                break
            self.lamp.ct_pc(_ct)
            self.sleep(_ts)
        self.lamp.ct_pc(0)
        
            