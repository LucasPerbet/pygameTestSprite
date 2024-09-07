import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 3
        self.all_projectiles = pygame.sprite.Group()
        self.image_origin = pygame.image.load('assets/link_down.png')
        self.image_up = pygame.image.load('assets/link_up.png')
        self.image_left = pygame.image.load('assets/link_left.png')
        self.image_right = pygame.image.load('assets/link_right.png')
        self.rect = self.image_origin.get_rect()
        self.rect.x = 1478
        self.rect.y = 1856
        self.direction = "down"  # Initial direction
        self.current_image = self.image_origin

    def move_right(self):
        self.rect.x += self.velocity
        self.direction = "right"
        self.current_image = self.image_right

    def move_left(self):
        self.rect.x -= self.velocity
        self.direction = "left"
        self.current_image = self.image_left
        
    def move_up(self):
        self.rect.y -= self.velocity
        self.direction = "up"
        self.current_image = self.image_up
        
    def move_down(self):
        self.rect.y += self.velocity
        self.direction = "down"
        self.current_image = self.image_origin
    
    def launch_projectile(self):
        # Créer un nouveau projectile en fonction de la direction actuelle du personnage
        projectile = Projectile(self.rect.centerx, self.rect.centery, self.direction)
        self.all_projectiles.add(projectile)
