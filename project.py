import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont("Courier", 24)

def reset_game():
    snake = [(300, 300), (280, 300), (260, 300)]
    direction = (GRID_SIZE, 0)
    food = get_random_food_pos(snake)
    score = 0
    return snake, direction, food, score

def get_random_food_pos(snake):
    while True:
        x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        if (x, y) not in snake:
            return (x, y)

snake, direction, food, score = reset_game()
high_score = 0
speed = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, GRID_SIZE):
                direction = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -GRID_SIZE):
                direction = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and direction != (GRID_SIZE, 0):
                direction = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-GRID_SIZE, 0):
                direction = (GRID_SIZE, 0)

    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake):
        pygame.time.delay(1000)
        snake, direction, food, score = reset_game()
        speed = 10
        continue

    snake.insert(0, new_head)

    if new_head == food:
        score += 10
        if score > high_score:
            high_score = score
        speed += 0.5
        food = get_random_food_pos(snake)
    else:
        snake.pop()

    screen.fill(BLACK)

    for i, segment in enumerate(snake):
        color = GREEN if i == 0 else DARK_GREEN
        pygame.draw.rect(screen, color, (segment[0], segment[1], GRID_SIZE - 1, GRID_SIZE - 1))

    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE - 1, GRID_SIZE - 1))

    score_text = font.render(f"Score: {score}  High Score: {high_score}", True, WHITE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))

    pygame.display.flip()
    clock.tick(speed)
