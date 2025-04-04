import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while (True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        pygame.display.flip()  # always call this last
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
