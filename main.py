from direct.showbase.ShowBase import ShowBase
from keybindings.device_listener import DeviceListener, SinglePlayerAssigner
from game.gui import Gui
from game.vehicles import PlayerCar, spawn
from game.trackgen import DummyTrackGenerator


def set_faux_lights(node):
    for light in node.find_all_matches('**/*light*'):
        light.set_alpha_scale(0.1)
        light.set_transparency(True)

def child_dict(model):
    nodes = {}
    for node in model.get_children():
        node.detach_node()
        set_faux_lights(node)
        node.clear_transform()
        nodes[node.name] = node
    return nodes


class Base(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.device_listener = DeviceListener(SinglePlayerAssigner())
        self.gui = Gui()
        self.dt = 1
        self.enemies = []
        self.models = {}
        # Load track generator
        self.trackgen = DummyTrackGenerator()
        self.trackgen.register_spawn_callback(spawn)
        # Load cars
        car_models = loader.load_model("assets/models/cars.bam")
        self.models["cars"] = child_dict(car_models)
        self.player = PlayerCar(self.models["cars"]["player"])
        # Testroad
        self.models["testroad"] = loader.load_model("assets/models/testroad.bam")
        set_faux_lights(self.models["testroad"])
        for i in range(20):
            r = self.models["testroad"].copy_to(render)
            r.set_y(i*260)
        self.task_mgr.add(self.player.input)
        self.task_mgr.add(self.tick)

    def tick(self, task=None):
        self.dt = globalClock.get_dt()
        return task.cont

if __name__ == "__main__":
    base = Base()
    base.run()
