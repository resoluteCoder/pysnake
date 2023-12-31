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
    screen.fill("red")

    # RENDER YOUR GAME HERE

    pygame.draw.rect(surface=screen, color="black", rect=pygame.Rect(
        snake.pos_x,
        snake.pos_y,
        snake.width,
        snake.height
    ))
    
    #implement input here
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_w]:
        # print("press w")
        snake.move_up()
    elif key_input[pygame.K_s]:
        # print("press s")
        snake.move_down()
    elif key_input[pygame.K_a]:
        # print("press a")
        snake.move_left()
    elif key_input[pygame.K_d]:
        # print("press d")
        snake.move_right()
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
