"""

--- Day 4: Camp Cleanup ---

Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been assigned the job of cleaning up sections of the camp. Every section has a unique ID number, and each Elf is assigned a range of section IDs.

However, as some of the Elves compare their section assignments with each other, they've noticed that many of the assignments overlap. To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a big list of the section assignments for each pair (your puzzle input).

For example, consider the following list of section assignment pairs:

2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8

For the first few pairs, this list means:

    Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the second Elf was assigned sections 6-8 (sections 6, 7, 8).
    The Elves in the second pair were each assigned two sections.
    The Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7, while the other also got 7, plus 8 and 9.

This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger numbers. Visually, these pairs of section assignments look like this:

.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8

Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration. In this example, there are 2 such pairs.

In how many assignment pairs does one range fully contain the other?

To begin, get your puzzle input.


"""


def full_overlap(elves_pair):
    """ We take in argument a list of lists representing an elves pair
    like [['2', '8'], ['3', '7']]     (in raw data it was:  2-8,3-7)
    And we calculate if there is a full overlap. """
    
    overlap = False
    
    elf_1 = elves_pair[0]
    e1s = int(elf_1[0]) # First elf starting area
    e1f = int(elf_1[1]) # First elf finishing area
    
    elf_2 = elves_pair[1]
    e2s = int(elf_2[0]) # Second elf starting area
    e2f = int(elf_2[1]) # Second elf finishing area
    
    # First elf containing the second ?
    if e1s <= e2s:
        if e1f >= e2f:
            overlap = True
    
    # Second elf containing the first ?
    if e2s <= e1s:
        if e2f >= e1f:
            overlap = True
    
    return overlap
    


def resolve_problem(data_file):
    data = open(data_file, 'r')
    data_list = data.read().splitlines()
    
    nb_of_full_overlaps = 0
    
    for raw_pair in data_list: # Elves-pairs
        
        """Elves data processing;
        elf_1 and elf_2 will be a list of two elements:
        starting point and finishing point of theirs cleaning areas."""
        pair = raw_pair.split(',')
        elf_1 = pair[0].split('-')
        elf_2 = pair[1].split('-')
        elves_pair = [elf_1, elf_2]
        
        
        if full_overlap(elves_pair):
            nb_of_full_overlaps += 1
    
    return nb_of_full_overlaps

print(resolve_problem('day_04_test_input'))
print(resolve_problem('day_04_my_input'))










