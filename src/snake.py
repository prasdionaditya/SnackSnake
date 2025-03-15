import pygame
import time
import random
from utils import draw_snake, draw_food, check_collision

pygame.init()

#define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
dark_green = (0, 100, 0)
light_brown = (210, 180, 140)

#define dimensions
dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))

pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 11

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

def message(text, color):
    msg = font_style.render(text, True, color)
    dis.blit(msg, [dis_width/6, dis_height/3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = snake_block
    y1_change = 0

    #snake initialization
    snake_list = [[x1, y1], [x1 - snake_block, y1]]
    Length_of_snake = 2

    foodx = round(random.randrange(0, dis_width - snake_block)/10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block)/10.0) * 10.0

    direction = 'right'

    while not game_over:

        while game_close == True:
            dis.fill(light_brown)
            message("Quit (Q) or Replay (C)?", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'right':
                    x1_change = -snake_block
                    y1_change = 0
                    direction = 'left'
                elif event.key == pygame.K_RIGHT and direction != 'left':
                    x1_change = snake_block
                    y1_change = 0
                    direction = 'right'
                elif event.key == pygame.K_UP and direction != 'down':
                    y1_change = -snake_block
                    x1_change = 0
                    direction = 'up'
                elif event.key == pygame.K_DOWN and direction != 'up':
                    y1_change = snake_block
                    x1_change = 0
                    direction = 'down'

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change

        dis.fill(light_brown)

        #food initialization
        draw_food(dis, white, foodx, foody, snake_block)

        snake_Head = [x1, y1]
        snake_list.append(snake_Head)
        if len(snake_list) > Length_of_snake:
            del snake_list[0]
        
        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True

        # snake colorization
        for i, segment in enumerate(snake_list):
            if i == len(snake_list) - 1:
                pygame.draw.rect(dis, red, [segment[0], segment[1], snake_block, snake_block])
            else:
                pygame.draw.rect(dis, dark_green, [segment[0], segment[1], snake_block, snake_block])

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block)/10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block)/10.0) * 10.0
            Length_of_snake += 1
            
        clock.tick(snake_speed)
    
    pygame.quit()
    quit()

gameLoop()

#uhh..