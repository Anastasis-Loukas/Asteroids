from circleshape import * 
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, SHOT_RADIUS)
        #self.rotation = 0         # Default rotation, can be overridden
        #self.velocity = pygame.Vector2(0, 0)  
        #self.position = pygame.Vector2(x, y)  
    def draw(self,screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)
    def update(self, dt):
        self.move(dt) # self.position += self.velocity * dt
    def move(self, dt):
        self.position += self.velocity * dt
