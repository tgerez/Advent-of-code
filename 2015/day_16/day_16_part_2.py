"""

--- Part Two ---

As you're about to send the thank you note, something in the MFCSAM's instructions catches your eye. Apparently, it has an outdated retroencabulator, and so the output from the machine isn't exact values - some of them indicate ranges.

In particular, the cats and trees readings indicates that there are greater than that many (due to the unpredictable nuclear decay of cat dander and tree pollen), while the pomeranians and goldfish readings indicate that there are fewer than that many (due to the modial interaction of magnetoreluctance).

What is the number of the real Aunt Sue?

"""

def comparison(ticket, prop_name, prop_number):
    if prop_name == 'cats' or prop_name == 'trees':
        if ticket[prop_name] < prop_number:
            return True
        else:
            return False
    elif prop_name == 'pomeranians' or prop_name == 'goldfish':
        if ticket[prop_name] > prop_number:
            return True
        else:
            return False
    else:
        if ticket[prop_name] == prop_number:
            return True
        else:
            return False

def resolve_problem(data_file):
    data = open(data_file, 'r')
    data_list = data.read().splitlines()
    
    ticket = {
'children': 3,
'cats': 7,
'samoyeds': 2,
'pomeranians': 3,
'akitas': 0,
'vizslas': 0,
'goldfish': 5,
'trees': 3,
'cars': 2,
'perfumes': 1}
    
    for line in data_list:
        properties = line.split()
        # parameters assignation and cleaning terminal caracters in the input (: or ,)
        sue_number = properties[1][:-1]
        prop_1_name = properties[2][:-1]
        prop_1_number = int(properties[3][:-1])
        prop_2_name = properties[4][:-1]
        prop_2_number = int(properties[5][:-1])
        prop_3_name = properties[6][:-1]
        prop_3_number = int(properties[7])
        
        if comparison(ticket, prop_1_name, prop_1_number):
            if comparison(ticket, prop_2_name, prop_2_number):
                if comparison(ticket, prop_3_name, prop_3_number):
                    return f'La tante qui a envoyé le cadeau est la numéro {sue_number}.'
    
    return 'Pas de tante trouvée.'


print(resolve_problem('day_16_my_input'))



