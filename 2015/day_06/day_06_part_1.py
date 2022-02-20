"""

--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

    turn on 0,0 through 999,999 would turn on (or leave on) every light.
    toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
    turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

After following the instructions, how many lights are lit?


"""

import numpy as np

def decode(line):
    liste = line.split()
    return liste

def resolve_problem(data_file):
    data = open(data_file, 'r')
    data_in_list = data.read().splitlines()
    
    """
    # Génération d'une matrice de 0 qui sont des entiers
    grid = []
    for n in range(1000):
        grid.append([])
        for m in range(1000):
            grid[n].append(0)
    
    matrix = np.array(grid)
    """
    
    # Génération d'une matrice de 0. qui sont des flottants
    matrix = np.zeros((1000, 1000))
    
    # https://courspython.com/tableaux-numpy.html#slicing-des-tableaux-2d
    # matrix[ligne, colonne]
    
    #print(matrix)
    
    for line in data_in_list:
        instruction = decode(line)
        
        
        if len(instruction) == 4: # toggle
            inst = 'toggle'
            # coordinates of the reclangle
            start = instruction[1].split(',')
            end = instruction[3].split(',')
        
        elif len(instruction) == 5: # turn on or off
            inst = instruction[1]
            # coordinates of the reclangle
            start = instruction[2].split(',')
            end = instruction[4].split(',')

        start_column = int(start[0])
        start_line = int(start[1])
        
        end_column = int(end[0]) + 1 # On rajoute 1 car la syntaxe en slice utilisée ensuite va ignorer la dernière position
        end_line= int(end[1]) + 1
        
        if inst == 'on':
            matrix[start_line:end_line, start_column:end_column] = 1
        
        elif inst == 'off':
            matrix[start_line:end_line, start_column:end_column] = 0
        
        elif inst == 'toggle':
            for x in range(start_line, end_line):
                for y in range(start_column, end_column):
                    matrix[x][y] = int(not bool(matrix[x][y]))
    
    #print(matrix)
    
    return int(np.sum(matrix))

print(resolve_problem('day_06_test_1'))
print(resolve_problem('day_06_test_2'))
print(resolve_problem('day_06_my_input'))





