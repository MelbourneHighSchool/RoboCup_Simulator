from simulation.interactor import IInteractor
from simulation.world import World
from objects.base import objectFactory
from visual.objects import visualFactory
from visual import ScreenObjectManager

class SpawnerInteractor(IInteractor):

    def __init__(self, **kwargs):
        self.prefix_key = kwargs.get('prefix', 'spawn_')
        self.items = kwargs['elements']
        self.object_map = {}

    def startUp(self, **kwargs):
        self.objects = []
        for item in self.items:
            if item['type'] == 'visual':
                vis = visualFactory(**item)
                ScreenObjectManager.instance.registerVisual(vis, self.prefix_key + item.get('key', 'object'))
                self.object_map[item.get('key', 'object')] = vis
            elif item['type'] == 'object':
                obj = objectFactory(**item)
                if item.get('physics', False):
                    World.instance.registerObject(obj)    
                ScreenObjectManager.instance.registerObject(obj, self.prefix_key + item.get('key', 'object'))
                self.object_map[item.get('key', 'object')] = obj

    def tick(self, tick):
        return False
