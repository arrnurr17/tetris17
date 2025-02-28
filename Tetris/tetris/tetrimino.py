import random
from .constants import SHAPES, COLUMNS, ROWS

class Tetrimino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = [random.randint(50, 255) for _ in range(3)]
        self.x = COLUMNS // 2 - len(self.shape[0]) // 2
        self.y = 0
        self.rotation = 0

    def rotate(self):
        """Rotate the tetrimino clockwise"""
        self.shape = [list(row) for row in zip(*self.shape[::-1])]
        self.rotation = (self.rotation + 1) % 4

    def get_ghost_position(self, grid):
        """Calculate the ghost piece position"""
        ghost_y = self.y
        while not self._check_collision(grid, (self.x, ghost_y + 1)):
            ghost_y += 1
        return ghost_y

    def _check_collision(self, grid, offset):
        """Check if the tetrimino collides with the grid or boundaries"""
        x_offset, y_offset = offset
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    if (x + x_offset < 0 or 
                        x + x_offset >= COLUMNS or 
                        y + y_offset >= ROWS or 
                        grid[y + y_offset][x + x_offset]):
                        return True
        return False

