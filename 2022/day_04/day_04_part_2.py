"""

--- Part Two ---

It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

    5-7,7-9 overlaps in a single section, 7.
    2-8,3-7 overlaps all of the sections 3 through 7.
    6-6,4-6 overlaps in a single section, 6.
    2-6,4-8 overlaps in sections 4, 5, and 6.

So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?


"""


def partial_overlap(elves_pair):
    """ We take in argument a list of lists representing an elves pair
    like [['2', '8'], ['3', '7']]     (in raw data it was:  2-8,3-7)
    And we calculate if there is a partial overlap. """
    
    overlap = False
    
    elf_1 = elves_pair[0]
    e1s = int(elf_1[0]) # First elf starting area
    e1f = int(elf_1[1]) # First elf finishing area
    e1a = [] # First elf areas
    for a in range(e1s, e1f+1):
        e1a.append(a)
    
    elf_2 = elves_pair[1]
    e2s = int(elf_2[0]) # Second elf starting area
    e2f = int(elf_2[1]) # Second elf finishing area
    e2a = [] # Second elf areas
    for a in range(e2s, e2f+1):
        e2a.append(a)
    
    # Checking partial overlaping
    for a in e1a:
        if a in e2a:
            overlap = True
    
    return overlap
    


def resolve_problem(data_file):
    data = open(data_file, 'r')
    data_list = data.read().splitlines()
    
    nb_of_partial_overlaps = 0
    
    for raw_pair in data_list: # Elves-pairs
        
        """Elves data processing;
        elf_1 and elf_2 will be a list of two elements:
        starting point and finishing point of theirs cleaning areas."""
        pair = raw_pair.split(',')
        elf_1 = pair[0].split('-')
        elf_2 = pair[1].split('-')
        elves_pair = [elf_1, elf_2]
        
        
        if partial_overlap(elves_pair):
            nb_of_partial_overlaps += 1
    
    return nb_of_partial_overlaps

print(resolve_problem('day_04_test_input'))
print(resolve_problem('day_04_my_input'))










