"""

--- Day 6: Guard Gallivant ---

The Historians use their fancy device again, this time to whisk you all away to the North Pole prototype suit manufacturing lab... in the year 1518! It turns out that having direct access to history is very convenient for a group of historians.

You still have to be careful of time paradoxes, and so it will be important to avoid anyone from 1518 while The Historians search for the Chief. Unfortunately, a single guard is patrolling this part of the lab.

Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?

You start by making a map (your puzzle input) of the situation. For example:

....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...

The map shows the current position of the guard with ^ (to indicate the guard is currently facing up from the perspective of the map). Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:

    If there is something directly in front of you, turn right 90 degrees.
    Otherwise, take a step forward.

Following the above protocol, the guard moves up several times until she reaches an obstacle (in this case, a pile of failed suit prototypes):

....#.....
....^....#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...

Because there is now an obstacle in front of the guard, she turns right before continuing straight in her new facing direction:

....#.....
........>#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...

Reaching another obstacle (a spool of several very long polymers), she turns right again and continues downward:

....#.....
.........#
..........
..#.......
.......#..
..........
.#......v.
........#.
#.........
......#...

This process continues for a while, but the guard eventually leaves the mapped area (after walking past a tank of universal solvent):

....#.....
.........#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#v..

By predicting the guard's route, you can determine which specific positions in the lab will be in the patrol path. Including the guard's starting position, the positions visited by the guard before leaving the area are marked with an X:

....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X..

In this example, the guard will visit 41 distinct positions on your map.

Predict the path of the guard. How many distinct positions will the guard visit before leaving the mapped area?



"""

def find_guard(carte:list):
    # return guard as a list containing x, y coordiantes and direction
    for y in range(len(carte)):
        for x in range(len(carte[y])):
            if carte[y][x] == 'v':
                return [int(x),int(y), 'v']
            elif carte[y][x] == '^':
                return [int(x),int(y), '^']
            elif carte[y][x] == '<':
                return [int(x),int(y), '<']
            elif carte[y][x] == '>':
                return [int(x),int(y), '>']

def new_position(x, y, direction):
    i = 0
    j = 0
    if direction == '>': # les x grandissent vers la droite
        i = 1
    elif direction == '<':
        i = -1
    elif direction == 'v': # les y grandissent en descendant
        j = 1
    elif direction == '^':
        j = -1
    else:
        print('Cas non traité dans la fonction "new position"')
    return x+i, y+j

def turn(direction):
    # renvoie la nouvelle direction quand on tourne
    if direction == '>':
        return 'v'
    elif direction == '<':
        return '^'
    elif direction == 'v':
        return '<'
    elif direction == '^':
        return '>'
    else:
        print('Cas non traité dans la fonction "turn"')

def check_border(guard:list, carte:list):
    x = guard[0]
    y = guard[1]
    xmax = len(carte[0]) - 1
    ymax = len(carte) - 1
    if x == 0 or y == 0 or x == xmax or y == ymax:
        carte[y][x] = 'X'
        guard[2] = 'away'

def move(guard:list, carte:list):
    # Pas de return dans cette fonction qui va modifier les input eux-même (car ce sont des listes)
    x = guard[0]
    y = guard[1]
    direction = guard[2]
    new_x, new_y = new_position(x, y, direction)
    symbol_ahead = carte[new_y][new_x]
    if symbol_ahead == "." or symbol_ahead == "X":
        carte[y][x] = "X"
        guard[0] = new_x
        guard[1] = new_y
        
    elif symbol_ahead == "#":
        guard[2] = turn(direction)
    
    else:
        print('Cas non traité dans la fonction "move"')

def afficher(carte):
    for line in carte:
        print(str(line))

def resolve_problem(data_file):
    data = open(data_file, 'r')
    
    #lines est une liste de str
    lines = data.read().splitlines()
    
    # carte est une liste de listes
    carte = []
    for line in lines:
        carte.append(list(line))
    
    # garde est une liste contenant la positions x les y du garde (sous forme d'entiers) en indice 0 et 1
    # et sa direction sous forme d'une string ayant la valeur 'v', '^', '<' ou '>' en indice 2
    guard = find_guard(carte)
    
    while guard[2] != 'away':
        move(guard, carte)
        
        check_border(guard, carte)
    
    count = 0
    
    for line in carte:
        for symbol in line:
            if symbol == "X":
                count += 1
    
    return count


print(resolve_problem('day_06_my_input'))



