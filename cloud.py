from random import randint, choice
from gameobject import GameObject

class Cloud(GameObject):
    def __init__(self):
        super(Cloud, self).__init__(0, 0, choice(['images/cloud1.png', 'images/cloud2.png', 'images/cloud3.png']))
        self.dx = (randint(50, 150) /100)
        self.reset()

    def move(self):
        self.x +=self.dx
        if self.x > 375:
            self.reset()
    
    def reset(self):
        self.x = -64
        self.y = randint(0, 667)