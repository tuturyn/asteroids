import pygame
from logger import log_state
from constants import PLAYER_RADIUS, SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
import sys
from shot import Shot

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    player = Player(x, y, PLAYER_RADIUS)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    return


        screen.fill("black")
        player.draw(screen)

        updatable.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid) == True:
                log_event("player_hit")
                print("\nGAME OVER\n")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid) == True:
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        for drawable_object in drawable:
            drawable_object.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

# print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
