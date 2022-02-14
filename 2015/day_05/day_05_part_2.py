"""

--- Part Two ---

Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

    It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

For example:

    qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
    xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
    uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
    ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.

How many strings are nice under these new rules?

"""


def check_pairs_of_twice_letters(l): # l est une liste de chaines
    result = []
    for s in l: # for each string in list
        ok = False
        for i in range(len(s)-1):
            doublet = s[i:i+2]
            for j in range(i+2, len(s)-1):
                if doublet == s[j:j+2]:
                    ok = True
        if ok:
            result.append(s)
    return result

def check_repeating_letters(l): # repeating letters with exactly one letter between them
    result = []
    for s in l: # for each string in list
        ok = False
        for i in range(len(s)-2):
            if s[i] == s[i+2]:
                ok = True
        if ok:
            result.append(s)
    return result


def resolve_problem(data_file):
    data = open(data_file, 'r')
    data_in_list = data.read().splitlines()
    
    return len(check_repeating_letters(check_pairs_of_twice_letters(data_in_list)))
    

print(resolve_problem('day_05_test_2'))
print(resolve_problem('day_05_my_input'))





