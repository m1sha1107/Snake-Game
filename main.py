import pygame
import time
import random
from pygame.locals import *

pygame.init()

# Define colors
red = (255, 0, 0)
green = (0, 255, 0)
black = (0,0,0)

# Window size
win_width = 600
win_height = 400

# Create the game window
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Snake Game")

# Define snake properties
snake_size = 10
snake_speed = 15

# Define fonts for rendering
font_style = pygame.font.SysFont("calibri", 26)
score_font = pygame.font.SysFont("comicsansms", 30)

# Define function to render score
def render_score(score):
    score_text = score_font.render("Score: " + str(score), True, red)
    window.blit(score_text, [10, 10])

# Function to draw snake
def draw_snake(snake_segments):
    for segment in snake_segments:
        pygame.draw.rect(window, green, [segment[0], segment[1], snake_size, snake_size])

# Function to display messages
def display_messages(msg):
    message_text = font_style.render(msg, True, red)
    window.blit(message_text, [win_width / 6, win_height / 3])

# Main game loop
def game_loop():
    # Initialize game variables
    game_over = False
    game_close = False  # Added a variable to handle game over state

    snake_segments = [[win_width // 2, win_height // 2]]
    snake_length = 1

    x_change = 0
    y_change = 0

    food_x = round(random.randrange(0, win_width - snake_size) / snake_size) * snake_size
    food_y = round(random.randrange(0, win_height - snake_size) / snake_size) * snake_size

    clock = pygame.time.Clock()

    while not game_over:
        while game_close:
            window.fill(black)
            display_messages("You Lost! Press Q to Quit or C to Play Again")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        game_over = True
                        game_close = False
                    if event.key == K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    x_change = -snake_size
                    y_change = 0
                elif event.key == K_RIGHT:
                    x_change = snake_size
                    y_change = 0
                elif event.key == K_UP:
                    y_change = -snake_size
                    x_change = 0
                elif event.key == K_DOWN:
                    y_change = snake_size
                    x_change = 0

        # Update snake position
        head = [snake_segments[0][0] + x_change, snake_segments[0][1] + y_change]
        snake_segments.insert(0, head)

        if len(snake_segments) > snake_length:
            del snake_segments[-1]

        # Check for collisions
        if head[0] >= win_width or head[0] < 0 or head[1] >= win_height or head[1] < 0:
            game_close = True
        for segment in snake_segments[1:]:
            if segment == head:
                game_close = True

        # Check for food collision
        if head[0] == food_x and head[1] == food_y:
            food_x = round(random.randrange(0, win_width - snake_size) / snake_size) * snake_size
            food_y = round(random.randrange(0, win_height - snake_size) / snake_size) * snake_size
            snake_length += 1

        # Draw game elements
        window.fill(black)
        pygame.draw.rect(window, red, [food_x, food_y, snake_size, snake_size])
        draw_snake(snake_segments)
        render_score(snake_length - 1)

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Run the game
game_loop()
