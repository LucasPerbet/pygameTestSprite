from player import Player
from monster import Monster
import pygame

class Game:
    
    def __init__(self):
        
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_monsters = pygame.sprite.Group()
        self.all_players.add(self.player)
        self.pressed = {}
        self.spawn_monster()
        
    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
        
    def check_collision(self, sprite, group):  # Corrigé : "check_collision"
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
