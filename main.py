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

# create new screen for menu
# needs only the text to display menu
# needs its own loop to run and button/action can allow the game to run or quit
# needs buttons or keystrokes to start game
# if buttons are used, needs collision with rect
# if keystrokes are used it needs if statement to reflect which keys are necessary to do actions

def main_menu():
    # menu loop, took from game loop, just changed running to a simple bool True statement during testing and worked
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # new screen dedicated to only the main menu
        screen.fill("dark gray")

        # text displayed on screen. used updated function that replaced display_text
        draw_text("Welcome to Snake", 50, "green", 640, 200)
        draw_text("Press SPACE to Play", 36, "white", 640, 400)
        draw_text("Press Q to Quit", 36, "white", 640, 450)

        # used keystrokes since my brain was hurting looking up buttons
        #took from game loop controls and various pygame doc examples
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return True
        elif keys[pygame.K_q]:
            pygame.quit()
            quit()

        # took from game loop/pygame docs
        pygame.display.flip()
        clock.tick(60)

# updated display_text function for more readability and better functionality
def draw_text(text, size, color, x, y):
    font = pygame.font.SysFont("arial", size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

main_menu()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

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

    draw_text((f"Score: {score}"), 25, "white", 640, 15)

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
