"""

--- Day 10: Elves Look, Elves Say ---

Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading aloud the previous sequence and using that reading as the next sequence. For example, 211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).

Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each step, take the previous value, and replace each run of digits (like 111) with the number of digits (3) followed by the digit itself (1).

For example:

    1 becomes 11 (1 copy of digit 1).
    11 becomes 21 (2 copies of digit 1).
    21 becomes 1211 (one 2 followed by one 1).
    1211 becomes 111221 (one 1, one 2, and two 1s).
    111221 becomes 312211 (three 1s, two 2s, and one 1).

Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?

Your puzzle input is 3113322113.

"""



def look_and_say(seq):
    """
    This function takes in argument a string, and its return another string.
    
    It can be very improved because it takes a lot of time to execute.
    """
    seq_list = []
    for c in seq:
        seq_list.append(c)
    
    result = ''
    
    while seq_list != []:
        
        c = seq_list.pop(0)
        i = 1
        
        while seq_list != [] and seq_list[0] == c:
            seq_list.pop(0)
            i += 1
        
        result = result + str(i) + c
        
    return result
    

def resolv_problem(seq, n): # une sequence, un nombre de fois qu'on joue
    # condition particulière
    if n == 1:
        return look_and_say(seq)
    # condition générale
    else:
        return resolv_problem(look_and_say(seq), n-1)
        

#print(look_and_say(input()))
        

choix = input("Choisissez l'input :\n\
t : Thierry\n\n")

if choix == 't':
    sequence = '3113322113'
else:
    sequence = input("Entrez une séquence : ")

print('\n\nNombre d\'itérations :\n\
Partie 1 : 40 (quelques secondes).\n\
Partie 2 : 50 (quelques heures).\n\n')

nb_iter = int(input("Combien d'itérations? "))

print(len(resolv_problem(sequence, nb_iter)))
        
        
        
        
        
        
        
        


