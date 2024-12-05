"""

--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?


"""

# https://docs.python.org/fr/3/howto/regex.html#modifying-strings
# https://docs.python.org/fr/3/howto/regex.html#grouping
import re

"""
On va devoir remplacer le chiffre exprimé en lettres par son expression numérique, en analysant les lignes soigneusement :
- si aucune expression en lettres n'est trouvée, on renvoie la ligne telle qu'elle,
- si une expression en lettres est trouvée, on remplace sans se prendre la tête et on renvoie la ligne 
- s'il y en a deux :
    - si elles ne sont pas imbriquées, on remplace sans se prendre la tête et on renvoie la ligne
    - si elles le sont, on doit déterminer où sont les vrais chiffres déjà en place par rapport aux lettres qui vont donner des chiffres (pour savoir si on récupère le chiffre de gauche, qui sera le premier de la chaine, ou le chiffre de droite, qui sera le dernier)
- s'il y en a trois ou plus, on ne convertit que la première et la dernière sans se soucier des intermédiaires

Autre idée : braquage. Chercher les concaténations possibles dans tout le texte et les remplacer simplement par les deux chiffres correspondants (ça fonctionne ! Heureusement, Eric Wastl n'a pas fait de triples concaténations...)

"""

def converting_spelled_digits(text:str):
    
    p = re.compile('oneight')
    text = p.sub('18', text)
    
    p = re.compile('twone')
    text = p.sub('21', text)
    
    p = re.compile('threeight')
    text = p.sub('38', text)
    
    p = re.compile('fiveight')
    text = p.sub('58', text)
    
    p = re.compile('sevenine')
    text = p.sub('79', text)
    
    p = re.compile('eightwo')
    text = p.sub('82', text)
    
    p = re.compile('eighthree')
    text = p.sub('83', text)
    
    p = re.compile('nineight')
    text = p.sub('98', text)
    
    p = re.compile('one')
    text = p.sub('1', text)
    p = re.compile('two')
    text = p.sub('2', text)
    p = re.compile('three')
    text = p.sub('3', text)
    p = re.compile('four')
    text = p.sub('4', text)
    p = re.compile('five')
    text = p.sub('5', text)
    p = re.compile('six')
    text = p.sub('6', text)
    p = re.compile('seven')
    text = p.sub('7', text)
    p = re.compile('eight')
    text = p.sub('8', text)
    p = re.compile('nine')
    text = p.sub('9', text)
    
    return text


def find_first_digit(string):
    for c in string:
        if c.isnumeric():
            return c

def find_last_digit(string):
    for c in reversed(string):
        if c.isnumeric():
            return c

def desamending(line:str):
    first = find_first_digit(line)
    last = find_last_digit(line)
    return int(first+last)


def resolve_problem(data_file):
    data = open(data_file, 'r')
    
    data_str = data.read()
    
    data_str_converties = converting_spelled_digits(data_str)
    
    data_list = data_str_converties.splitlines()
    
    calibration_values = []
    
    for line in data_list:
        value = desamending(line)
        calibration_values.append(value)
    
    return sum(calibration_values)


print(resolve_problem('day_01_my_input'))



