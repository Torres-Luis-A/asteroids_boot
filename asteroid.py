import pygame,random
from circleshape import CircleShape
from constants import LINE_WIDTH,ASTEROID_MIN_RADIUS,ASTEROID_MAX_RADIUS
from logger import log_event

class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    def update(self, dt):
        self.position += self.velocity * dt
    def split(self,):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            directiona = self.velocity.rotate(angle)
            directionb = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_a.velocity = directiona*1.2
            asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_b.velocity = directionb*1.2

