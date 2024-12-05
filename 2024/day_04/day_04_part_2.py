"""

--- Part Two ---

The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S

Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........

In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?


"""

def find_X_MAS(x:int,y:int,lines:list):
    # Check if letter at x and y is a "A", and valid or not the X-MAS
    
    if lines[y][x] == "A":
        
        backslash_diagonal = False
        if lines[y-1][x-1] == "M":
            if lines[y+1][x+1] == "S":
                backslash_diagonal = True
        elif lines[y-1][x-1] == "S":
            if lines[y+1][x+1] == "M":
                backslash_diagonal = True
        else:
            return False
        
        slash_diagonal = False
        if lines[y-1][x+1] == "M":
            if lines[y+1][x-1] == "S":
                slash_diagonal = True
        elif lines[y-1][x+1] == "S":
            if lines[y+1][x-1] == "M":
                slash_diagonal = True
        else:
            return False
        
    else:
        return False
    
    if slash_diagonal and backslash_diagonal:
        return True

def resolve_problem(data_file):
    data = open(data_file, 'r')
    
    lines = data.read().splitlines()
    
    count = 0
    
    ymax = len(lines[0]) - 1
    xmax = len(lines) - 1
    
    for y in range (1, ymax):
        for x in range(1, xmax):
            if find_X_MAS(x,y,lines):
                count += 1
    
    return count


print(resolve_problem('day_04_my_input'))



