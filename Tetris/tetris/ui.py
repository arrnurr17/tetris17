import pygame
from .constants import *

class UI:
    def __init__(self):
        pygame.font.init()
        self.font_big = pygame.font.Font(None, 48)
        self.font_medium = pygame.font.Font(None, 36)
        self.font_small = pygame.font.Font(None, 24)

    def draw_grid(self, surface, grid, current_piece=None, ghost_y=None):
        """Draw the game grid and current piece"""
        # Draw background
        pygame.draw.rect(surface, BLACK, (0, 0, PLAY_WIDTH, PLAY_HEIGHT))
        
        # Draw grid cells
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(surface, cell, 
                                   (x * GRID_SIZE, y * GRID_SIZE, 
                                    GRID_SIZE - 1, GRID_SIZE - 1))

        # Draw ghost piece
        if current_piece and ghost_y is not None:
            ghost_color = (*current_piece.color, 128)  # Semi-transparent
            self._draw_piece(surface, current_piece.shape, 
                           current_piece.x, ghost_y, ghost_color)

        # Draw current piece
        if current_piece:
            self._draw_piece(surface, current_piece.shape, 
                           current_piece.x, current_piece.y, 
                           current_piece.color)

    def draw_next_piece(self, surface, next_piece):
        """Draw the next piece preview"""
        preview_x = PLAY_WIDTH + 50
        preview_y = 100
        
        text = self.font_medium.render("Next:", True, WHITE)
        surface.blit(text, (preview_x, preview_y - 30))
        
        pygame.draw.rect(surface, BLACK, 
                        (preview_x, preview_y, 
                         GRID_SIZE * 4, GRID_SIZE * 4))
        
        self._draw_piece(surface, next_piece.shape,
                        preview_x // GRID_SIZE, 
                        preview_y // GRID_SIZE + 1,
                        next_piece.color)

    def draw_stats(self, surface, score, level, lines):
        """Draw game statistics"""
        stats_x = PLAY_WIDTH + 50
        stats_y = 250
        
        texts = [
            ("Score", str(score)),
            ("Level", str(level)),
            ("Lines", str(lines))
        ]
        
        for i, (label, value) in enumerate(texts):
            label_surf = self.font_small.render(label + ":", True, WHITE)
            value_surf = self.font_medium.render(value, True, WHITE)
            surface.blit(label_surf, (stats_x, stats_y + i * 60))
            surface.blit(value_surf, (stats_x, stats_y + i * 60 + 25))

    def draw_game_over(self, surface, final_score):
        """Draw game over screen"""
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.fill(BLACK)
        overlay.set_alpha(128)
        surface.blit(overlay, (0, 0))
        
        game_over = self.font_big.render("GAME OVER", True, RED)
        score = self.font_medium.render(f"Final Score: {final_score}", True, WHITE)
        restart = self.font_small.render("Press R to restart", True, WHITE)
        
        surface.blit(game_over, 
                    (WIDTH // 2 - game_over.get_width() // 2, 
                     HEIGHT // 2 - 60))
        surface.blit(score, 
                    (WIDTH // 2 - score.get_width() // 2, 
                     HEIGHT // 2))
        surface.blit(restart, 
                    (WIDTH // 2 - restart.get_width() // 2, 
                     HEIGHT // 2 + 40))

    def draw_pause(self, surface):
        """Draw pause screen"""
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.fill(BLACK)
        overlay.set_alpha(128)
        surface.blit(overlay, (0, 0))
        
        pause_text = self.font_big.render("PAUSED", True, WHITE)
        surface.blit(pause_text, 
                    (WIDTH // 2 - pause_text.get_width() // 2, 
                     HEIGHT // 2))

    def _draw_piece(self, surface, shape, x, y, color):
        """Helper method to draw a tetrimino"""
        for row_idx, row in enumerate(shape):
            for col_idx, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(surface, color,
                                   ((x + col_idx) * GRID_SIZE,
                                    (y + row_idx) * GRID_SIZE,
                                    GRID_SIZE - 1, GRID_SIZE - 1))

