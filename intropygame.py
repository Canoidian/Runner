import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock() # Creating a clock object to control the game's framerate

test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# new images are on septate surface
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

score_surface = test_font.render('Runner', False, 'Black')
score_rect = score_surface.get_rect(center = (400,50))

# Make sure to add the "_alpha" when converting the image, to make image background transparent
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600,300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

# Checking for Pygame events (such as quitting the game)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() # Exiting the game if the user closes the window
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos): print('collision')

    # draw all our elements
    # update everything

    # draw the sky
    screen.blit(sky_surface,(0,0))
    # draw the ground
    screen.blit(ground_surface,(0,300))
    # draw the text
    screen.blit(score_surface,score_rect)
    
    # draw & move the snail
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surface,snail_rect)

    # draw the player
    screen.blit(player_surf,player_rect)

    # if player_rect.colliderect(snail_rect):
    #     print('collision')

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)