import pygame
from game import Game
import math
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1920

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Zelda du pauvre")

# define variables
background = pygame.image.load('assets/map1920.png').convert()

# charger l'image du menu

banner = pygame.image.load('assets/banner.png').convert_alpha()
banner_rect = banner.get_rect()
banner_rect.x = 0
banner_rect.y = 0


play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button,(256,256))
play_button_rect = play_button.get_rect()
play_button_rect.x = 875
play_button_rect.y = 1000


game = Game()

run = True
while run:
    # affiche le background
    screen.blit(background, (0, 0))
    
    # verifie si le jeu start ou non
    if game.is_playing:
        game.update(screen)
    #si le jeu n'a pas start
    else:
        # ajouter ma banner
        screen.blit(banner, (banner_rect.x, banner_rect.y))
        screen.blit(play_button, (play_button_rect.x ,play_button_rect.y))
        
    pygame.display.flip()

            
    # event de fermeture
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            
            # détecte si l'espace est enclenché
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
            
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                #mettre le je uen mode lancer 
                game.start()
                
                
pygame.quit()
