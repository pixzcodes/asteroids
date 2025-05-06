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

        if keys[pygame.K_ESCAPE]:
            flag_paused = False if flag_paused else True

        updatable.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        # if player collides with an asteroid, end the game
        for asteroid in asteroids:
            if asteroid.checkCollision(player):
                print("Game Over")
                return
            # check for collision with shots, kill both objects
            for shot in shots:
                if asteroid.checkCollision(shot):
                    hud.score += 100
                    asteroid.split()
                    shot.kill()

        hud.update(dt)
        hud.draw(screen)

        dt = clock.tick(60) / 1000

        # check for pause
        if flag_paused:
            dt = 0
            hud.pause_screen(screen)

        pygame.display.flip()  # always call this last


if __name__ == "__main__":
    main()
