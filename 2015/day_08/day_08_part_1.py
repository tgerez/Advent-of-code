"""

--- Day 8: Matchsticks ---

Pour l'énoncé, voir le fichier "énoncé".

"""


def resolve_problem(data_file):
    data = open(data_file, 'r')
    data_in_list = data.read().splitlines()
    
    number_of_caracters_of_code = 0
    number_of_caracters_in_strings = 0
    
    for line in data_in_list:
        len_line_of_code = len(line)
        # print(len_line_of_code)
        number_of_caracters_of_code += len_line_of_code
        
        i = 0
        len_line_of_string = 0
        
        while i < len_line_of_code:
            if line[i] == '\\': # Si on a juste un \ (mais je dois l'échapper dans mon propre code)
                if line[i+1] == 'x': # Caractère hexadécimal
                    i += 4
                    len_line_of_string += 1
                else: # On échape \ ou "
                    i += 2
                    len_line_of_string += 1
            else: # caractères qui prennent autant de place en code qu'en string
                i += 1
                len_line_of_string += 1
        
        len_line_of_string -= 2 # On supprime les guillements de début et de fin
        
        number_of_caracters_in_strings += len_line_of_string
    
    n_code = number_of_caracters_of_code
    n_string = number_of_caracters_in_strings
    
    return f'{n_code} - {n_string} = {n_code - n_string}'

print(resolve_problem('day_08_test'))
print(resolve_problem('day_08_my_input'))





