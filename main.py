import pygame
from game import Game

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1920

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Zelda du pauvre")

# define variables
background = pygame.image.load('assets/map1920.png').convert()

game = Game()

run = True
while run:
    # affiche le background
    screen.blit(background, (0, 0))
    
    
    for projectile in game.player.all_projectiles:
        projectile.move()
    
    # affiche le projectile
    game.player.all_projectiles.draw(screen)
    
    # mouvement du joueur et affichage de l'image correspondante
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
    elif game.pressed.get(pygame.K_UP) and game.player.rect.y > 0:
        game.player.move_up()
    elif game.pressed.get(pygame.K_DOWN) and game.player.rect.y + game.player.rect.height < screen.get_height():
        game.player.move_down()

    # affiche l'image correspondant à la dernière direction
    screen.blit(game.player.current_image, game.player.rect)
            
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

    pygame.display.flip()

pygame.quit()
