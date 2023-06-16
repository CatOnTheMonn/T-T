class Mapmanager():
    def __init__(self):
        self.model =  'block.egg'
        self.texture = 'chs.jpg'
        self.startNew()
        self.addBlock((0, 10, 0))
    def startNew(self):
        self.land = render.attachNewNode('Land')
    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.block.reparentTo(self.land)
        self.block.setTag('at', str(position))
    def loadLand(self, filename):
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z)+1):
                        block = self.addBlock((x, y, z0))
                    x += 1
                y += 1
            return x//2, y//2
    def clear(self):
        self.land.removeNode()
        self.startNew()
    def findBlocks(self, pos):
        return self.land.findAllMatches('=at='+str(pos))
    def delBlock(self, pos):
        blocks = self.findBlocks(pos)
        for block in blocks:
            block.removeNode()