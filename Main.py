import pygame
import math
pygame.init()
WIDTH = 1100
HEIGHT = 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
surface = pygame.Surface([WIDTH, HEIGHT], pygame.SRCALPHA)
pygame.display.set_caption('Tic-Tac-Toe')
pygame.font.init()
logo = pygame.font.SysFont('Comic Sans MS', 70)
clock = pygame.time.Clock()
running = True
dt = 0
t1 = pygame.time.get_ticks()
transparency = 255
follow_cursor = True
game_paused = False
distance_list = []
top_left_placed = False
current_player = 'X'
X = pygame.transform.scale(pygame.image.load("output-onlinepngtools-removebg-preview.png").convert_alpha(), (250, 250))
Y = pygame.transform.scale(pygame.image.load("image-removebg-preview.png").convert_alpha(), (250, 250))
mouse_pos = pygame.mouse.get_pos()
center = screen.get_rect().center
pygame.mouse.set_visible(False)
bg = pygame.transform.scale(pygame.image.load("tic-tac-toe-game-for-imessage-messages-sticker-0-tic-tac-toe-layout-11562970968nlsrfat1uq-removebg-preview.png").convert_alpha(), (800, 800))
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_img = X
top_left = pygame.draw.rect(screen, 'black', (0,0, 1, 1))
vector_top_left = pygame.Vector2(bg.get_width()/6 + 300, bg.get_height()/6 + 100)
vector_top_middle = pygame.Vector2(bg.get_width()/2 + 300, bg.get_height()/6 + 100)
vector_top_right = pygame.Vector2(bg.get_width()/6*5 + 300, bg.get_height()/6 + 100)
vector_middle_left = pygame.Vector2(bg.get_width()/6 + 300, bg.get_height()/2 + 100)
vector_middle = pygame.Vector2(bg.get_width()/2 + 300, bg.get_height()/2 + 100)
vector_middle_right = pygame.Vector2(bg.get_width()/6*5 + 300, bg.get_height()/2 + 100)
vector_bottom_left = pygame.Vector2(bg.get_width()/6 + 300, bg.get_height()/6*5 + 100)
vector_bottom_middle = pygame.Vector2(bg.get_width()/2 + 300, bg.get_height()/6*5 + 100)
vector_bottom_right = pygame.Vector2(bg.get_width()/6*5 + 300, bg.get_height()/6*5 + 100)
vector_list = [vector_top_left, vector_top_middle, vector_top_right, vector_middle_left, vector_middle, vector_middle_right, 
               vector_bottom_left, vector_bottom_middle, vector_bottom_right]
top_left_placed = False
top_middle_placed = False
top_right_placed = False
middle_left_placed = False
middle_placed = False
middle_right_placed = False
bottom_left_placed = False
bottom_middle_placed = False
bottom_right_placed = False
placed_list = [top_left_placed, top_middle_placed,top_right_placed,middle_left_placed,middle_placed,middle_right_placed,bottom_left_placed,bottom_middle_placed,bottom_right_placed]
title = logo.render('Tic-Tac-Toe', False, (0, 0, 0))

