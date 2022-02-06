"""

--- Part Two ---

Now find one that starts with six zeroes.

"""

import hashlib

def resolve_problem(data_file):
    data = open(data_file, 'r')
    data_in_str = data.read().splitlines()[0] # la ligne de l'input est maintenant une str
    
    answer = 0
    crypt = '111111'
    
    while crypt[:6] != '000000': # ne pas oublier de modifier la chaine contenant 6 zéros ET la syntaxe en slice (avec crypt[:5] != '000000' on peut attendre longtemps que le programme se finisse...
        
        answer += 1
        
        clair = bytes(data_in_str+str(answer), encoding='utf-8')
        crypt = hashlib.md5(clair).hexdigest()
    
    
    
    return f"""Pour l'input {data_in_str} la réponse est {answer}.
Le hash MD5 est {crypt}
"""
    

print(resolve_problem('day_04_test_1'))
print(resolve_problem('day_04_test_2'))
print(resolve_problem('day_04_my_input'))





