from homedaemon.scenes import BaseAutomation, Time

class Scene(BaseAutomation):
    def __init__(self,sid, daemon):
        super().__init__(sid, daemon)
        self.name = 'Lamp color temp'
        self.add_trigger('report.0x0000000007e7bae0.power.on', self.set_ct)
        self.place = 'Living room'
        self.lamp = self.get_device('0x0000000007e7bae0')
        self.clock = self.get_device('clock')
    
    def calc_ct(self, ct, delta, ts):
        if delta <= 0:
            return 0
        return int(ct / (delta / ts))
        
    def set_ct(self):
        _sunset  = Time(*[int(i) for i in self.daemon.config['datetime']['sunset'].split(':')])
        _now = Time(self.clock.hour, self.clock.minute)
        _end_time = Time(23)
        
        try:
            _end_time - _sunset
        except ValueError:
            pass
                        