import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width  # клетки по вертикали
        self.height = height    # клетки по горизонтали
        self.board = [[1] * width for _ in range(height)]
        self.color = [[5] * width for _ in range(height)]

        self.left = 30  # отступ слева
        self.top = 30   # отступ справа
        self.cell_size = 30 # длина клетки

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        # изменение параметров по улочанию
        self.left = left
        self.top = top
        self.cell_size = cell_size

    # прорисовка клеток поля
    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                c = self.board[j][i]
                if self.color[j][i] == 5:
                    pygame.draw.rect(screen, (0, 0, 0), (self.left + i * self.cell_size,
                                        self.top + j * self.cell_size, self.cell_size, self.cell_size))
                elif self.color[j][i] == 4:
                    pygame.draw.rect(screen, (255, 0, 0), (self.left + i * self.cell_size,
                                        self.top + j * self.cell_size, self.cell_size, self.cell_size))
                elif self.color[j][i] == 3:
                    pygame.draw.rect(screen, (0, 0, 255), (self.left + i * self.cell_size,
                                                self.top + j * self.cell_size, self.cell_size, self.cell_size))
                pygame.draw.rect(screen, (255, 255, 255), (self.left + i * self.cell_size,
                                                       self.top + j * self.cell_size, self.cell_size, self.cell_size), 1)


    # возвращает координаты клетки в виде кортежа по переданным координатам мыши
    def get_cell(self, mouse):
        if self.left <= mouse[0] <= self.left + self.cell_size * len(self.board[0]) \
                and self.top <= mouse[1] <= self.top + self.cell_size * len(self.board):
            c = self.cell_size
            return (mouse[0] - self.left) // c, (mouse[1] - self.top) // c
        else:
            return None

    def get_click(self, mouse):
        cell = self.get_cell(mouse)
        if cell is not None:
            self.on_click(cell)

    # изменяет поле, опираясь на полученные координаты клетки
    def on_click(self, xy):
        x, y = xy[1], xy[0]   # кортедж с координатами
        if self.color[x][y] == 5:
            self.color[x][y] = 4
        elif self.color[x][y] == 4:
            self.color[x][y] = 3
        else:
            self.color[x][y] = 5



board = Board(5, 7)
board.set_view(30, 30, 30)
size = 300, 300

screen = pygame.display.set_mode(size)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            board.get_click(event.pos)
    screen.fill((0, 0, 0))
    board.render()
    pygame.display.flip()