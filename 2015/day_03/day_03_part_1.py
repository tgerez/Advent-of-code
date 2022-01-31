"""

--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

    > delivers presents to 2 houses: one at the starting location, and one to the east.
    ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
    ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

"""

# Tentative de résolution par programmation fonctionnelle sans passer par des classes

def counting_houses(elf_indications):
    # initial positions
    x = 0
    y = 0
    houses = [(x, y)] # list of coordinates of visited houses. Contains duplicates
    for c in elf_indications:
        if c == '<':
            x -= 1
        elif c == '>':
            x += 1
        elif c == 'v':
            y -= 1
        elif c == '^':
            y += 1
        houses.append((x, y))
    return len(set(houses)) # a set remove duplicates from a list

def resolve_problem(data_file):
    data = open(data_file, 'r')
    data_in_str = data.read() # la ligne de l'input est maintenant une str
    
    return counting_houses(data_in_str)
    

print(resolve_problem('day_03_test_1'))
print(resolve_problem('day_03_test_2'))
print(resolve_problem('day_03_test_3'))
print(resolve_problem('day_03_my_input'))





