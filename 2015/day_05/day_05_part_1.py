"""

--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

For example:

    ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
    aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
    jchzalrnumimnmhp is naughty because it has no double letter.
    haegwjzuvuyypxyu is naughty because it contains the string xy.
    dvszwmarrgswjxmb is naughty because it contains only one vowel.

How many strings are nice?

"""

def check_vowels(l): # l est une liste de chaines
    result = []
    for s in l: # for each string in list
        vowels = []
        for c in s: # for each caracter in string
            if c in 'aeiou':
                vowels.append(c)
        if len(vowels) >= 3:
            result.append(s)
    return result

def check_twice_letters(l): # l est une liste de chaines
    result = []
    for s in l: # for each string in list
        for i, c in enumerate(s[:-1]): # i sont les adresses, c les contenus (caractères)
            if c == s[i+1]: # On a énuméré jusqu'à l'avant dernier caractère car on compare le caractère courant au suivant
                result.append(s)
                break # pour éviter d'ajouter deux fois aux résutats une même chaine qui a deux lettres doubles
    return result

def remove_disallowed_substrings(l): # l est une liste de chaines
    result = []
    for s in l: # for each string in list
        allowed = True
        for i in range(len(s[:-1])): # i sont les adresses
            if s[i:i+2] in ['ab', 'cd', 'pq', 'xy']: # règles d'inégibilité
                allowed = False # on sort les chaines qui satisfont aux règles d'inégibilité
        if allowed:
            result.append(s)
    return result


def resolve_problem(data_file):
    data = open(data_file, 'r')
    data_in_list = data.read().splitlines()
    
    return len(remove_disallowed_substrings(check_twice_letters(check_vowels(data_in_list))))
    

print(resolve_problem('day_05_test_1'))
print(resolve_problem('day_05_my_input'))





