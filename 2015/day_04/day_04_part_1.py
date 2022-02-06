"""

--- Day 4: The Ideal Stocking Stuffer ---

Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

    If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
    If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....

"""

# https://docs.python.org/fr/3/library/hashlib.html
# https://moonbooks.org/Articles/Comment-convertir-des-octets-bytes-en-cha%C3%AEne-de-caract%C3%A8res-string-sous-python/
# >>> help(bytes)
# b'...' est une chaine de caractère transformée en bytes object
# hashlib.sha256(...) renvoie un objet '_hashlib.HASH'
# la méthode .hexdigest() permet de convertir l'objet hash en string contenant de l'info sous forme hexadécimale
'''
>>> import hashlib
>>> a = 'mot de passe'
>>> clair = bytes(a, encoding='utf-8')
>>> clair
b'mot de passe'
>>> crypt = hashlib.sha256(clair).hexdigest()
'''

import hashlib

def resolve_problem(data_file):
    data = open(data_file, 'r')
    data_in_str = data.read().splitlines()[0] # la ligne de l'input est maintenant une str
    '''
    Attention, dans le code ci-dessus, si on fait data.read() on obtient une str avec
    un retour à la ligne (disgracieux !) alors qu'en appliquant .splitlines() on coupe
    les retours à la ligne (et l'utilisation de l'index [0] permet le récupérer le seul
    élément de la liste Ainsi créée.
    Dans mes précédentes énigmes Advent of Code, il est possible que j'ai eu des problèmes
    à cause d'un retour à la ligne qui s'est glissé à mon insu dans l'input.
    '''
    
    answer = 0
    crypt = '11111'
    
    while crypt[:5] != '00000':
        
        answer += 1
        
        clair = bytes(data_in_str+str(answer), encoding='utf-8')
        crypt = hashlib.md5(clair).hexdigest()
    
    
    
    return f"""Pour l'input {data_in_str} la réponse est {answer}.
Le hash MD5 est {crypt}
"""
    

print(resolve_problem('day_04_test_1'))
print(resolve_problem('day_04_test_2'))
print(resolve_problem('day_04_my_input'))





