data = open('mon_input', 'r')
lines_in_list = data.read().splitlines()

data_test = open('test_input', 'r')
lines_in_list_test = data_test.read().splitlines()

"""
--- Part Two ---

Considering every single measurement isn't as useful as you expected: there's just too much noise in the data.

Instead, consider sums of a three-measurement sliding window. Again considering the above example:

199  A      
200  A B    
208  A B C  
210    B C D
200  E   C D
207  E F   D
240  E F G  
269    F G H
260      G H
263        H

Start by comparing the first and second three-measurement windows. The measurements in the first window are marked A (199, 200, 208); their sum is 199 + 200 + 208 = 607. The second window is marked B (200, 208, 210); its sum is 618. The sum of measurements in the second window is larger than the sum of the first, so this first comparison increased.

Your goal now is to count the number of times the sum of measurements in this sliding window increases from the previous sum. So, compare A with B, then compare B with C, then C with D, and so on. Stop when there aren't enough measurements left to create a new three-measurement sum.

In the above example, the sum of each three-measurement window is as follows:

A: 607 (N/A - no previous sum)
B: 618 (increased)
C: 618 (no change)
D: 617 (decreased)
E: 647 (increased)
F: 716 (increased)
G: 769 (increased)
H: 792 (increased)

In this example, there are 5 sums that are larger than the previous sum.
"""

def measurment(list_of_depth):
    number_of_increase = 0
    list_of_int = []
    for e in list_of_depth:
        list_of_int.append(int(e))
    for i in range(len(list_of_int)-3):
        if list_of_int[i]+list_of_int[i+1]+list_of_int[i+2] < list_of_int[i+1]+list_of_int[i+2]+list_of_int[i+3]:
            number_of_increase += 1
    return number_of_increase

print(measurment(lines_in_list_test))
print(measurment(lines_in_list))


