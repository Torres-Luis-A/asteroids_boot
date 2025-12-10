import pygame, sys, os
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    VERSION = pygame.version.ver
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable)
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    asteroid_field = AsteroidField()
    score = 0
    score_increment = 10
    while True:
        log_state()
        dt = clock.tick(60) / 1000
        font = pygame.font.Font(None, 36)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
            score_text = font.render(f"Score: {score}", True, (255, 255, 255))
            screen.blit(score_text, (10, 10))  
        updatable.update(dt)

            # check for collisions
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print(f"Game Over! Score: {score}")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    score += score_increment

        pygame.display.flip()
if __name__ == "__main__":
    main()
