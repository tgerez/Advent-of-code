"""
--- Day 1: Not Quite Lisp ---

Santa was hoping for a white Christmas, but his weather machine's "snow" function is powered by stars, and he's fresh out! To save Christmas, he needs you to collect fifty stars by December 25th.

Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

Here's an easy puzzle to warm you up.

Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example:

    (()) and ()() both result in floor 0.
    ((( and (()(()( both result in floor 3.
    ))((((( also results in floor 3.
    ()) and ))( both result in floor -1 (the first basement level).
    ))) and )())()) both result in floor -3.

To what floor do the instructions take Santa?

"""

def resolve_problem(data_file):
    data = open(data_file, 'r')
    line_in_str = data.read() # une seule ligne de type str
    
    floor = 0 # Le père Noël commence au rez
    
    for p in line_in_str: # pour chaque parenthèse dans les données
        if p == '(':
    	    floor += 1
        elif p == ')':
            floor -= 1
    
    return floor
    
print(resolve_problem('day_01_my_input'))

'''

-----

    for p in line_in_str: # pour chaque parenthèse dans les données
        if p == '(':
    	    floor += 1
        else: # p == ')'       Je suppose que le créateur des énigmes n'est pas un sadique
            floor -= 1
            
That's not the right answer; your answer is too low. If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again. (You guessed 137.) [Return to Day 1]

-----

    for p in line_in_str: # pour chaque parenthèse dans les données
        if p == '(':
    	    floor += 1
        elif p == '(':
            floor -= 1

That's not the right answer; your answer is too high. If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again. (You guessed 3569.) [Return to Day 1]

-----

    for p in line_in_str: # pour chaque parenthèse dans les données
        if p == '(':
    	    floor += 1
        elif p == ')': # évidemment il vaut mieux une parenthèse fermante...
            floor -= 1

That's the right answer! You are one gold star closer to powering the weather machine. [Continue to Part Two]

'''



