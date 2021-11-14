from homedaemon.scenes import BaseAutomation


class Scene(BaseAutomation):
    def __init__(self, sid:str):
        super().__init__(sid)
        self.name = 'bedroom motion'
        self.add_trigger('report.0x00158d0002ec03fe.no_occupancy_since.120', self.on_no_motion)

    def on_no_motion(self):
        wallsw = self.get_device('0x00158d0002a16338')
        wallsw.off("left")
        wallsw.off("right")

        bedlamp = self.get_device('0x000000000545b741')
        bedlamp.off()
