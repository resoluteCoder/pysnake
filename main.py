# Example file showing a basic pygame "game loop"
import pygame
from snake import Snake

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("red")

    # RENDER YOUR GAME HERE
    snake = pygame.Rect(640, 360, 20, 20)
    pygame.draw.rect(surface=screen, color="black", rect=snake)
    # snake = Snake()
    # pygame.draw.rect(surface=screen, color="black", rect=pygame.Rect(
    #     snake.pos_x,
    #     snake.pos_y,
    #     snake.width,
    #     snake.height
    # ))
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
