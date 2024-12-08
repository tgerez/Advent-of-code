"""

--- Part Two ---

While The Historians begin working around the guard's patrol route, you borrow their fancy device and step outside the lab. From the safety of a supply closet, you time travel through the last few months and record the nightly status of the lab's guard post on the walls of the closet.

Returning after what seems like only a few seconds to The Historians, they explain that the guard's patrol area is simply too large for them to safely search the lab without getting caught.

Fortunately, they are pretty sure that adding a single new obstruction won't cause a time paradox. They'd like to place the new obstruction in such a way that the guard will get stuck in a loop, making the rest of the lab safe to search.

To have the lowest chance of creating a time paradox, The Historians would like to know all of the possible positions for such an obstruction. The new obstruction can't be placed at the guard's starting position - the guard is there right now and would notice.

In the above example, there are only 6 different positions where a new obstruction would cause the guard to get stuck in a loop. The diagrams of these six situations use O to mark the new obstruction, | to show a position where the guard moves up/down, - to show a position where the guard moves left/right, and + to show a position where the guard moves both up/down and left/right.

Option one, put a printing press next to the guard's starting position:

....#.....
....+---+#
....|...|.
..#.|...|.
....|..#|.
....|...|.
.#.O^---+.
........#.
#.........
......#...

Option two, put a stack of failed suit prototypes in the bottom right quadrant of the mapped area:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
......O.#.
#.........
......#...

Option three, put a crate of chimney-squeeze prototype fabric next to the standing desk in the bottom right quadrant:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----+O#.
#+----+...
......#...

Option four, put an alchemical retroencabulator near the bottom left corner:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
..|...|.#.
#O+---+...
......#...

Option five, put the alchemical retroencabulator a bit to the right instead:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
....|.|.#.
#..O+-+...
......#...

Option six, put a tank of sovereign glue right next to the tank of universal solvent:

....#.....
....+---+#
....|...|.
..#.|...|.
..+-+-+#|.
..|.|.|.|.
.#+-^-+-+.
.+----++#.
#+----++..
......#O..

It doesn't really matter what you choose to use as an obstacle so long as you and The Historians can put it into position without the guard noticing. The important thing is having enough options that you can find one that minimizes time paradoxes, and in this example, there are 6 different positions you could choose.

You need to get the guard stuck in a loop by adding a single new obstruction. How many different positions could you choose for this obstruction?


"""

# Le garde est dans une boucle dès qu'il parcourt deux cases adjascentes qu'il a déjà visité dans ce sens
# je vais donc remplacer les X sur son passage par des - ou des | ou des +
# et vérifier que deux cases adjacentes en cours de parcourt ont ces symboles
# Je pourrais aussi laisser les "." sur son passage mais stocker le chemin parcouru et vérifier que deux cases adjacentes
# en cours de parcourt ont déjà été parcourues ou non

from copy import *

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

def move(guard:list, carte:list, turned:list):
    # Pas de return dans cette fonction qui va modifier les input eux-même (car ce sont des listes, même turned avec 1 élément)
    x = guard[0]
    y = guard[1]
    direction = guard[2]
    new_x, new_y = new_position(x, y, direction)
    symbol_ahead = carte[new_y][new_x]
    if symbol_ahead != "#" and symbol_ahead != "O":
        guard[0] = new_x
        guard[1] = new_y
        if direction == '>' or direction == '<':
            carte[y][x] = "-"
        elif direction == '^' or direction == 'v':
            carte[y][x] = "|"
        
    elif symbol_ahead == "#" or symbol_ahead == "O":
        guard[2] = turn(direction)
        carte[y][x] = "+"
        turned[0] = True
    
    else:
        print('Cas non traité dans la fonction "move"')

def afficher(carte):
    for line in carte:
        print("".join(line))
    print()

def check_loop(history_of_positions:list):
    hp = history_of_positions
    loop = False
    for i, coord in enumerate(hp[:len(hp)-2]):
        if coord[0] == hp[-2][0] and coord[1] == hp[-2][1]:
            if hp[i+1][0] == hp[-1][0] and hp[i+1][1] == hp[-1][1]:
                loop = True
                print('boucle !')
    return loop

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
    
    guard_initial_x = guard[0]
    guard_initial_y = guard[1]
    guard_initial_position = guard[2]
    carte_initiale = deepcopy(carte)
    
    # A list of x, y coordinates where the gard initialy follow (initial position excluded). So where the additionnal obstacle can be placed
    initial_pathway = []
    
    while guard[2] != 'away':
        turned = [False]
        move(guard, carte, turned)
        if not turned[0]:
            initial_pathway.append([guard[0],guard[1]])
        check_border(guard, carte)
    
    positions_of_all_obstacles = []
    for pos in initial_pathway:
        if pos not in positions_of_all_obstacles:
            positions_of_all_obstacles.append(pos)
    
    number_of_new_obstacle_possible_positions = 0
    
    for x, y in positions_of_all_obstacles:
        new_carte = deepcopy(carte_initiale)
        new_carte[y][x] = 'O'
        #afficher(new_carte)
        guard[0] = guard_initial_x
        guard[1] = guard_initial_y
        guard[2] = guard_initial_position
        history_of_positions = []
        while guard[2] != 'away':
            turned = [False]
            move(guard, new_carte, turned)
            if not turned[0]:
                history_of_positions.append([guard[0],guard[1]])
            check_border(guard, new_carte)
            if len(history_of_positions) >= 6:
                if check_loop(history_of_positions):
                    number_of_new_obstacle_possible_positions += 1
                    break
        #afficher(new_carte)
        #print('-------------')
        
    return number_of_new_obstacle_possible_positions


print(resolve_problem('day_06_my_input'))



