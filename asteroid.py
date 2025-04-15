from circleshape import * 
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0         # Default rotation, can be overridden
        self.velocity = pygame.Vector2(0, 0)  
        self.position = pygame.Vector2(x, y)  
    def draw(self,screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)
    def update(self, dt):
        self.move(dt) # self.position += self.velocity * dt
    def move(self, dt):
    # Calculate the forward direction based on the asteroid's rotation
        forward = pygame.Vector2(0, -1).rotate(self.rotation)  # Negative y moves "up"

        # Update the position using velocity, direction, and time delta
        self.position += forward * self.velocity.length() * dt

        # (Optional) Check if the asteroid is off-screen and wrap it
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = SCREEN_WIDTH

        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # randomize the angle of the split
        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2


            
        #elif(self.radius == ASTEROID_MAX_RADIUS):
         #   random_angle = random.uniform(20,50)
          #  right = self.velocity.rotate(random_angle)
           # left= self.velocity.rotate(-random_angle)
            #new_radius = self.radius - 2*ASTEROID_MIN_RADIUS
            #r_ast = Asteroid(right.x,right.y,new_radius)
            #r_ast.velocity  = right * 1.2
            #l_ast = Asteroid(left.x,left.y,new_radius)
            #l_ast.velocity= left * 1.2

            
            
            