"""

--- Part Two ---

As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact. If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more accurate result.

There are two new instructions you'll need to handle:

    The do() instruction enables future mul instructions.
    The don't() instruction disables future mul instructions.

Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

For example:

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))

This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are disabled because there is a don't() instruction before them. The other mul instructions function normally, including the one at the end that gets re-enabled by a do() instruction.

This time, the sum of the results is 48 (2*4 + 8*5).

Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?


"""

import re

def make_operation(instruction:str):
    # instruction is like 'mul(xx,yy)' with ww and yy digits
    cleaned_instruction = instruction[4:-1]
    numbers = cleaned_instruction.split(",")
    return int(numbers[0])*int(numbers[1])

def resolve_problem(data_file):
    data = open(data_file, 'r')
    #data_list = data.read().splitlines()
    data_str = data.read()
    
    p = re.compile(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)')
    raw_instructions = p.findall(data_str) # raw_instructions is a list
    
    results = [] # la liste des résultats des multiplications
    
    mul_enabled = True
    
    for instruction in raw_instructions:
        if instruction == "do()":
            mul_enabled = True
            continue
        elif instruction == "don't()":
            mul_enabled = False
            continue
        else:
            if mul_enabled:
                results.append(make_operation(instruction))
    
    return sum(results)

# Attention en cas de choix des données de test, elles sont différentes entre les parties 1 et 2 ...
print(resolve_problem('day_03_my_input'))



