from random import randint, choice
import numpy as np

class Piece:

    def __init__(self,):
        self._layout = choice('oizsljt')
        self._color = choice(('r', 'b', 'g', 'y'))

        if self._layout == 'o':
            self._grid_maps = np.array(
            [
            [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
            ]
            ]
            )

        elif self._layout == 'i':
            self._grid_maps = np.array(
            [
            [
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0]
            ],

            [
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
            ]
            ]
            )

        elif self._layout == 'z':
            self._grid_maps = np.array(
            [
            [
            [1, 1, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
            ],

            [
            [0, 1, 0, 0],
            [1, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 0]
            ]
            ]
            )

        elif self._layout == 's':
            self._grid_maps = np.array(
            [
            [
            [0, 1, 1, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
            ],

            [
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0]
            ]
            ]
            )

        elif self._layout == 'l':
            self._grid_maps = np.array(
            [
            [
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0]
            ],

            [
            [1, 1, 1, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
            ],

            [
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0]
            ],

            [
            [0, 0, 1, 0],
            [1, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
            ]
            ]
            )

        elif self._layout == 'j':
            self._grid_maps = np.array(
            [
            [
            [1, 1, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 0]
            ],

            [
            [1, 0, 0, 0],
            [1, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
            ],

            [
            [0, 1, 0, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 0, 0]
            ],

            [
            [1, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
            ]
            ]
            )

        elif self._layout == 't':
            self._grid_maps = np.array(
            [
            [
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
            ],

            [
            [1, 0, 0, 0],
            [1, 1, 0, 0],
            [1, 0, 0, 0],
            [0, 0, 0, 0]
            ],

            [
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
            ],

            [
            [0, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0]
            ]
            ]
            )

        self._disposition = randint(0, len(self._grid_maps) - 1)

    # Roda a peça na direcao posotiva (por padrao), ou negativa
    def rotate(self, direction='positive'):
        if direction == 'negative':
            if self._disposition == len(self._grid_maps) - 1:
                self._disposition = 0
            else:
                self._disposition += 1
        elif direction == 'positive':
            if self._disposition == 0:
                self._disposition = len(self._grid_maps) - 1
            else:
                self._disposition -= 1

    @property
    def map_grid(self):
        return self._grid_maps[self._disposition]

    @property
    def color(self):
        return self._color

    def __repr__(self):
        msg = self._layout + '\n' + str(self.map_grid)
        return msg

    def __str__(self):
        msg = str(self.map_grid)
        return msg
