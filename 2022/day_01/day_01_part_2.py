"""

--- Part Two ---

By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?


"""


def resolve_problem(data_file):
    data = open(data_file, 'r')
    data_list = data.read().splitlines()
    
    elves = {} # a dict with elf number in key and total calories in value
    
    elf_number = 1
    
    for line in data_list:
        if line == '':
            elf_number += 1
        else:
            if elf_number in elves.keys():
                elves[elf_number] += int(line)
            else:
                elves[elf_number] = int(line)
    
    classified = sorted(list(elves.values()), reverse=True)
    
    print(classified[:3])
    
    return sum(classified[:3])


print(resolve_problem('day_01_my_input'))



