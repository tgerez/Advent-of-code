'''

--- Part Two ---

Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?

'''


def decode(line):
    instruction = line.split()
    
    target = instruction[-1]
    
    if len(instruction) == 3: 
        if instruction[0].isnumeric(): # Attribution :   value -> wire
            inst = 'numeric_attribution'
            value = int(instruction[0])
            return (inst, value, target)
        
        else: # Attribution :   wire_1 -> wire_2
            inst = 'wire_wire_attribution'
            from_value = instruction[0]
            return (inst, from_value, target)
    
    elif len(instruction) == 4: # Bitwize complément :    NOT value_of_wire_1 -> wire_2
        inst = 'complement'
        from_value = instruction[1]
        return (inst, from_value, target)
        
    elif len(instruction) == 5: # Other operations : Bwze AND, OR, L or R shift
        inst = instruction[1] # AND, OR, LSHIFT, RSHIFT
        
        if inst in ('AND', 'OR'):
            from_value_1 = instruction[0]
            from_value_2 = instruction[2]
            return (inst, from_value_1, from_value_2, target)
            
        else: # inst in ('LSHIFT', 'RSHIFT')
            from_value = instruction[0]
            shift_lenght = int(instruction[2])
            return (inst, from_value, shift_lenght, target)
        

def presentating_results(wires : dict, data_file : str):
    # list of sorted value dict
    sorted_wires = sorted(wires)
    result = ''
    for identifier in sorted_wires:
        if result == '':
            result = f'\nResults for {data_file} :\n{identifier} {wires[identifier]}'
        else:
            result += f'\n{identifier} {wires[identifier]}'
    return result + '\n-----\n'

def resolve_problem(data_file):
    data = open(data_file, 'r')
    data_in_list = data.read().splitlines()
    
    wires = {} # dictionnaire de fils dont les clés/valeurs sont leurs identifiants/signaux
    
    # Pour toutes les instructions :
    # Celles qui sont de type attribution numérique, on les fait.
    for line in data_in_list:
        instructions = decode(line)
        target = instructions[-1]
        if instructions[0] == 'numeric_attribution':
            wires[target] = instructions[1]
    
    # Pour toutes les instructions :
    # on met les fils possibles (cibles des instructions) dans un set
    possible_wires = set()
    for line in data_in_list:
        instructions = decode(line)
        possible_wires.add(instructions[-1])
    
    # L'input cache un fil nommé 1 dont la valeur du signal est 1
    # Mais il n'est pas créé par une instruction d'attrobution
    # Il est directement utilisé dans les fonctions AND et OR
    wires['1'] = 1
    possible_wires.add('1')
    
    # Overwriting for part II
    wires['b'] = 16076
    
    # Pour toutes les instructions :
    # Tant que la longueur du dico de fils est inférieure à la longueur du set 
    # des fils possibles, faire la succession des instruction uniquement
    # pour les fils qui peuvent être calculés à partir de fils qui sont dans le dico
    while len(wires) < len(possible_wires):
        for line in data_in_list:
            instructions = decode(line)
            
            target = instructions[-1]
            
            if instructions[0] == 'wire_wire_attribution':
                if instructions[1] in wires.keys():
                    wires[target] = wires[instructions[1]]
            
            if instructions[0] == 'complement':
                if instructions[1] in wires.keys():
                    wires[target] = 65535 - wires[instructions[1]]
            
            elif instructions[0] == 'AND':
                if instructions[1] in wires.keys() and instructions[2] in wires.keys():
                    wires[target] = wires[instructions[1]] & wires[instructions[2]]
            
            elif instructions[0] == 'OR':
                if instructions[1] in wires.keys() and instructions[2] in wires.keys():
                   wires[target] = wires[instructions[1]] | wires[instructions[2]]
            
            elif instructions[0] == 'LSHIFT':
                if instructions[1] in wires.keys():
                    wires[target] = wires[instructions[1]] << instructions[2]
            
            elif instructions[0] == 'RSHIFT':
                if instructions[1] in wires.keys():
                   wires[target] = wires[instructions[1]] >> instructions[2]
    
    
    return presentating_results(wires, data_file)

print(resolve_problem('day_07_test'))
print(resolve_problem('day_07_my_input'))

