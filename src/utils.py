import pygame

def draw_snake(dis, color, snake_list, snake_block):
    for x in snake_list:
        pygame.draw.rect(dis, color, [x[0], x[1], snake_block, snake_block])

def draw_food(dis, color, foodx, foody, snake_block):
    pygame.draw.rect(dis, color, [foodx, foody, snake_block, snake_block])

def check_collision(x1, y1, foodx, foody, snake_block):
    return x1 == foodx and y1 == foody