from homedaemon.scenes import BaseAutomation, RunAfter

class Scene(BaseAutomation):
    def __init__(self,sid:str):
        super().__init__(sid)
        self.name = 'Bathroom events'
        self.add_trigger('report.0x00158d0002abac97.right.ON', self.on_on)
        self.add_trigger('report.0x00158d0002abac97.right.OFF', self.on_off)
        self.add_trigger('report.0x00124b0022ec93cf.occupancy.True', self.on_movement)
        self.add_trigger('report.0x00124b0022ec93cf.occupancy.False', self.on_no_movement)
        self.add_trigger('report.0x00124b0022431c36.contact.False', self.on_door_open)
        self.add_trigger('report.0x00124b0022431c36.contact.True', self.on_door_close)
        self._timer_on = RunAfter(240, self.fun_on)
        self._timer_off = RunAfter(5, self.fun_off)
        self._timer_on_no_movement = RunAfter(60, self.off_light)
        self.bath_occupancy = False
    
    def on_movement(self):
        self._timer_on_no_movement.cancel()
        if self.bath_occupancy:
            self.on_light()
    
    def on_no_movement(self):
        self._timer_on_no_movement.wait()

    def off_light(self):
        wallsw = self.get_device('0x00158d0002abac97')
        if wallsw.is_on('right'):
            wallsw.off('right')


    def on_light(self):
        wallsw = self.get_device('0x00158d0002abac97')
        if wallsw.is_off('right'):
            wallsw.on('right')

    def on_door_open(self):
        if not self.bath_occupancy:
            self.on_light()
        
    def on_door_close(self):
        if (self.bath_occupancy):
            self.off_light()
        self.toggle_occupancy()
        

    def toggle_occupancy(self):
        if (self.bath_occupancy):
            self.bath_occupancy = False
        else:
            self.bath_occupancy = True

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

            
    
        