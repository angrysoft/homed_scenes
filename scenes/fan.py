from homedaemon.scenes import BaseAutomation, RunAfter

class Scene(BaseAutomation):
    def __init__(self,sid:str):
        super().__init__(sid)
        self.name = 'Bathroom fan'
        self.add_trigger('report.158d0002abac97.channel_1.on', self.on_on)
        self.add_trigger('report.158d0002abac97.channel_1.off', self.on_off)
        self._timer_on = RunAfter(240, self.fun_on)
        self._timer_off = RunAfter(5, self.fun_off)

    def on_on(self):
        self._timer_off.cancel()
        self._timer_on.wait()
        
    def on_off(self):
        self._timer_on.cancel()
        self._timer_off.wait()
    
    def fun_on(self):
        self.wallsw = self.get_device('158d0002abac97')
        if self.wallsw.channel_1.is_on():
            self.wallsw.channel_0.on()
    
    def fun_off(self):
        self.wallsw = self.get_device('158d0002abac97')
        if self.wallsw.channel_1.is_off():
            self.wallsw.channel_0.off()
            self.switch = self.get_device('1000b6063e')
            self.switch.off()
    
        