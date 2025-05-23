import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


class Hud():
    def __init__(self):
        self.score = 0
        self.death_screen_blink_counter = 0
        self.text_obj = pygame.font.SysFont("Roboto", 24)
        self.score_text = self.text_obj.render(
            "Score: " + str(self.score), False, "white")

    def update(self, dt):
        self.score_text = self.text_obj.render(
            "Score: " + str(self.score), False, "white")

    def draw(self, screen):
        screen.blit(self.score_text, (5, 5))

    def pause_screen(self, screen):
        pause_text = pygame.font.SysFont(
            "Roboto", 72).render("PAUSE", False, "white")
        screen.blit(pause_text, ((SCREEN_WIDTH / 2) -
                    100, (SCREEN_HEIGHT / 2) - 100))

    def death_screen(self, screen):
        self.death_screen_blink_counter += 1
        death_text = pygame.font.SysFont("Roboto", 72).render(
            "SMASHED TO PIECES", False, "red")
        if self.death_screen_blink_counter < 50:
            screen.blit(death_text, ((SCREEN_WIDTH / 2) -
                                     350, (SCREEN_HEIGHT / 2) - 200))
        if self.death_screen_blink_counter >= 100:
            self.death_screen_blink_counter = 0
        final_score_text = pygame.font.SysFont("Roboto", 72).render(
            f"Score: \n{self.score}", False, "white")
        screen.blit(final_score_text, ((SCREEN_WIDTH / 2) -
                    100, (SCREEN_HEIGHT / 2) - 100))
