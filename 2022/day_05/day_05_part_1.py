"""

--- Day 5: Supply Stacks ---

The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 

In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3

Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3

Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3

The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?



"""

def creating_initial_stacks(data_list):
    stacks = {}
    split_in_instructions_line = 0
    
    for i, l in enumerate(data_list):
        if l == '':
            split_in_instructions_line = i
    
    number_of_stacks = len(data_list[split_in_instructions_line-1].split())
    
    for s in range(1, number_of_stacks+1):
        stacks[s] = []
    
    for i in range(split_in_instructions_line-2, -1, -1):
        for s in range(1, number_of_stacks+1):
            crate = data_list[i][1+(s-1)*4]
            if crate != ' ':
                stacks[s].append(crate)
    
    return stacks


def identifying_moves(data_list):
    split_in_instructions_line = 0
    for i, l in enumerate(data_list):
        if l == '':
            split_in_instructions_line = i
    return data_list[split_in_instructions_line+1:]


def interpreting_moves(move_string):
    
    move_list = move_string.split()
    
    crates_quantity = int(move_list[1])
    from_stack = int(move_list[3])
    to_stack = int(move_list[5])
    
    return [crates_quantity, from_stack, to_stack]


def resolve_problem(data_file):
    data = open(data_file, 'r')
    data_list = data.read().splitlines()
    
    stacks = creating_initial_stacks(data_list)
    
    moves = identifying_moves(data_list)
    
    for m in moves:
        intructions = interpreting_moves(m)
        crates_quantity = intructions[0]
        from_stack = intructions[1]
        to_stack = intructions[2]
        for n in range(1, crates_quantity+1):
            stacks[to_stack].append(stacks[from_stack].pop())
    
    message = ''
    
    for stack in stacks.keys():
        message += stacks[stack][-1]
    
    return message

print(resolve_problem('day_05_test_input'))
print(resolve_problem('day_05_my_input'))










