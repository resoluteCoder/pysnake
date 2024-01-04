# Example file showing a basic pygame "game loop"
import pygame
from snake import Snake
from food import Food


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
snake = Snake()
food = Food()
score = 0
core_font = pygame.font.SysFont("arial", 25)

def display_text(font, text, color, x, y):
    text_image = pygame.font.Font.render(font, text, True, color)
    screen.blit(text_image, (x, y))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    #draw screen for start menu
    #get text on the screen (name of game, start button and exit button)
    #allow start option to begin game
    #allow exit option to close out

    display_text(core_font, ("Welcome to Snake"), "white", 540, 200)
    display_text(core_font, ("Start"), "white", 620, 300)
    display_text(core_font, ("Quit"), "white", 623, 350)

    # RENDER YOUR GAME HERE

    pygame.draw.rect(surface=screen, color=snake.color, rect=pygame.Rect(
        snake.pos_x,
        snake.pos_y,
        snake.width,
        snake.height
    ))
    pygame.draw.rect(surface=screen, color=food.color , rect=pygame.Rect(
        food.pos_x,
        food.pos_y,
        food.width,
        food.height
    ))
    
    #implement input here
    key_input = pygame.key.get_pressed()
    up_direction = [pygame.K_w, pygame.K_UP, pygame.K_k]
    right_direction = [pygame.K_d, pygame.K_RIGHT, pygame.K_l]
    down_direction = [pygame.K_s, pygame.K_DOWN, pygame.K_j]
    left_direction = [pygame.K_a, pygame.K_LEFT, pygame.K_h]

    for direction in up_direction:
        if key_input[direction]:
            snake.move_up()

    for direction in right_direction:
        if key_input[direction]:
            snake.move_right()

    for direction in down_direction:
        if key_input[direction]:
            snake.move_down()

    for direction in left_direction:
        if key_input[direction]:
            snake.move_left()

    if snake.has_eaten(food.pos_x, food.pos_y, food.height, food.width):
        food = Food()
        score += 1

    score_text = pygame.font.Font.render(core_font, (f"Score: {score}"), True, "white")
    score_position = score_text.get_rect(center=(640, 15))
    screen.blit(score_text, score_position)


    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
