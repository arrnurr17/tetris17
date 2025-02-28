import pygame

# Window dimensions
WIDTH = 800
HEIGHT = 600
GRID_SIZE = 30
PLAY_WIDTH = 300
PLAY_HEIGHT = 600
COLUMNS = PLAY_WIDTH // GRID_SIZE
ROWS = PLAY_HEIGHT // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Game settings
FPS = 60
INITIAL_SPEED = 500
DROP_SPEED = 50
LEVEL_SPEEDUP = 50
LINES_PER_LEVEL = 10

# Tetrimino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]]  # J
]

# Key bindings
CONTROLS = {
    'LEFT': pygame.K_LEFT,
    'RIGHT': pygame.K_RIGHT,
    'DOWN': pygame.K_DOWN,
    'ROTATE': pygame.K_UP,
    'HARD_DROP': pygame.K_SPACE,
    'PAUSE': pygame.K_p,
    'RESTART': pygame.K_r
}

