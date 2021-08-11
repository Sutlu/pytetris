   #55:00 war ich

import pygame
import random

colors = [
    (0, 0, 0),
    (0, 240, 240), #4 in einer Reihe
    (0, 0, 240), #Reverse L
    (240, 160, 0), #L
    (240, 240, 0), #Block
    (0, 240, 0), #S
    (160, 0, 240), #T
    (240, 0, 0) #Reverse S
]

class Figure:
    x = 0
    y = 0

    Figures = [
        [[1,5,9,13], [4,5,6,7]], #gerade
        [[1,2,5,9], [0,4,5,6], [1,5,9,8], [4,5,6,10]], #rev L
        [[1,2,6,10], [5,6,7,9], [2,6,10,11], [3,5,6,7]], #L
        [[1,2,5,6]], #block
        [[6,7,9,10], [1,5,6,10]], # S
        [[1,4,5,6], [1,4,5,9], [4,5,6,9], [1,5,6,9]], #T
        [[4,5,9,10], [2,6,5,9]] #rev S
    ]

    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
        self.type = random.randint(0, len(self.Figures) - 1)
        self.color = colors[self.type+1]
        self.rotation = 0

    def image(self):
        return self.Figures[self.type][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])
        

class Tetris:
    height = 0
    width = 0
    field = []
    score = 0
    state = 'start'
    Figure = None

    def __init__(self, _height, _width):
        self.height = _height
        self.width = _width
        self.field = []
        self.score = 0
        self.state = 'start'
        for i in range(_height):
            new_line = []
            for j in range(_width):
                new_line.append(0)
            self.field.append(new_line)
        self.new_figure()

    def new_figure(self):
        self.Figure = Figure(3, 0)

    def go_down(self):
        self.Figure.y += 1


pygame.init()
screen = pygame.display.set_mode((380,700))
pygame.display.set_caption("Tetris")

done = False
fps = 2
clock = pygame.time.Clock()
counter = 0
zoom = 30

game = Tetris(20, 10)
pressing_down = False
pressing_left = False
pressing_right = False

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

while not done:
    if game.state == 'start':
        game.go_down()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
            if event.key == pygame.K_DOWN:
                pressing_down = True
            if event.key == pygame.K_LEFT:
                pressing_left = True
            if event.key == pygame.K_RIGHT:
                pressing_right = True

        if pressing_down:
            game.down()
        if pressing_left:
            game.left()
        if pressing_right:
            game.right()
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                game.down()
                pressing_down = False
            if event.key == pygame.K_LEFT:
                game.left()
                pressing_left = False
            if event.key == pygame.K_RIGHT:
                game.right()
                pressing_right = False

    screen.fill(color = WHITE)
    for i in range(game.height):
        for j in range(game.width):
            if game.field [i][j] == 0:
                color = GRAY
                just_border = 1
            else:
                color = colors[game.field[i][j]]
                just_border = 0
            pygame.draw.rect(screen, color, [35 + j*zoom, 35 + i*zoom, zoom, zoom,], just_border)

    if game.Figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.Figure.image():
                    pygame.draw.rect(screen, game.Figure.color, [35 + (j+game.Figure.x)*zoom, 35 + (i+game.Figure.y)*zoom, zoom, zoom,])

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()