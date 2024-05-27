import math

taille_grille_x = 20
taille_grille_y = 20

def ajouter_stable(grille):
    
    stable = [
        [1, 1, 1, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
    ]

    osi = [
       [1, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
    ]

    for x in range(0, len(osi)) :
        for y in range(0, len(osi[0])) :
           grille[math.floor(taille_grille_x / 2)+ x][math.floor(taille_grille_y / 2) + y] = osi[x][y]

def print_state(grid) :
    for x in range(0, taille_grille_x) :
        for y in range(0, taille_grille_y) :
            if(grid[x][y] == 1) :
                print('■', end=' ')
            else :
                print('□', end=' ')
        print('')

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
                cell = grid[x][y]
                isAlive = cell == 1
                neightbord_count = get_neighbord_count(grid, x, y) 
                if (isAlive) :
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
    grille = [[0 for y in range(taille_grille_y)] for x in range(taille_grille_x)]
    next_grille = [[0 for y in range(taille_grille_y)] for x in range(taille_grille_x)]
    ajouter_stable(grille)

    while(i < tours) :
        print_state(grille)
        calculate_next_state(grille, next_grille)
        grille = [row[:] for row in next_grille]
        print('')
        i += 1

loop()

