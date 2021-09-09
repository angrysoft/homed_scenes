from homedaemon.scenes import BaseAutomation


class Scene(BaseAutomation):
    def __init__(self, sid:str):
        super().__init__(sid)
        self.name = 'hall motion'
        self.add_trigger('report.158d00029a49ba.occupancy.True', self.on_motion)
        self.add_trigger('report.158d00029a49ba.no_occupancy_since.60', self.on_no_motion)
    
    def on_motion(self):
        light = self.get_device('0x04cf8cdf3c8a0236')
        if int(light.status.illuminance) < 8000:
            entrance = self.get_device('158d0002b74c28')
            wallsw = self.get_device('158d0002a18c2b')
            lamp = self.get_device('0x0000000007e7bae0')
            if entrance.status.status == 'false':
                lamp.on()
                wallsw.on("left")
            else:
                pass
                #  on bubl
                # if is after 21 dimm bulb

                
    def on_no_motion(self):
        wallsw = self.get_device('158d0002a18c2b')
        wallsw.off("left")
