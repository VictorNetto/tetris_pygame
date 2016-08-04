
class Background:

    def __init__(self, size=(18, 12)):
        self._size = size

        lines, columns = size
        self._background_grid = []
        for line in range(lines):
            self._background_grid.append(['']*columns)

    def __repr__(self):
        msg = ''
        for count, line in enumerate(self._background_grid):
            msg += '\n{:2} - '.format(count+1) + str(line)
        return msg


    # Dada uma posicao no Background, e uma peça, coloca ela no background_grid
    def put_piece(self, pos, piece):
        line, column = pos[0], pos[1]

        G = ((a, b) for a in range(4)
                    for b in range(4))
        for i, j in G:
             if piece.map_grid[i][j] == 1:
                self._background_grid[i+line][j+column] = piece.color


    # Dada uma posicao no Background, e uma peça, verifica se aquela peça
    # pode se mober para baixo ou para os lados.
    # Basicante executa a acao, e verifica se a peça se choca com alguma posi-
    # ção do _background_grid.
    def there_is_way(self, pos, piece, direction='down'):
        # linha e coluna do _background_grid a serem avaliadas
        if direction == 'down':
            line, column = pos[0]+1, pos[1]
        elif direction == 'left':
            line, column = pos[0], pos[1]-1
        elif direction == 'right':
            line, column = pos[0], pos[1]+1

        # Verifica se ha alguma colisao. Nesse caso, retorna False
        # O try da conta dos casos ondem a peça sai fora do Background

        # Peça fora do background pela esquerda
        # essa confição a parte é necessária, porque valores negativos de
        # indices tem um significados no python.
        if column < 0:
            return False

        G = ((a, b) for a in range(4)
                    for b in range(4))
        for i, j in G:
            try:
                if piece.map_grid[i][j] == 1 and \
                   self._background_grid[i+line][j+column] != '':
                    return False
            except IndexError:
                return False
        # Se nao houver nenhum impedimento, returno True
        return True

    # Dada uma posicao no Background, e uma peça, verifica se aquela peça
    # pode executar o metodo rotate.
    # Basicante executa a acao, e verifica se a peça se choca com alguma posi-
    # ção do _background_grid
    def there_is_way_to_rotate(self, pos, piece):
        # Roda a peça para poder avaliar se existe algum choque
        piece.rotate('positive')

        # linha e coluna do _background_grid a serem avaliadas
        line, column = pos[0], pos[1]

        # Verifica se ha alguma colisao. Nesse caso, retorna False, mas antes
        # usa o metodo piece.rotate('negative') para fazer com que a peça volte
        # para sua posicao original.
        # O try da conta dos casos ondem a peça sai fora do Background
        G = ((a, b) for a in range(4)
                    for b in range(4))
        for i, j in G:
            try:
                if piece.map_grid[i][j] == 1 and \
                   self._background_grid[i+line][j+column] != '':
                    piece.rotate('negative')
                    return False
            except IndexError:
                piece.rotate('negative')
                return False
        # Se nao houver nenhum impedimento, returno True
        piece.rotate('negative')
        return True

    # Limpa as linhas que estão completas
    def update(self):
        columns = self._size[1]
        clean_line_list = ['']*columns

        # É mais natural trabalhar com self._background_grid[::-1], pois podemos
        # com ela podemos usar os metodos append e remove para limpar as linhas
        # que estao cheias. Veja:
        # >>> lista = [1, 2, 0, 0, 3, 0, 4, 0, 0, 0, 0]
        # >>> lista.remove(0); lista.append(0); print(lista)
        # [1, 2, 0, 3, 0, 4, 0, 0, 0, 0, 0]
        # >>> lista.remove(0); lista.append(0); print(lista)
        # [1, 2, 3, 0, 4, 0, 0, 0, 0, 0, 0]
        # >>> lista.remove(0); lista.append(0); print(lista)
        # [1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0]
        reversed_grid = self._background_grid[::-1]

        # A variavel lines_to_down guarda o numero de linhas que estavam comple-
        # tas, que foram limpas. Assim eh possivel saber o numero de vezes que
        # que precisamos aplicar os metodos remove e append para tirar todas li-
        # nhas vazias do reversed_grid.
        lines_to_down = 0

        # Determina linhas que precisa ser limpas, e ja as altera para uma linha
        # limpa.
        for i, line in enumerate(reversed_grid):
            erase_Line = True
            for column in line:
                if column == '':
                    erase_Line = False
            if erase_Line:
                reversed_grid[i] = clean_line_list
                lines_to_down += 1

        # Aplica os metodos remove e append a quantidade de vezes necessaria pa-
        # ra retirar a linhas limpas do meio do reversed_grid
        for i in range(lines_to_down):
            reversed_grid.remove(clean_line_list)
            reversed_grid.append(clean_line_list)

        # Atualiza o background
        self._background_grid = reversed_grid[::-1]
