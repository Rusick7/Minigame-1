import pygame
import os.path
pygame.init()

FPS = 60
clock = pygame.time.Clock()
cellSize = 20
world = []
worldWidth, worldHeight = 30, 30
WIDTH, HEIGHT = worldWidth * cellSize, worldHeight * cellSize
window = pygame.display.set_mode((WIDTH, HEIGHT))
info = pygame.display.Info()
pygame.mouse.set_visible(False)


def drawCursor(x, y):
    pygame.draw.circle(window, (225, 225, 225), (x, y), 10, 1)
    pygame.draw.rect(window, (225, 0, 0), (x-2, y-2, 4, 4), 4, 2)


for row in range(worldHeight):
    line = []
    for col in range(worldWidth):
        line.append(0)
    world.append(line)
play = True
while play:

    pos = pygame.mouse.get_pos()
    mousePX, mousePY = pygame.mouse.get_pos()
    mouseRow, mouseCol = mousePY // cellSize, mousePX // cellSize
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE) or world[mouseRow][mouseCol] == 1:
            play = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_l and os.path.exists("Map.py"):
            import Map
            file = Map.data
            worldWidth, worldHeight = Map.wW, Map.wH
            row, col = 0, 0
            for line in file:
                for s in line:
                    world[row][col] = int(s)
                    col += 1
                    if col == worldWidth:
                        row += 1
                        col = 0

    window.fill(pygame.Color('black'))
    for row in range(worldHeight):
        for col in range(worldWidth):
            x, y = col * cellSize, row * cellSize
            if world[row][col] == 1:
                pygame.draw.rect(window, pygame.Color('gray'), (x, y, cellSize, cellSize))
            else:
                pygame.draw.rect(window, pygame.Color('black'), (x, y, cellSize, cellSize), 1)
    drawCursor(pos[0], pos[1])
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
