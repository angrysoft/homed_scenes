from homedaemon.scenes import BaseAutomation
from pyiot.software import Time


class Scene(BaseAutomation):
    def __init__(self, sid:str):
        super().__init__(sid)
        self.name = 'hall motion'
        self.add_trigger('report.0x00158d00029a49ba.occupancy.True', self.on_motion)
        self.add_trigger('report.0x00158d00029a49ba.no_occupancy_since.60', self.on_no_motion)
    
    def on_motion(self):
        light = self.get_device('0x04cf8cdf3c8a0236')
        if int(light.status.illuminance) < 8000:
            entrance = self.get_device('0x00158d0002b74c28')
            wallsw = self.get_device('0x00158d0002a18c2b')
            lamp = self.get_device('0x0000000007e7bae0')
            print(entrance.status.contact)
            if entrance.status.contact:
                lamp.on()
                wallsw.on("left")
            else:
                bulb = self.get_device("0x0000000013f0bc44")
                _now = Time.get_time_now()

                bright = 30

                if _now >= Time(21) and _now < Time(22):
                    bright = 17
                

                if bulb.is_on():
                    bulb.set_bright(bright)
           
                
    def on_no_motion(self):
        wallsw = self.get_device('0x00158d0002a18c2b')
        bulb = self.get_device("0x0000000013f0bc44")
        wallsw.off("left")
        bulb.off()
