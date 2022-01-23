"""
--- Day 1: Not Quite Lisp ---

--- Part Two ---

Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.

For example:

    ) causes him to enter the basement at character position 1.
    ()()) causes him to enter the basement at character position 5.

What is the position of the character that causes Santa to first enter the basement?


"""

def resolve_problem(data_file):
    data = open(data_file, 'r')
    line_in_str = data.read() # une seule ligne de type str
    
    floor = 0 # Le père Noël commence au rez
    
    caracter_position = 0
    
    for p in line_in_str: # pour chaque parenthèse dans les données
        caracter_position += 1
        
        print(line_in_str[caracter_position-1], floor, caracter_position)
        
        if floor >= 0:
        
            if p == '(':
        	    floor += 1
            elif p == ')':
                floor -= 1
        
        elif floor == -1:
            print(floor)
            return caracter_position
    
print(resolve_problem('day_01_my_input'))

'''

----

    caracter_position = 0
    
    for p in line_in_str: # pour chaque parenthèse dans les données
        caracter_position += 1
        
        if floor >= 0:
        
            if p == '(':
        	    floor += 1
            elif p == ')':
                floor -= 1
        
        else:
            return caracter_position

That's not the right answer; your answer is too high. If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again. (You guessed 1772.) [Return to Day 1]

----

Entrée manuelle...

That's the right answer! You are one gold star closer to powering the weather machine.

You have completed Day 1! You can [Shareon Twitter Mastodon] this victory or [Return to Your Advent Calendar].


'''
