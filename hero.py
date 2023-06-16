class Hero():
    def __init__(self,pos,land):
        self.land = land
        self.hero = loader.loadModel("smiley")
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()
    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True
    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2] - 3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False
    def accept_events(self):
        base.accept('c', self.changeView)
        base.accept('arrow_left', self.tl)
        base.accept('arrow_left' + '-repeat', self.tl)
        base.accept('arrow_right', self.tr)
        base.accept('arrow_right' + '-repeat', self.tr)
        base.accept('w', self.gf)
        base.accept('w' + '-repeat', self.gf)
        base.accept('s', self.gb)
        base.accept('s' + '-repeat', self.gb)
        base.accept('a', self.gl)
        base.accept('a' + '-repeat', self.gl)
        base.accept('d', self.gr)
        base.accept('d' + '-repeat', self.gr)
        base.accept('e', self.fykaUP)
        base.accept('e' + '-repeat', self.fykaUP)
        base.accept('q', self.fykaDOWN)
        base.accept('q' + '-repeat', self.fykaDOWN)
        base.accept("mouse1", self.build)
        base.accept('mouse3', self.destroy)
    def changeView(self):
        if self.cameraOn == True:
            self.cameraUp()
        elif self.cameraOn == False:
            self.cameraBind()
    def tl(self):
        a = self.hero.getH()
        a = (a + 5)%360
        self.hero.setH(a)
    def tr(self):
        a = self.hero.getH()
        a = (a - 5)%360
        self.hero.setH(a)
    def gf(self):
        angel = self.hero.getH()
        posss = self.look_at(angel)
        self.hero.setPos(posss)
    def gb(self):
        angel = self.hero.getH()+180
        posss = self.look_at(angel)
        self.hero.setPos(posss)
    def gr(self):
        angel = self.hero.getH()+270
        posss = self.look_at(angel)
        self.hero.setPos(posss)
    def gl(self):
        angel = self.hero.getH()+90
        posss = self.look_at(angel)
        self.hero.setPos(posss)
    def check_dir(self,angle):
        if angle >= 0 and angle <= 20:
            return (0, -1)
        elif angle <= 65:
            return (1, -1)
        elif angle <= 110:
            return (1, 0)
        elif angle <= 155:
            return (1, 1)
        elif angle <= 200:
            return (0, 1)
        elif angle <= 245:
            return (-1, 1)
        elif angle <= 290:
            return (-1, 0)
        elif angle <= 335:
            return (-1, -1)
        else:
            return (0, -1)
    def look_at(self, angel):
        x_from = round(self.hero.getX())
        y_from = round(self.hero.getY())
        z_from = round(self.hero.getZ())

        dx, dy =  self.check_dir(angel)
        x_to = x_from + dx
        y_to = y_from + dy
        return x_to, y_to, z_from
    
    def build(self):
        angle = self.hero.getH()
        posss = self.look_at(angle)
        self.land.addBlock(posss)

    def destroy(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        self.land.delBlock(pos)

    def fykaUP(self):
        z = self.hero.getZ()
        self.hero.setZ(z + 1)
    def fykaDOWN(self):
        z = self.hero.getZ()
        self.hero.setZ(z - 1)
