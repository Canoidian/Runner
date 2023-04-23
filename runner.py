import pygame
from sys import exit
from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surface, obstacle_rect)
            else:
                screen.blit(fly_surface, obstacle_rect)


        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    else: return []

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock() # Creating a clock object to control the game's framerate
test_font = pygame.font.Font('font/Pixeltype.ttf', 50) # type: ignore
game_active = False
start_time = 0
score = 0

# new images are on septate surface
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()

# score_surface = test_font.render('Runner', False, (64,64,64))
# score_rect = score_surface.get_rect(center = (400,50))

# Make sure to add the "_alpha" when converting the image, to make image background transparent
# obstacles
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()

fly_surface = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()

obstacle_rect_list = []

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_grav = 0

# Intro screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render('Pixel Runner', False, (111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

game_message = test_font.render('Press space to run', False, (111,196,169))
game_message_rect = game_message.get_rect(center = (400,330))

# timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

# Checking for Pygame events (such as quitting the game)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() # Exiting the game if the user closes the window

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_grav = -15

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_grav = -15
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time =  int(pygame.time.get_ticks() / 1000)

        if event.type == obstacle_timer and game_active:
            if randint(0,3):
                obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900,1100),300)))
        else:
            obstacle_rect_list.append(fly_surface.get_rect(bottomright = (randint(900,1100),210)))


    # draw all our elements
    # update everything
    if game_active:
        # draw the sky
        screen.blit(sky_surface,(0,0))
        # draw the ground
        screen.blit(ground_surface,(0,300))
        
        # draw the score
        score = display_score()
        # pygame.draw.rect(screen,'#c0eBec',score_rect)
        # pygame.draw.rect(screen,'#c0eBec',score_rect, 10)
        
        # draw & move the snail
        # snail_rect.x -= 4
        # if snail_rect.right <= 0: snail_rect.left = 800
        # screen.blit(snail_surface,snail_rect)

        # player
        player_grav += 0.5
        player_rect.y += player_grav # type: ignore
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf,player_rect)

        # obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # collision detection

    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)

        score_message = test_font.render(f'Your score: {score}', False, (111,196,169))
        score_message_rect = score_message.get_rect(center = (400,330))
        screen.blit(game_name,game_name_rect)

        if score == 0: 
            screen.blit(game_message,game_message_rect)
        else:
            screen.blit(score_message,score_message_rect)
        

    pygame.display.update()
    clock.tick(60)