def place_img():
    if current_player == "X":
        if top_left_placed == True:   
            screen.blit(X, (300,100))
        if top_middle_placed == True:
            screen.blit(X, (300 + bg.get_width()/3,100))
        if top_right_placed == True:
            screen.blit(X, (300 + bg.get_width()/3*2,100))
        if middle_left_placed == True:
            screen.blit(X, (300,100 + bg.get_height()/3))
        if middle_placed == True:
            screen.blit(X, (300 + bg.get_width()/3,100 + bg.get_height()/3))
        if middle_right_placed == True:
            screen.blit(X, (300 + bg.get_width()/3*2, 100 + bg.get_height()/3))
        if bottom_left_placed == True:
            screen.blit(X, (300,100 + bg.get_width()/3*2))
        if bottom_middle_placed == True:
            screen.blit(X, (300 + bg.get_width()/3,100 + bg.get_width()/3*2))
        if bottom_right_placed == True:
            screen.blit(X, (300 + bg.get_width()/3*2,100 + bg.get_width()/3*2))
    if current_player == "Y":
        if top_left_placed == True:   
            screen.blit(Y, (300,100))
        if top_middle_placed == True:
            screen.blit(Y, (300 + bg.get_width()/3,100))
        if top_right_placed == True:
            screen.blit(Y, (300 + bg.get_width()/3*2,100))
        if middle_left_placed == True:
            screen.blit(Y, (300,100 + bg.get_height()/3))
        if middle_placed == True:
            screen.blit(Y, (300 + bg.get_width()/3,100 + bg.get_height()/3))
        if middle_right_placed == True:
            screen.blit(Y, (300 + bg.get_width()/3*2, 100 + bg.get_height()/3))
        if bottom_left_placed == True:
            screen.blit(Y, (300,100 + bg.get_width()/3*2))
        if bottom_middle_placed == True:
            screen.blit(Y, (300 + bg.get_width()/3,100 + bg.get_width()/3*2))
        if bottom_right_placed == True:
            screen.blit(Y, (300 + bg.get_width()/3*2,100 + bg.get_width()/3*2))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:  
            if position_vector == 0 and placed_list[0] == False:
                top_left_placed = True
            elif position_vector == 1 and placed_list[1] == False:
                top_middle_placed = True
            elif position_vector == 2 and placed_list[2] == False:
                top_right_placed = True
            elif position_vector == 3 and placed_list[3] == False:
                middle_left_placed = True
            elif position_vector == 4 and placed_list[4] == False:
                middle_placed = True
            elif position_vector == 5 and placed_list[5] == False:
                middle_right_placed = True
            elif position_vector == 6 and placed_list[6] == False:
                bottom_left_placed = True
            elif position_vector == 7 and placed_list[7] == False:
                bottom_middle_placed = True
            elif position_vector == 8 and placed_list[8] == False:
                bottom_right_placed = True
            if current_player == "X":
                current_player = "Y"
            elif current_player == "Y":
                current_player = "X"
                    

    screen.fill("white")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE] and game_paused == False and pygame.time.get_ticks() - t1 > 300:
        follow_cursor = False
        game_paused = True
        pygame.mouse.set_visible(True)
        t1 = pygame.time.get_ticks()
        bg.set_alpha(120)
        player_img.set_alpha(120)
    elif keys[pygame.K_ESCAPE] and game_paused == True and pygame.time.get_ticks() - t1 > 300:
        follow_cursor = True
        game_paused = False
        pygame.mouse.set_visible(False)
        pygame.mouse.set_pos(player_pos.x + player_img.get_width() / 2, player_pos.y + player_img.get_height() / 2)
        t1 = pygame.time.get_ticks()
        bg.set_alpha(255)
        player_img.set_alpha(255)
    
    x, y = pygame.mouse.get_pos()

    
    '''line_top_left = pygame.draw.line(screen, "white", vector_top_left, pygame.mouse.get_pos())
    line_top_left = pygame.draw.line(screen, "white", vector_top_middle, pygame.mouse.get_pos())
    line_top_left = pygame.draw.line(screen, "white", vector_top_right, pygame.mouse.get_pos())
    line_top_left = pygame.draw.line(screen, "white", vector_middle_left, pygame.mouse.get_pos())
    line_top_left = pygame.draw.line(screen, "white", vector_middle, pygame.mouse.get_pos())
    line_top_left = pygame.draw.line(screen, "white", vector_middle_right, pygame.mouse.get_pos())
    line_top_left = pygame.draw.line(screen, "white", vector_bottom_left, pygame.mouse.get_pos())
    line_top_left = pygame.draw.line(screen, "white", vector_bottom_middle, pygame.mouse.get_pos())
    line_top_left = pygame.draw.line(screen, "white", vector_bottom_right, pygame.mouse.get_pos())'''
    smallest = 10000000
    for i in range(9):
        distance = math.sqrt((vector_list[i].x - x) ** 2 + (vector_list[i].y - y) ** 2)
        if distance < smallest:
            position_vector = i
            smallest = distance
      
    if position_vector == 0 and top_left_placed == False:
        current_tile = pygame.draw.rect(screen, (226, 226, 226), (300,100, bg.get_width()/3, bg.get_height()/3))
    elif position_vector == 1:
        current_tile = pygame.draw.rect(screen, (226, 226, 226), (300 + bg.get_width()/3,100, bg.get_width()/3, bg.get_height()/3))
    elif position_vector == 2:
        current_tile = pygame.draw.rect(screen, (226, 226, 226), (300 + bg.get_width()/3*2,100, bg.get_width()/3, bg.get_height()/3))
    elif position_vector == 3:
        current_tile = pygame.draw.rect(screen, (226, 226, 226), (300,100 + bg.get_height()/3, bg.get_width()/3, bg.get_height()/3))
    elif position_vector == 4:
        current_tile = pygame.draw.rect(screen, (226, 226, 226), (300 + bg.get_width()/3,100 + bg.get_height()/3, bg.get_width()/3, bg.get_height()/3))
    elif position_vector == 5:
        current_tile = pygame.draw.rect(screen, (226, 226, 226), (300 + bg.get_width()/3*2, 100 + bg.get_height()/3, bg.get_width()/3, bg.get_height()/3))
    elif position_vector == 6:
        current_tile = pygame.draw.rect(screen, (226, 226, 226), (300,100 + bg.get_width()/3*2, bg.get_width()/3, bg.get_height()/3))
    elif position_vector == 7:
        current_tile = pygame.draw.rect(screen, (226, 226, 226), (300 + bg.get_width()/3,100 + bg.get_width()/3*2, bg.get_width()/3, bg.get_height()/3))
    elif position_vector == 8:
        current_tile = pygame.draw.rect(screen, (226, 226, 226), (300 + bg.get_width()/3*2,100 + bg.get_width()/3*2, bg.get_width()/3, bg.get_height()/3))

    
    
    
    screen.blit(surface, (800, 0))
    screen.blit(bg, (300, 100 ))
    if follow_cursor == True:
        player_pos.x = x - player_img.get_width() / 2
        player_pos.y = y - player_img.get_height() / 2
    screen.blit(player_img, player_pos)
    screen.blit(title, (WIDTH / 2 -30, 15))    
    place_img()
    

    pygame.display.flip()
    dt = clock.tick(30) / 1000

pygame.quit()