from direct.showbase.ShowBase import ShowBase
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.model = loader.loadModel('Boeing707.egg')
        self.model.reparentTo(render)
        self.model.setH(90)
        self.model.setScale(0.1)
        base.camLens.setFov(90)
game = Game()
game.run()