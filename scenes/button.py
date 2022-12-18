from homedaemon.scenes import BaseAutomation


class Scene(BaseAutomation):
    def __init__(self, sid: str):
        super().__init__(sid)
        self.name = "Button"
        self.add_trigger("report.0x00124b001f4502db.action.single", self.lamp_tree_toggle)
        # self.add_trigger("report.0x00124b001f4502db.action.double", self.toggle_bright)
        self.place = "Living room"

    def lamp_tree_toggle(self):
        if self.lamp_tree := self.get_device("0x00158d000283b219")
            self.lamp.toggle()
