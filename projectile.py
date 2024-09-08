import pygame

class Projectile(pygame.sprite.Sprite):
    
    def __init__(self, player, x, y, direction):
        super().__init__()
        self.player = player  # Assigner le joueur passé en paramètre à l'attribut player
        self.velocity = 5
        
        # Load all the arrow images
        self.image_arrow_right = pygame.image.load("assets/arrow_right.png")
        self.image_arrow_left = pygame.image.load("assets/arrow_left.png")
        self.image_arrow_down = pygame.image.load("assets/arrow_down.png")
        self.image_arrow_up = pygame.image.load("assets/arrow_up.png")
        
        # Set the initial direction and image
        self.direction = direction
        self.update_image_and_rect(x, y)
    
    def update_image_and_rect(self, x, y):
        # Update the image based on direction
        if self.direction == "right":
            self.image = self.image_arrow_right
        elif self.direction == "left":
            self.image = self.image_arrow_left
        elif self.direction == "up":
            self.image = self.image_arrow_up
        elif self.direction == "down":
            self.image = self.image_arrow_down
        
        # Update the rect based on the new image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def move(self):
        # Move the projectile based on the direction
        if self.direction == "right":
            self.rect.x += self.velocity
        elif self.direction == "left":
            self.rect.x -= self.velocity
        elif self.direction == "up":
            self.rect.y -= self.velocity
        elif self.direction == "down":
            self.rect.y += self.velocity
        
        # Check for collisions
        if self.player.game.check_collision(self, self.player.game.all_monsters):
            self.kill()
        
        # Remove the projectile if it goes off-screen
        if self.rect.x < 0 or self.rect.x > 1920 or self.rect.y < 0 or self.rect.y > 1920:
            self.kill()
