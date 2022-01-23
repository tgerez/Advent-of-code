"""
--- Day 4: Giant Squid ---

You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7

After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

Finally, 24 is drawn:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7

At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?

"""

class Grid:
    def __init__(self, name, grid):
        self.name = name
        self.content = []
        self.grid = grid

class Row:
    def __init__(self, name, content, grid):
        self.name = name
        self.content = content
        self.grid = grid
        self.numeros_sortis = 0

class Column:
    def __init__(self, name, grid):
        self.name = name
        self.content = []
        self.grid = grid
        self.numeros_sortis = 0

def resolve_bingo_problem(data_file): # data_file est le nom de fichier des données en str
    data = open(data_file, 'r')
    lines_in_list = data.read().splitlines()
    
    tirage_str = lines_in_list[0] # str contenant les numéros qui vont être tirés séparés par des virgules
    tirage_str = tirage_str.split(',') # liste ontenant les numéros qui vont être tirés
    tirage = []
    for i in range(len(tirage_str)):
        tirage.append(int(tirage_str[i]))
    
    numeros_tires = [] # numéros déjà tirés
    
    rows = []
    columns = []
    grids = []
    
    grid_number = 1
    
    # On remplit des objets lignes avec l'input (création des instances de Row)
    # on fait de même avec les grilles (listes de 25 éléments)
    for i in range(2, len(lines_in_list)): # les grilles commencent à la ligne 3
        
        if len(grids) < grid_number:
            grids.append(Grid(f'grille {grid_number}', grid_number))
            
        if lines_in_list[i] == '':
            grid_number += 1
        else:
            # nom de ligne, contenu (liste de 5numéros) et numéro de grille
            rows.append(Row(f'ligne {i}', lines_in_list[i].split(), grid_number))
            grids[-1].content.extend(lines_in_list[i].split())
    
    # Création et remplissage des objets colonnes
    for grid in grids:
        for i in range(1, 6):
            columns.append(Column(f'colonne {i} de la grille {grid.grid}', grid.grid))
            for n in range(0, 25, 5):
                columns[-1].content.append(grid.content[i-1+n])
    
    # On effectue le tirage
    for n in tirage_str:
        numeros_tires.append(int(n))
        
        for row in rows:
            if n in row.content:
                row.numeros_sortis += 1
                if row.numeros_sortis == 5:
                    print(f'La ligne {row.name} (grille {row.grid}) est gagnante après {len(numeros_tires)} numéros tirés !')
                    # La partie s'arrête, il faut calculer le score et le renvoyer
                    for grid in grids:
                        if grid.grid == row.grid:
                            for n in numeros_tires:
                                if str(n) in grid.content:
                                    grid.content.remove(str(n)) # on retire les numéros tirés de la grille gagnante
                            # Le score final est la somme des numéros restants de la grille * le dernier numéro tiré
                            # ces numéros sont encore des str donc on doit les convertir en int
                            grid_content_int = []
                            for i in range(len(grid.content)):
                                grid_content_int.append(int(grid.content[i]))
                            return sum(grid_content_int) * numeros_tires[-1]
        
        for column in columns:
            if n in column.content:
                column.numeros_sortis += 1
                if column.numeros_sortis == 5:
                    print(f'La colonne {column.name} (grille {column.grid}) est gagnante après {len(numeros_tires)} numéros tirés !')
                    # La partie s'arrête, il faut calculer le score et le renvoyer
                    for grid in grids:
                        if grid.grid == column.grid:
                            for n in numeros_tires:
                                if str(n) in grid.content:
                                    grid.content.remove(str(n)) # on retire les numéros tirés de la grille gagnante
                            # Le score final est la somme des numéros restants de la grille * le dernier numéro tiré
                            # ces numéros sont encore des str donc on doit les convertir en int
                            grid_content_int = []
                            for i in range(len(grid.content)):
                                grid_content_int.append(int(grid.content[i]))
                            return sum(grid_content_int) * numeros_tires[-1]

print(resolve_bingo_problem('test_input'))
print(resolve_bingo_problem('mon_input'))



