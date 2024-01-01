# Example file showing a basic pygame "game loop"
import pygame
from snake import Snake

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
snake = Snake()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    pygame.draw.rect(surface=screen, color="green", rect=pygame.Rect(
        snake.pos_x,
        snake.pos_y,
        snake.width,
        snake.height
    ))
    
    #implement input here
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_w] or key_input[pygame.K_UP] or key_input[pygame.K_k]:
        snake.move_up()
    elif key_input[pygame.K_s] or key_input[pygame.K_DOWN] or key_input[pygame.K_j]:
        snake.move_down()
    elif key_input[pygame.K_a] or key_input[pygame.K_LEFT] or key_input[pygame.K_h]:
        snake.move_left()
    elif key_input[pygame.K_d] or key_input[pygame.K_RIGHT] or key_input[pygame.K_l]:
        snake.move_right()
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
