from homedaemon.scenes import BaseAutomation


class Scene(BaseAutomation):
    def __init__(self, sid: str):
        super().__init__(sid)
        self.name = "tree lamp"
        self.add_trigger("report.0x00158d000200a020.action.single", self.toggle_tree)
        self.add_trigger("report.0x00124b001f4502db.action.single", self.toggle_tree)
        # self.add_trigger("report.0x00158d000200a020.action.double", self.toggle_light)

    def toggle_tree(self):
        self.strip_switch = self.get_device("0x00158d000283b219")
        if self.strip_switch:
            self.strip_switch.toggle()
