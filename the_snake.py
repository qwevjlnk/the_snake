from random import choice, randint

import pygame

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 20

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()


# Тут опишите все классы игры.
class GameObject:
    """kdsj"""

    position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def __init__(self, position=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
                 body_color=(255, 255, 255)):
        self.position = position
        self.body_color = body_color

    def draw():
        """Kdsj"""
        pass


class Apple(GameObject):
    """kdsj"""

    position = (0, 0)

    def __init__(self):
        self.body_color = (255, 0, 0)
        self.randomize_position()

    def randomize_position(self):
        """Kdsj"""
        self.position = (randint(0, GRID_WIDTH) * GRID_SIZE,
                         randint(0, GRID_HEIGHT) * GRID_SIZE)

    def draw(self):
        """Kdsj"""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """kdsj"""

    length = 1
    positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
    direction = RIGHT
    next_direction = None
    body_color = (0, 255, 0)

    def __init__(self):
        self.length = 1
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = RIGHT
        self.next_direction = None
        self.body_color = (0, 255, 0)
        self.last = None

    def update_direction(self):
        """Kdsj"""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        """Kdsj"""
        x = (self.positions[0][0] + self.direction[0] * GRID_SIZE) \
            % SCREEN_WIDTH
        y = (self.positions[0][1] + self.direction[1] * GRID_SIZE) \
            % SCREEN_HEIGHT
        if (x, y) in self.positions[1:]:
            self.reset()
        else:
            self.positions.insert(0, (x, y))
            if len(self.positions) > self.length:
                self.positions.pop()

    def draw(self):
        """Kdsj"""
        for position in self.positions:
            rect = (pygame.Rect(position, (GRID_SIZE, GRID_SIZE)))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        # Отрисовка головы змейки
        head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

        # Затирание последнего сегмента
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def get_head_position(self):
        """Kdsj"""
        return self.positions[0]

    def reset(self):
        """Kdsj"""
        self.direction = choice([UP, DOWN, LEFT, RIGHT])
        self.length = 1
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.next_direction = None
        self.body_color = (0, 255, 0)


def handle_keys(game_object):
    """Kdsj"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main():
    """Kdsj"""
    # Инициализация PyGame:
    pygame.init()
    # Тут нужно создать экземпляры классов.
    snake = Snake()
    apple = Apple()

    while True:
        clock.tick(SPEED)
        screen.fill(BOARD_BACKGROUND_COLOR)
        handle_keys(snake)
        snake.update_direction()
        snake.move()
        apple.draw()
        snake.draw()
        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position()
        pygame.display.update()


if __name__ == '__main__':
    main()
