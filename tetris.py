import pygame
from pygame.locals import *
from time import time

from tetris_piece import Piece
from tetris_background_grid import Background

class Pygame_Piece(Piece):
    BLOCK_SIZE = (34, 34)

    def __init__(self, pos_on_background=(0, 5)):
        super(Pygame_Piece, self).__init__()

        if self.color == "r":
            self._image = pygame.image.load('images/red_block.png')
        elif self.color == "b":
            self._image = pygame.image.load('images/blue_block.png')
        elif self.color == "g":
            self._image = pygame.image.load('images/green_block.png')
        elif self.color == "y":
            self._image = pygame.image.load('images/yellow_block.png')

        # Posicao da peça em relacao ao background
        self._pos_on_background = list(pos_on_background)

    @property
    def pos(self):
        return self._pos_on_background

    def draw(self, surface, surface_pos=(0, 0)):
        # Posicao da peça em relacao ao background
        pos_x = self._pos_on_background[1]
        pos_y = self._pos_on_background[0]
        # Tamanho dos blocos que formam as peças
        BLOCK_SIZE_x = self.BLOCK_SIZE[1]
        BLOCK_SIZE_y = self.BLOCK_SIZE[0]

        for i, line in enumerate(self._grid_maps[self._disposition]):
            for j, column in enumerate(line):
                draw_pos = ((j + pos_x)*BLOCK_SIZE_x + surface_pos[1],
                           (i + pos_y)*BLOCK_SIZE_y + surface_pos[0])
                # Desenha parte da peça se sua posição na matriz map_grid
                # corresponde a 1.
                if self.map_grid[i][j] == 1:
                    surface.blit(self._image, draw_pos)

    def move(self, direction):
        if direction == 'down':
            self._pos_on_background[0] += 1
        elif direction == 'left':
            self._pos_on_background[1] -= 1
        elif direction == 'right':
            self._pos_on_background[1] += 1

class Pygame_Background(Background):
    BLOCK_SIZE = (34, 34)

    def __init__(self):
        super(Pygame_Background, self).__init__()
        self._images = {
        'block': pygame.image.load('images/background.png'),
        'red': pygame.image.load('images/red_block.png'),
        'blue': pygame.image.load('images/blue_block.png'),
        'green': pygame.image.load('images/green_block.png'),
        'yellow': pygame.image.load('images/yellow_block.png')
        }

    # Desenha todo o background numa surface do pygame
    def draw(self, surface, surface_pos=(0, 0)):
        # Tamanho dos blocos que formam o background
        BLOCK_SIZE_x = self.BLOCK_SIZE[1]
        BLOCK_SIZE_y = self.BLOCK_SIZE[0]

        for i, line in enumerate(self._background_grid):
            for j, column in enumerate(line):
                draw_pos = (j*BLOCK_SIZE_x + surface_pos[1],
                            i*BLOCK_SIZE_y + surface_pos[0])

                if self._background_grid[i][j] == '':
                    surface.blit(self._images['block'], draw_pos)

                elif self._background_grid[i][j] == 'r':
                    surface.blit(self._images['red'], draw_pos)

                elif self._background_grid[i][j] == 'b':
                    surface.blit(self._images['blue'], draw_pos)

                elif self._background_grid[i][j] == 'g':
                    surface.blit(self._images['green'], draw_pos)

                elif self._background_grid[i][j] == 'y':
                    surface.blit(self._images['yellow'], draw_pos)

def draw(backackground_obj, piece_obj):
    pygame_background.draw(DISPLAYSURF, (10, 10))
    piece_obj.draw(DISPLAYSURF, (10, 10))

#- Pygame ----------------------------------------------------------------------
pygame.init()

FPS = 30 #frames per second setting
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((10 + 34*12 + 10, 10 + 34*18 + 10))
pygame.display.set_caption("TETRIS")

#draw on the surface object
DISPLAYSURF.fill((20, 20, 40))

pygame_background = Pygame_Background()
piece = Pygame_Piece()

# Game main loop
running = True

# Tempo para a peça do jogo cair
t_move_0 = time()
time_to_move = 0.5

while running:
    t_move_1 = time()

    if t_move_1 - t_move_0 > time_to_move:
        t_move_0 = t_move_1
        # Verifica se a peça pode se mover para baixo.
        # Caso possa, ela é movida. Se nao puder, ela é colocada no background,
        # o background sofre update, e outra peça é gerada.
        if pygame_background.there_is_way(piece.pos, piece, 'down'):
            piece.move('down')
        else:
            pygame_background.put_piece(piece.pos, piece)
            pygame_background.update()
            piece = Pygame_Piece()

    draw(pygame_background, piece)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_LEFT and \
              pygame_background.there_is_way(piece.pos, piece, 'left'):
                piece.move('left')

        if event.type == KEYDOWN:
            if event.key == K_RIGHT and \
              pygame_background.there_is_way(piece.pos, piece, 'right'):
                piece.move('right')

        if event.type == KEYDOWN:
            if event.key == K_DOWN and \
              pygame_background.there_is_way(piece.pos, piece, 'down'):
                piece.move('down')

        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                while pygame_background.there_is_way(piece.pos, piece, 'down'):
                    piece.move('down')
                t_move_0 = t_move_1
                pygame_background.put_piece(piece.pos, piece)
                pygame_background.update()
                piece = Pygame_Piece()


        if event.type == KEYDOWN:
            if event.key == K_SPACE and \
              pygame_background.there_is_way_to_rotate(piece.pos, piece):
                piece.rotate()

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()
