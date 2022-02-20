"""

--- Part Two ---

You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

    turn on 0,0 through 0,0 would increase the total brightness by 1.
    toggle 0,0 through 999,999 would increase the total brightness by 2000000.

"""

import numpy as np

def decode(line):
    liste = line.split()
    return liste

def resolve_problem(data_file):
    data = open(data_file, 'r')
    data_in_list = data.read().splitlines()
    
    
    # Génération d'une matrice de 0. qui sont des flottants
    matrix = np.zeros((1000, 1000))
    
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
            matrix[start_line:end_line, start_column:end_column] += 1
        
        elif inst == 'off':
            for x in range(start_line, end_line):
                for y in range(start_column, end_column):
                    if matrix[x][y] > 0:
                        matrix[x][y] -= 1
        
        elif inst == 'toggle':
            matrix[start_line:end_line, start_column:end_column] += 2
    
    #print(matrix)
    
    return int((np.sum(matrix)))

print(resolve_problem('day_06_test_3'))
print(resolve_problem('day_06_test_4'))
print(resolve_problem('day_06_my_input'))





