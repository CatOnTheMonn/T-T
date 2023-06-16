from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        x, y = self.land.loadLand('land.txt') 
        z = 2
        #x = 10
        #y = 22
        self.hero = Hero((x, y, z), self.land)
        base.camLens.setFov(90)
game = Game()
game.run()