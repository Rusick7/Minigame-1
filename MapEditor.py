import pygame
import os.path
import numpy as np
from PIL import Image
pygame.init()


FPS = 60
clock = pygame.time.Clock()
cellSize = 20
world = []
worldWidth, worldHeight = 30, 30
WIDTH, HEIGHT = worldWidth * cellSize, worldHeight * cellSize
window = pygame.display.set_mode((WIDTH, HEIGHT))


def Formate(RowCol, width, height, file,  SymWidth):
    file.write(f"wW, wH = {width}, {height}\ndata = [\n  ")
    for row in range(width):
        for col in range(height):
            if RowCol == "World":
                file.write(f"'{world[row][col]}', ")
                SymWidth += 1
                if SymWidth >= worldWidth:
                    file.write("\n  ")
                    SymWidth = 0
            elif RowCol == "Img":
                file.write(f"'{np_img[row][col]}', ")
                SymWidth += 1
                if SymWidth >= worldWidth:
                    file.write("\n  ")
                    SymWidth = 0
    file.write("]\n")
    print("Successful")
    file.close()


for row in range(worldHeight):
    line = []
    for col in range(worldWidth):
        line.append(0)
    world.append(line)
play = True
while play:

    b1, b2, b3 = pygame.mouse.get_pressed()
    mousePX, mousePY = pygame.mouse.get_pos()
    mouseRow, mouseCol = mousePY // cellSize, mousePX // cellSize
    if b1 and 0 <= mouseRow < worldHeight and 0 <= mouseCol < worldWidth:
        world[mouseRow][mouseCol] = 1
    elif b3 and 0 <= mouseRow < worldHeight and 0 <= mouseCol < worldWidth:
        world[mouseRow][mouseCol] = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            play = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            Formate("World", worldWidth, worldHeight, open('Map.py', 'w'), 0)
            play = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_f and os.path.exists("Map.png"):
            img = Image.open('Map.png').convert('L')
            np_img = np.array(img)
            np_img = ~np_img
            np_img[np_img > 0] = 1
            Formate("Img", worldWidth, worldHeight, open('Map.py', 'w'), 0)
            play = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_l and os.path.exists("Map.py"):
            import Map
            file = Map.data
            worldWidth, worldHeight = Map.wW, Map.wH
            row, col = 0, 0
            for line in file:
                for elm in line:
                    world[row][col] = int(elm)
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
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
