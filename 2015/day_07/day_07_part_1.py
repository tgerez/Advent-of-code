"""

--- Day 7: Some Assembly Required ---

This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

    123 -> x means that the signal 123 is provided to wire x.
    x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
    p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
    NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i

After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456

In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

"""

# https://wiki.python.org/moin/BitwiseOperators
# les opérateurs bit à bit dans python s'utilisent sur des entiers (décimaux)
# pas besoin de convertir en représentation binaire (ça doit être fait implicitement)

'''
The Operators:

x << y
    Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y. 
x >> y
    Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y. 
x & y
    Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0. 
x | y
    Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1. 
~ x
    Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same as -x - 1. 
x ^ y
    Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.
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

