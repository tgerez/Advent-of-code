"""

--- Part Two ---

The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

    ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
    ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
    ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

"""

# Tentative de résolution par programmation fonctionnelle sans passer par des classes

def new_position(c, x, y):
    # c = caracter in elf indications
    # x and y are previous positions
    if c == '<':
        x -= 1
    elif c == '>':
        x += 1
    elif c == 'v':
        y -= 1
    elif c == '^':
        y += 1
    return (x, y)

def counting_houses(elf_indications):
    # initial positions
    x_s = x_r = 0
    y_s = y_r = 0
    santa_houses = [(0, 0)] # list of coordinates of visited houses. Contains duplicates
    robot_houses = [(0, 0)]
    for i in range(len(elf_indications)):
        if i % 2 == 0: # si i est pair
            np = new_position(elf_indications[i], x_s, y_s)
            x_s, y_s = np[0], np[1]
            santa_houses.append((x_s, y_s))
        else:
            np = new_position(elf_indications[i], x_r, y_r)
            x_r, y_r = np[0], np[1]
            robot_houses.append((x_r, y_r))
    houses = santa_houses + robot_houses
    return len(set(houses)) # a set remove duplicates from a list

def resolve_problem(data_file):
    data = open(data_file, 'r')
    data_in_str = data.read() # la ligne de l'input est maintenant une str
    
    return counting_houses(data_in_str)
    

print(resolve_problem('day_03_test_1_bis'))
print(resolve_problem('day_03_test_2'))
print(resolve_problem('day_03_test_3'))
print(resolve_problem('day_03_my_input'))





