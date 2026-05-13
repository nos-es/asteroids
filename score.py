import pygame


class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(self.containers)

        self.score = 0
        self.font = pygame.font.Font(None, 36)

    def update(self, amount):
        self.score += amount

    def draw(self, screen):
        score_text = self.font.render(str(self.score), True, "white")
        screen.blit(score_text, (20, 20))
