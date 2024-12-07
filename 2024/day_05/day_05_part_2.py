"""

--- Part Two ---

While the Elves get to work printing the correctly-ordered updates, you have a little time to fix the rest of them.

For each of the incorrectly-ordered updates, use the page ordering rules to put the page numbers in the right order. For the above example, here are the three incorrectly-ordered updates and their correct orderings:

    75,97,47,61,53 becomes 97,75,47,61,53.
    61,13,29 becomes 61,29,13.
    97,13,75,29,47 becomes 97,75,47,29,13.

After taking only the incorrectly-ordered updates and ordering them correctly, their middle page numbers are 47, 29, and 47. Adding these together produces 123.

Find the updates which are not in the correct order. What do you get if you add up the middle page numbers after correctly ordering just those updates?


"""

def treating_raw_rule(line:str):
    rule = line.split("|")
    return rule

def treating_raw_update(line:str):
    update = line.split(",")
    return update

def treating_input(lines:list):
    rules = []
    updates = []
    i = 0
    for line in lines:
        if "|" in line:
            rule = treating_raw_rule(line)
            rules.append(rule)
        elif "," in line:
            update = treating_raw_update(line)
            updates.append(update)
    return rules, updates

def validation(update:list, rules:list):
    for i, page in enumerate(update):
        for rule in rules:
            if page == rule[0]:
                if rule[1] in update[:i]:
                    return False
    return True

def unvalidation(update:list, rules:list):
    for i, page in enumerate(update):
        for rule in rules:
            if page == rule[0]:
                if rule[1] in update[:i]:
                    return True
    return False
    
def make_valid(update:list, rules:list): # Utilisation du tri à bulles
    valided_update = update.copy()
    while not validation(valided_update, rules):
        for i, page in enumerate(valided_update):
            for rule in rules:
                if page == rule[0]:
                    if rule[1] in valided_update[:i]:
                        for j in range(i):
                             if rule[1] == valided_update[j]:
                                 valided_update[i], valided_update[j] = valided_update[j], valided_update[i]
                                 break
    #print(valided_update)
    return valided_update

def resolve_problem(data_file):
    data = open(data_file, 'r')
    lines = data.read().splitlines()
    
    # each update in updates must be a list
    # each rule is also a list of 2 elements : rule[0] is always before rule[1]
    rules, updates = treating_input(lines)
    
    uncorrect_updates = []
    
    for update in updates:
        if unvalidation(update, rules):
            uncorrect_updates.append(update)
    
    corrected_uncorrect_updates = []
    
    for update in uncorrect_updates:
        corrected_uncorrect_updates.append(make_valid(update, rules))
    
    middles_pages_of_corrected_uncorrect_uptades = []
    
    for update in corrected_uncorrect_updates:
         m = len(update)//2
         middles_pages_of_corrected_uncorrect_uptades.append(int(update[m]))
    
    
    return sum(middles_pages_of_corrected_uncorrect_uptades)


print(resolve_problem('day_05_my_input'))



