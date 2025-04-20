import pygame


class Hud():
    def __init__(self):
        self.score = 0
        self.text_obj = pygame.font.SysFont("Roboto", 24)
        self.score_text = self.text_obj.render(
            "Score: " + str(self.score), False, "white")

    def update(self, dt):
        self.score_text = self.text_obj.render(
            "Score: " + str(self.score), False, "white")

    def draw(self, screen):
        screen.blit(self.score_text, (5, 5))
