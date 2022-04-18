"""

--- Part Two ---

In all the commotion, you realize that you forgot to seat yourself. At this point, you're pretty apathetic toward the whole thing, and your happiness wouldn't really go up or down regardless of who you sit next to. You assume everyone else would be just as ambivalent about sitting next to you, too.

So, add yourself to the list, and give all happiness relationships that involve you a score of 0.

What is the total change in happiness for the optimal seating arrangement that actually includes yourself?


"""

import itertools
import math

''' Nous allons avoir un dictionnaire qui contient un autre dictionnaire

attendees = {
'Alice' : {'Bob' : 54, 'Carol' : -79, 'David' : -2},
'Bob' : {'Alice' : 83, 'Carol' : -7, 'David': -63}
}

Dans cet exemple, Alice gagne 54 points de bonheur en se mettant à côté de Bob et ce dernier gagne 83 points de bonheur en se plaçant à côté de Alice.

'''

def resolve_problem(data_file):
    data = open(data_file, 'r')
    data_list = data.read().splitlines()
    
    attendees = {}
    
    # attribution des invités comme clés primaires du dictionnaire
    for line in data_list:
        line = line[:-1].split() # La syntaxe en slice jusqu'à la dernière position (-1) exclue permet d'enlever le point final de chaque ligne
        attendees[line[0]] = {}
    
    liste_convives = list(attendees.keys())
    
    for line in data_list:
        line = line[:-1].split() # La syntaxe en slice jusqu'à la dernière position (-1) exclue permet d'enlever le point final de chaque ligne
        if line[2] == 'gain':
            sign = 1
        elif line[2] == 'lose':
            sign = -1
        attendees[line[0]][line[-1]] = sign * int(line[3])
        
    
    global_happiness = -math.inf
    
    for liste in itertools.permutations(liste_convives):
        happiness = 0
        for i in range(len(liste)):
            if i == 0:
                # you are before the first attendee
                trio = ('you', liste[0], liste[1])
                happiness += attendees[trio[1]][trio[2]]
            elif i == len(liste)-1:
                # you are after the last attendee
                trio = (liste[len(liste)-2], liste[len(liste)-1], 'you')
                happiness += attendees[trio[1]][trio[0]]
            else:
                trio = (liste[i-1], liste[i], liste[i+1])
                happiness += attendees[trio[1]][trio[0]]
                happiness += attendees[trio[1]][trio[2]]
            
        
        if global_happiness < happiness:
            global_happiness = happiness
        
        
    return global_happiness


print(resolve_problem('day_13_my_input'))




