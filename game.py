import pygame
from player import Player
from monster import Monster

class Game:
    
    def __init__(self):
        # definir si notre jeu started ou no
        self.is_playing = False
        # generation du joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_monsters = pygame.sprite.Group()
        self.all_players.add(self.player)
        self.pressed = {}
        
        
        # Définir les murs comme des pygame.Rect
        self.walls = [
            
            # Murs verticaux de droite à gauche
            pygame.Rect(1560, 500, 60, 1422), # 1
            pygame.Rect(1390, 675, 60, 1250), # 2
            pygame.Rect(1208, 950, 60, 738),  #3
            pygame.Rect(1124, 675, 60, 280),  #4
            pygame.Rect(1040, 1075, 60, 450),  #5 
            pygame.Rect(946, 550, 60, 550),  #6
            pygame.Rect(656, 645, 60, 880),  #7
            pygame.Rect(490, 750, 60, 900),  #8
            
            # Murs horizontaux de droite à gauche
            pygame.Rect(920, 490, 650, 60), # 1
            pygame.Rect(1120, 670, 330, 60), # 2 
            pygame.Rect(683, 1470, 400, 60), # 3 
            pygame.Rect(485, 1650, 750, 60), # 4
            pygame.Rect(167,590 , 550, 60), # 5
            pygame.Rect(167,750 , 330, 60), # 6
        ]
        
    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()
            
    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.is_playing = False
        
    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
        
    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
    def check_wall_collision(self, rect):
        for wall in self.walls:
            if rect.colliderect(wall):
                return True
        return False

    def update(self, screen) :
        
        for projectile in self.player.all_projectiles:
            projectile.move()
    
        # affiche le projectile
        self.player.all_projectiles.draw(screen)
    
    
        for monster in self.all_monsters:
            monster.monster_move()
    
        self.all_monsters.draw(screen)
    
        # mouvement du joueur et affichage de l'image correspondante
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        elif self.pressed.get(pygame.K_UP) and self.player.rect.y > 0:
            self.player.move_up()
        elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y + self.player.rect.height < screen.get_height():
            self.player.move_down()

        # affiche l'image correspondant à la dernière direction
        screen.blit(self.player.image, self.player.rect)

