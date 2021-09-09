from homedaemon.scenes import BaseAutomation, RunAfter

class Scene(BaseAutomation):
    def __init__(self,sid:str):
        super().__init__(sid)
        self.name = 'Bathroom events'
        # event loop death
        self.add_trigger('report.0x00158d0002abac97.right.ON', self.on_on)
        self.add_trigger('report.0x00158d0002abac97.right.OFF', self.on_off)
        self.add_trigger('report.0x00124b0022ec93cf.occupancy.True', self.on_movement)
        self.add_trigger('report.0x00124b0022ec93cf.occupancy.False', self.on_no_movement)
        self._timer_on = RunAfter(240, self.fun_on)
        self._timer_off = RunAfter(5, self.fun_off)
    
    def on_movement(self):
        wallsw = self.get_device('0x00158d0002abac97')
        if wallsw.is_on('right'):
            return
    
    def on_no_movement(self):
        wallsw = self.get_device('0x00158d0002abac97')
        if wallsw.is_on('right'):
            wallsw.off('right')
        

    def on_on(self):
        self._timer_off.cancel()
        self._timer_on.wait()
        
    def on_off(self):
        self._timer_on.cancel()
        self._timer_off.wait()
    
    def fun_on(self):
        wallsw = self.get_device('0x00158d0002abac97')
        if wallsw.is_on('right'):
            wallsw.on('left')
    
    def fun_off(self):
        wallsw = self.get_device('0x00158d0002abac97')
        if wallsw.is_off('right') and wallsw.is_on('left'):
            wallsw.off('left')
        
        light_switch = self.get_device('1000b6063e')
        if light_switch.is_on():
            light_switch.off()

            
    
        