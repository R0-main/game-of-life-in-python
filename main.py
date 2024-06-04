import math
import numpy as np

taille_grille_x = 20
taille_grille_y = 20

def print_state(grid) :
    for x in range(0, taille_grille_x) :
        for y in range(0, taille_grille_y) :
            if(grid[x][y] == 1) :
                print('■', end=' ')
            else :
                print('□', end=' ')
        print('')

def ajouter_stable(grille):
    
    patern = [
        [1],
        [1],
        [1],
    ]

    for x in range(0, len(patern)) :
        for y in range(0, len(patern[x])) :
           grille[math.floor(taille_grille_x / 2) + x][math.floor(taille_grille_y / 2) + y] = patern[x][y]

def get_neighbord_count(grid, targetX, targetY):
    count = 0
    for x in range(-1, 2) :
        for y in range(-1, 2) :
            if (targetX + x >= taille_grille_x or targetY + y >= taille_grille_y):
                continue

            if (targetX + x < 0 or targetY + y < 0):
                continue

            if (x == 0 and y == 0) :
                continue

            if (grid[targetX + x][targetY + y] == 1) :
                count += 1

    return count

def calculate_next_state(grid, next_grid):
    for x in range(0, taille_grille_x) :
        for y in range(0, taille_grille_y) :
            neightbord_count = get_neighbord_count(grid, x, y) 
            if (grid[x][y] == 1) :
                if (neightbord_count < 2 or neightbord_count > 3) :
                     next_grid[x][y] = 0
                else :
                    next_grid[x][y] = 1
            else :
                if (neightbord_count == 3):
                    next_grid[x][y] = 1
                else:
                    next_grid[x][y] = 0

def loop() :
    tours = 10
    i = 0
    grille = np.zeros((taille_grille_x, taille_grille_y), dtype=int)
    next_grille = np.zeros((taille_grille_x, taille_grille_y), dtype=int)
    ajouter_stable(grille)

    while(i < tours) :
        print_state(grille)
        calculate_next_state(grille, next_grille)
        grille = np.copy(next_grille)
        print('')
        i += 1

loop()

