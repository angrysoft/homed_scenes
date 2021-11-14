from homedaemon.scenes import BaseAutomation
from pyiot.software import Time


class Scene(BaseAutomation):
    def __init__(self, sid:str):
        super().__init__(sid)
        self.name = 'hall motion'
        self.add_trigger('report.0x00158d00029a49ba.occupancy.True', self.on_motion)
        self.add_trigger('report.0x00158d00029a49ba.occupancy.False', self.on_no_motion)
        # self.add_trigger('report.0x00158d00029a49ba.no_occupancy_since.120', self.on_no_motion)
        self.add_trigger('report.0x00158d0002a18c2b.action.release_right', self.bulb_on)
    
    def on_motion(self):
        light = self.get_device('0x04cf8cdf3c8a0236')
        if int(light.status.illuminance) < 8000:
            entrance = self.get_device('0x00158d0002b74c28')
            lamp = self.get_device('0x0000000007e7bae0')
            if entrance.is_open():
                wallsw = self.get_device('0x00158d0002a18c2b')
                lamp.on()
                wallsw.on("left")


            _now = Time.get_time_now()
            bright = 40
            if _now >= Time(21):
                bright = 1
            if  lamp.is_off():
                bulb = self.get_device("0x0000000013f0bc44")
                bulb.on()
                bulb.set_bright(bright)
            
                
    def on_no_motion(self):
        wallsw = self.get_device('0x00158d0002a18c2b')
        bulb = self.get_device("0x0000000013f0bc44")
        wallsw.off("left")
        bulb.off()
    
    def bulb_on(self):
        bulb = self.get_device("0x0000000013f0bc44")
        bulb.toggle()

    