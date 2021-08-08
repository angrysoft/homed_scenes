from homedaemon.scenes import BaseAutomation, RunAfter

class Scene(BaseAutomation):
    def __init__(self,sid:str):
        super().__init__(sid)
        self.name = 'Bathroom fan'
        # event loop death
        self.add_trigger('report.0x00158d0002abac97.right.ON', self.on_on)
        self.add_trigger('report.0x00158d0002abac97.right.OFF', self.on_off)
        # self._timer_on = RunAfter(240, self.fun_on)
        self._timer_on = RunAfter(5, self.fun_on)
        self._timer_off = RunAfter(5, self.fun_off)

    def on_on(self):
        self._timer_off.cancel()
        self._timer_on.wait()
        
    def on_off(self):
        self._timer_on.cancel()
        self._timer_off.wait()
    
    def fun_on(self):
        self.wallsw = self.get_device('0x00158d0002abac97')
        if self.wallsw.is_on('right'):
            self.wallsw.on('left')
    
    def fun_off(self):
        self.wallsw = self.get_device('0x00158d0002abac97')
        if self.wallsw.is_off('right'):
            if self.wallsw.is_on('left'):
                self.wallsw.off('left')
            self.switch = self.get_device('1000b6063e')
            if self.switch.is_on():
                self.switch.off()
    
        