"""

--- Day 13: Knights of the Dinner Table ---

In years past, the holiday feast with your family hasn't gone so well. Not everyone gets along! This year, you resolve, will be different. You're going to find the optimal seating arrangement and avoid all those awkward conversations.

You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if they were to find themselves sitting next to each other person. You have a circular table that will be just big enough to fit everyone comfortably, and so each person will have exactly two neighbors.

For example, suppose you have only four attendees planned, and you calculate their potential happiness as follows:

Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.

Then, if you seat Alice next to David, Alice would lose 2 happiness units (because David talks so much), but David would gain 46 happiness units (because Alice is such a good listener), for a total change of 44.

If you continue around the table, you could then seat Bob next to Alice (Bob gains 83, Alice gains 54). Finally, seat Carol, who sits next to Bob (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41). The arrangement looks like this:

     +41 +46
+55   David    -2
Carol       Alice
+60    Bob    +54
     -7  +83

After trying every other seating arrangement in this hypothetical scenario, you find that this one is the most optimal, with a total change in happiness of 330.

What is the total change in happiness for the optimal seating arrangement of the actual guest list?



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
                trio = (liste[-1], liste[0], liste[1])
            elif i == len(liste)-1:
                trio = (liste[len(liste)-2], liste[len(liste)-1], liste[0])
            else:
                trio = (liste[i-1], liste[i], liste[i+1])
            
            happiness += attendees[trio[1]][trio[0]]
            happiness += attendees[trio[1]][trio[2]]
        
        if global_happiness < happiness:
            global_happiness = happiness
        
        
    return global_happiness


print(resolve_problem('day_13_my_input'))

# copy and past the resulting string in a python shell to give the result



