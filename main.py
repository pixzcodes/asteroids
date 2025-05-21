import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from hud import Hud


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    flag_paused = False
    flag_dead = False
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # set groups as containers for object classes
    Hud.containers = (updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    hud = Hud()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        keys = pygame.key.get_just_pressed()

        # flip the pause flag when ESC is pressed
        if keys[pygame.K_ESCAPE]:
            flag_paused = not flag_paused

        if flag_dead:
            # TODO: add death animation
            screen.fill("black")
            hud.death_screen(screen)
        elif flag_paused:
            hud.pause_screen(screen)
        else:
            updatable.update(dt)

            screen.fill("black")

            for obj in drawable:
                obj.draw(screen)

            # if player collides with an asteroid, end the game
            for asteroid in asteroids:
                if asteroid.checkCollision(player):
                    flag_dead = True
                # check for collision with shots, kill both objects
                for shot in shots:
                    if asteroid.checkCollision(shot):
                        hud.score += asteroid.radius * 2
                        asteroid.split()
                        shot.kill()

            hud.update(dt)
            hud.draw(screen)

        dt = clock.tick(60) / 1000

        pygame.display.flip()  # always call this last


if __name__ == "__main__":
    main()
