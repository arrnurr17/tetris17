import pygame
from .constants import *
from .tetrimino import Tetrimino
from .ui import UI

class TetrisOiyyny:
    def __init__(self):
        pygame.init()
        
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Тетрис")
        self.clock = pygame.time.Clock()
        self.ui = UI()
        
        self.oiyndy_qayta_bastyru()

    def oiyndy_qayta_bastyru(self):
        """Ойынды қайта бастау"""
        self.grid = [[0] * COLUMNS for _ in range(ROWS)]
        self.current_piece = Tetrimino()
        self.next_piece = Tetrimino()
        self.game_over = False
        self.paused = False
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.speed = INITIAL_SPEED
        self.counter = 0

    def engizudi_basqaru(self):
        """Пайдаланушының енгізуін басқару"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == CONTROLS['PAUSE']:
                    self.paused = not self.paused
                elif event.key == CONTROLS['RESTART']:
                    self.oiyndy_qayta_bastyru()
                elif not self.paused and not self.game_over:
                    self._oiyndy_basqaru(event)
            
            elif event.type == pygame.KEYUP:
                if event.key == CONTROLS['DOWN']:
                    self.speed = INITIAL_SPEED - (self.level - 1) * LEVEL_SPEEDUP

        return True

    def jańartu(self):
        """Ойын күйін жаңарту"""
        if self.paused or self.game_over:
            return

        self.counter += self.clock.get_time()
        if self.counter > self.speed:
            self._figura_oralystyru()
            self.counter = 0

    def salu(self):
        """Ойын күйін көрсету"""
        self.screen.fill(GRAY)
        
        ghost_y = self.current_piece.get_ghost_position(self.grid)
        self.ui.oyyn_tor_salu(self.screen, self.grid, self.current_piece, ghost_y)
        
        self.ui.kelesi_figura_salu(self.screen, self.next_piece)
        self.ui.statistika_korsetu(self.screen, self.score, self.level, self.lines_cleared)
        
        if self.game_over:
            self.ui.oyyn_ayaqtaldy(self.screen, self.score)
        elif self.paused:
            self.ui.uaqytsha_toqtatu(self.screen)
        
        pygame.display.flip()

    def _oiyndy_basqaru(self, event):
        """Ойындағы басқару"""
        if event.key == CONTROLS['LEFT']:
            if not self._soqtygysudy_tekseru((self.current_piece.x - 1, self.current_piece.y)):
                self.current_piece.x -= 1
        elif event.key == CONTROLS['RIGHT']:
            if not self._soqtygysudy_tekseru((self.current_piece.x + 1, self.current_piece.y)):
                self.current_piece.x += 1
        elif event.key == CONTROLS['DOWN']:
            self.speed = DROP_SPEED
        elif event.key == CONTROLS['ROTATE']:
            self._aılandyru()
        elif event.key == CONTROLS['HARD_DROP']:
            self._tez_tusiru()

    def _figura_oralystyru(self):
        """Фигураның орнын өзгерту"""
        if not self._soqtygysudy_tekseru((self.current_piece.x, self.current_piece.y + 1)):
            self.current_piece.y += 1
        else:
            self._biriktiru()
            self._qatarlardy_alu()
            self._jańa_figura()

    def _soqtygysudy_tekseru(self, offset):
        """Фигура соқтығысқанын тексеру"""
        return self.current_piece._soqtygysudy_tekseru(self.grid, offset)

    def _aılandyru(self):
        """Фигураны айналдыру"""
        old_shape = self.current_piece.shape[:]
        self.current_piece.rotate()
        if self._soqtygysudy_tekseru((self.current_piece.x, self.current_piece.y)):
            self.current_piece.shape = old_shape

    def _tez_tusiru(self):
        """Фигураны тез түсіру"""
        while not self._soqtygysudy_tekseru((self.current_piece.x, self.current_piece.y + 1)):
            self.current_piece.y += 1
            self.score += 2
        self._figura_oralystyru()

    def _jańa_figura(self):
        """Жаңа фигура пайда болу"""
        self.current_piece = self.next_piece
        self.next_piece = Tetrimino()
        
        if self._soqtygysudy_tekseru((self.current_piece.x, self.current_piece.y)):
            self.game_over = True