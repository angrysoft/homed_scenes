from homedaemon.scenes import BaseAutomation
from pyiot.software import Time
import os

class Scene(BaseAutomation):
    def __init__(self,sid:str):
        super().__init__(sid)
        self.name = 'Livingroom motion'
        self.add_trigger('report.0x00158d0002a13819.contact.False', self.on_door_open)
        self.add_trigger('report.0x00158d0002a13819.contact.True', self.on_door_close)
        self.add_trigger('report.0x00158d0002ec2fa6.occupancy.True', self.on_motion)
        self.add_trigger('report.0x0000000007e7bae0.power.on', self.on_power_on)
        self.add_trigger('report.clock.time.21.00.00', self.on_power_on)
        self.add_trigger('report.clock.time.22.00.00', self.on_power_on)
        self.add_trigger('report.clock.time.23.00.00', self.on_power_on)
        self.add_trigger('report.0x00158d0002ec2fa6.no_occupancy_since.900', self.power_off)
        self.place = 'Living room'
    
    def on_motion(self):
        lamp = self.get_device('0x0000000007e7bae0')
        light = self.get_device('0x04cf8cdf3c8a0236')
        if os.path.exists("/etc/homedaemon/lamp_disable"):
            return
            
        if int(light.status.illuminance) < 9500: # and Time.get_time_now() < Time(23):
            lamp.on()
        else:
            lamp.off()
    
    def power_off(self):
        lamp = self.get_device('0x0000000007e7bae0')
        lamp.off()
    
    def on_power_on(self):
        self.set_lamp()

    def set_lamp(self):
        lamp = self.get_device('0x0000000007e7bae0')
      
        _now = Time.get_time_now()

        bright = 30
        ct = 50

        if _now >= Time(21) and _now < Time(22):
            bright = 17
            ct = 17
        elif _now >= Time(22) and _now < Time(23):
            bright = 10
            ct = 10
        elif _now >= Time(23) or _now < Time(6):
            bright = 1
            ct = 1

        if lamp.is_on():
            lamp.set_bright(bright)
            lamp.set_ct_pc(ct)
            
    def on_door_open(self):
        light = self.get_device('0x04cf8cdf3c8a0236')
        lamp = self.get_device('1000b6e1c8')
        if int(light.status.illuminance) < 7000:
            lamp.on()
    
    def on_door_close(self):
        lamp = self.get_device('1000b6e1c8')
        if lamp.is_on():
            lamp.off()