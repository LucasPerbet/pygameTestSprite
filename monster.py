import pygame

class Monster(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health =100
        self.attack = 5
        self.image = pygame.image.load('assets/orc.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1478
        self.rect.y = 900
        self.velocity = 1
        
    def monster_move(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.y += self.velocity
        