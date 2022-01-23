data = open('mon_input', 'r')
lines_in_list = data.read().splitlines()

data_test = open('test_input', 'r')
lines_in_list_test = data_test.read().splitlines()

"""
--- Day 3: Binary Diagnostic ---

The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the power consumption.

You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. For example, given the following diagnostic report:

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010

Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)

"""

def string_binary_to_decimal_int(s):
    """
    Fonction qui prend en argument une str qui contient un mot de plusieurs bits, comme 110110011
    Et renvoie un entier qui est l'expression décimal de l'entier correspondant à ce mot
    """
    result = 0
    for c in range(-1, - len(s) -1, -1):
        result += int(s[c]) * 2**(abs(c)-1)
    return result

def binary_diagnostic(list_of_datas):
    gamma_rate = '' # gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report.
    premiere_ligne = list_of_datas[0]
    frequences_bits_1 = []
    gamma_rate_list = []
    for b in premiere_ligne: # b sont des caractères de fréquence str
        frequences_bits_1.append(0) # on crée les emplacements du compteur
    for position in list_of_datas: # position est de type str et contient 5 caractères (1 ou 0)
        for i in range(len(position)):# i est l'indice du bit de la position
            frequences_bits_1[i] += int(position[i])
    quantity_of_each_bit = len(list_of_datas)
    for freq in frequences_bits_1: # freq sont des entiers
        if freq > quantity_of_each_bit/2:
            gamma_rate_list.append(1)
        else:
            gamma_rate_list.append(0)
    gamma_rate_list_str = []
    for e in gamma_rate_list:
        gamma_rate_list_str.append(str(e))
    gamma_rate = ''.join(gamma_rate_list_str) # gamma_rate is a string
    
    epsilon_rate = ''
    for c in gamma_rate:
        if c == '0':
            epsilon_rate += '1'
        else: # c == '1'
            epsilon_rate += '0'
    
    power_consumption = string_binary_to_decimal_int(gamma_rate) * string_binary_to_decimal_int(epsilon_rate) # gamma_rate * epsilon_rate
        
#    return gamma_rate, epsilon_rate, string_binary_to_decimal_int(gamma_rate), string_binary_to_decimal_int(epsilon_rate), power_consumption
    return power_consumption

print(binary_diagnostic(lines_in_list_test))
print(binary_diagnostic(lines_in_list))














