"""
--- Day 9: Smoke Basin ---

These caves seem to be lava tubes. Parts are even still volcanically active; small hydrothermal vents release smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to avoid it and be that much safer. The submarine generates a heightmap of the floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678

Each number corresponds to the height of a particular location, where 9 is the highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than any of its adjacent locations. Most locations have four adjacent locations (up, down, left, and right); locations on the edge or corner of the map have three or two adjacent locations, respectively. (Diagonal locations do not count as adjacent.)

In the above example, there are four low points, all highlighted: two are in the first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom row (also a 5). All other locations on the heightmap have some lower adjacent location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels of all low points on your heightmap?

"""

class Lowpoint:
    def __init__(self, x, y, h): # vérifier que x, y, et h sont des entiers lors de l'attribution
        self.x = x # column coordinate (starting from 0)
        self.y = y # row coordinate (starting from 0)
        self.h = h # height (value of the point on the ground_map

def check_lowpoints_in_corners(ground_map, lowpoints, x, y):
    if x == 0:
        x_1 = 1
    elif x == -1:
        x_1 = -2
    
    if y == 0:
        y_1 = 1
    elif y == -1:
        y_1 = -2
    
    if ground_map[y][x] < ground_map[y_1][x] and ground_map[y][x] < ground_map[y][x_1]:
        lowpoints.append(Lowpoint(x, y, int(ground_map[y][x])))
    

def check_lowpoints_in_border_rows(ground_map, lowpoints, x, y): # except the corners
    
    if y == 0:
        y_1 = 1
    elif y == -1:
        y_1 = -2
    
    if ground_map[y][x] < ground_map[y_1][x] and ground_map[y][x] < ground_map[y][x-1] and ground_map[y][x] < ground_map[y][x+1]:
        lowpoints.append(Lowpoint(x, y, int(ground_map[y][x])))


def check_lowpoints_in_border_columns(ground_map, lowpoints, x, y): # except the corners
    
    if x == 0:
        x_1 = 1
    elif x == -1:
        x_1 = -2
    
    if ground_map[y][x] < ground_map[y][x_1] and ground_map[y][x] < ground_map[y-1][x] and ground_map[y][x] < ground_map[y+1][x]:
        lowpoints.append(Lowpoint(x, y, int(ground_map[y][x])))


def check_bulk_lowpoints(ground_map, lowpoints, x, y): # all points except the corners and borders
    
    if ground_map[y][x] < ground_map[y][x-1] and ground_map[y][x] < ground_map[y][x+1] and ground_map[y][x] < ground_map[y-1][x] and ground_map[y][x] < ground_map[y+1][x]:
        lowpoints.append(Lowpoint(x, y, int(ground_map[y][x])))


def resolve_problem(data_file): # data_file est le nom de fichier des données en str
    data = open(data_file, 'r')
    lines_in_list = data.read().splitlines() # 100 lignes de 100 chiffres de type str
    # lines_in_list is a ground map
    # lines_in_list is a matrix of 100 rows (100 str)
    # we call a position by the syntaxe lines_in_list[line_number][column number]
    # line_number is the y coordinate
    # column_number is the x coordinate
    
    points = [] # a list of lowpoints
    
    
    ### collecting lowpoints ###
    
    # Corners
    check_lowpoints_in_corners(lines_in_list, points, 0, 0)
    check_lowpoints_in_corners(lines_in_list, points, 0, -1)
    check_lowpoints_in_corners(lines_in_list, points, -1, 0)
    check_lowpoints_in_corners(lines_in_list, points, -1, -1)
    
    # Border rows
    for x in range(1, len(lines_in_list[0])-1): # longueur d'une ligne, en enlevant les première ert dernière position (coins)
        check_lowpoints_in_border_rows(lines_in_list, points, x, 0)
        check_lowpoints_in_border_rows(lines_in_list, points, x, -1)
    
    # Border columns
    for y in range(1, len(lines_in_list)-1): # longueur d'une colonne, en enlevant les première ert dernière position (coins)
        check_lowpoints_in_border_columns(lines_in_list, points, 0, y)
        check_lowpoints_in_border_columns(lines_in_list, points, -1, y)
        
    # Bulk points
    for x in range(1, len(lines_in_list[0])-1):
        for y in range(1, len(lines_in_list)-1):
            check_bulk_lowpoints(lines_in_list, points, x, y)
    
    sum_of_risk_levels = 0
    
    for point in points:
        sum_of_risk_levels += point.h + 1
    
    return sum_of_risk_levels
    
print(resolve_problem('test_input'))
print(resolve_problem('mon_input'))



