"""

--- Part Two ---

As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 

However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3

Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3

Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3

In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?


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
            stacks[to_stack].append(stacks[from_stack].pop(-crates_quantity+n-1)) # The only modification between part 1 and 2
    
    message = ''
    
    for stack in stacks.keys():
        message += stacks[stack][-1]
    
    return message

print(resolve_problem('day_05_test_input'))
print(resolve_problem('day_05_my_input'))










