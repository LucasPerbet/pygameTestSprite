import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):
    
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 3
        self.all_projectiles = pygame.sprite.Group()
        
        # Load images
        self.image_origin = pygame.image.load('assets/link_down.png').convert_alpha()
        self.image_up = pygame.image.load('assets/link_up.png').convert_alpha()
        self.image_left = pygame.image.load('assets/link_left.png').convert_alpha()
        self.image_right = pygame.image.load('assets/link_right.png').convert_alpha()
        
        self.rect = self.image_origin.get_rect()
        self.rect.x = 1478
        self.rect.y = 1856
        self.direction = "down"  # Initial direction
        
        # Set the current image and mask
        self.image = self.image_origin
        self.mask = pygame.mask.from_surface(self.image)

    def update_image_and_mask(self, new_image):
        """ Helper function to update image and mask """
        self.image = new_image
        self.mask = pygame.mask.from_surface(self.image)
    
    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity
            self.direction = "right"
            self.update_image_and_mask(self.image_right)
    
    def move_left(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x -= self.velocity
            self.direction = "left"
            self.update_image_and_mask(self.image_left)
    
    def move_up(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.y -= self.velocity
            self.direction = "up"
            self.update_image_and_mask(self.image_up)
    
    def move_down(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.y += self.velocity
            self.direction = "down"
            self.update_image_and_mask(self.image_origin)
    
# Exemple dans Player.py

    def launch_projectile(self):
    # Crée un nouveau projectile avec une référence au joueur actuel
        projectile = Projectile(self, self.rect.centerx, self.rect.centery, self.direction)
        self.all_projectiles.add(projectile)

