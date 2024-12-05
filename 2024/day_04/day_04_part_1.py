"""

--- Day 4: Ceres Search ---

"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:

..X...
.SAMX.
.A..A.
XMAS.S
.X....

The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX

In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX

Take a look at the little Elf's word search. How many times does XMAS appear?


"""

import re

# Fonction pour gérer les correspondances chevauchantes
# Source : ChatGPT
def find_all_matches_even_overlapping(pattern, text):
    # pattern est le motif comme re.compile(r'cats|surf')
    # text est la chaine à analyser comme "catsurf cats surfing catsurfing surfingcats surfcats catsurf"
    # renvoie une liste de tous les mots (cats, surf) même concaténés
    matches = []
    pos = 0
    while pos < len(text):
        match = pattern.search(text, pos)
        if not match:
            break
        matches.append(match.group())
        pos = match.start() + 1  # Avance d'un caractère pour détecter les chevauchements
    return matches

def convert_lines_to_columns(lines:list):
    columns = []
    # initialiser
    for c in lines[0]:
        columns.append("")
    # remplir
    for line in lines:
        for i, c in enumerate(line):
            columns[i] += c
    return columns

def make_diagonal(xi:int,yi:int,lines:list,ymax:int):
    x = xi
    y = yi
    diagonal = ""
    while x >= 0 and y <= ymax:
        diagonal += lines[y][x]
        x -= 1
        y += 1
    return diagonal

def make_slash_diagonals(lines:list):
    diagonals = []
    xi = 0
    yi = 0
    xmax = len(lines[0]) - 1
    ymax = len(lines) - 1
    while yi <= ymax:
        while xi <= xmax:
            diagonals.append(make_diagonal(xi,yi,lines,ymax))
            if xi < xmax:
                xi += 1
            else:
                break
        yi += 1
    return diagonals

def make_backslash_diagonals(lines:list):
    reversed_lines = list(reversed(lines))
    return make_slash_diagonals(reversed_lines)

def resolve_problem(data_file):
    data = open(data_file, 'r')
    
    lines = data.read().splitlines()
    
    columns = convert_lines_to_columns(lines)
    slash_diagonals = make_slash_diagonals(lines)
    backslash_diagonals = make_backslash_diagonals(lines)
    
    count = 0
    
    for line in lines:
        p = re.compile(r'XMAS|SAMX')
        found = find_all_matches_even_overlapping(p, line)
        count += len(found)
    
    for column in columns:
        p = re.compile(r'XMAS|SAMX')
        found = find_all_matches_even_overlapping(p, column)
        count += len(found)
    
    for diagonal in slash_diagonals:
        p = re.compile(r'XMAS|SAMX')
        found = find_all_matches_even_overlapping(p, diagonal)
        count += len(found)
    
    for diagonal in backslash_diagonals:
        p = re.compile(r'XMAS|SAMX')
        found = find_all_matches_even_overlapping(p, diagonal)
        count += len(found)
    
    return count


print(resolve_problem('day_04_my_input'))



