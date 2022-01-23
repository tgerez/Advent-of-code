data = open('mon_input', 'r')
lines_in_list = data.read().splitlines()

data_test = open('test_input', 'r')
lines_in_list_test = data_test.read().splitlines()

"""
Les données sont la profondeur mesurée par un sonar.
Il faut compter le nombre de fois que la profondeur augmente (à chaque relevé !).
199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)
In this example, there are 7 measurements that are larger than the previous measurement.
How many measurements are larger than the previous measurement?
"""

def measurment(list_of_depth):
    number_of_increase = 0
    for i in range(1, len(list_of_depth)):
        if int(list_of_depth[i]) > int(list_of_depth[i-1]): # On doit convetir les éléments str en int !
            number_of_increase += 1
    return number_of_increase

print(measurment(lines_in_list_test))
print(measurment(lines_in_list))


