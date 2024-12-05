"""

--- Part Two ---

The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

    7 6 4 2 1: Safe without removing any level.
    1 2 7 8 9: Unsafe regardless of which level is removed.
    9 7 6 2 1: Unsafe regardless of which level is removed.
    1 3 2 4 5: Safe by removing the second level, 3.
    8 6 4 4 1: Safe by removing the third level, 4.
    1 3 6 7 9: Safe without removing any level.

Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?



"""

def str_to_int(liste:list):
    result = []
    for e in liste:
        result.append(int(e))
    return result

def test_increasing_or_decreasing(liste:list):
    increasingsortedlist = sorted(liste)
    decreasingsortedlist = list(reversed(increasingsortedlist)) # reversed() crée un itérateur qu'on doit convertir en liste avec list()
    if liste == increasingsortedlist or liste == decreasingsortedlist:
        return True
    else:
        return False

def test_duplicated_levels(liste:list):
    if len(liste) == len(set(liste)):
        return True
    else:
        return False

def test_distance_between_levels(liste:list):
    for i in range(len(liste)-1):
        if abs(liste[i]-liste[i+1]) > 3:
            return False
    return True

def test_safety(report:list):
    if test_increasing_or_decreasing(report):
        if test_duplicated_levels(report):
            if test_distance_between_levels(report):
                return True
    return False

def resolve_problem(data_file):
    data = open(data_file, 'r')
    data_list = data.read().splitlines()
    
    reports = []
    
    for line in data_list:
        report = line.split()
        
        reports.append(str_to_int(report))
    
    #print(f"{reports = }")
    
    safe_reports = []
    
    for report in reports:
        if test_safety(report):
            safe_reports.append(report)
        else:
            v = False
            for i in range(len(report)):
                light_report = report[:i]+report[i+1:]
                #print(f'{light_report=}')
                if test_safety(light_report):
                    v = True
            #print(f'{v=}')
            if v:
                safe_reports.append(report)
        
    
    #print(f"{safe_reports = }")
    
    #print(f"{len(safe_reports) = }")
    
    return len(safe_reports)


print(resolve_problem('day_02_my_input'))



