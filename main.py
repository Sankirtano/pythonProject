import random


class Cell:
    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = True


class GamePole:
    def __init__(self, n, m):
        self._n = n
        self._m = m
        self.pole = [[Cell() for n in range(self._n)] for n in range(self._n)]
        self.init()

    def init(self):
        m = 0
        while self._m > m:
            i = random.randint(0, self._n - 1)
            j = random.randint(0, self._n - 1)
            if self.pole[i][j].mine:
                continue
            else:
                self.pole[i][j].mine = True
                m += 1
        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self._n):
            for y in range(self._n):
                if not self.pole[x][y].mine:
                    self.pole[x][y].around_mines = sum((self.pole[x+i][y+j].mine for i, j in indx if 0 <= x+i < self._n and 0 <= y+j < self._n))

    def show(self):
        for row in self.pole:
            print(*map(lambda x: '#' if not x.fl_open else x.around_mines if not x.mine else '*', row))


pole_game = GamePole(10, 12)
pole_game.show()