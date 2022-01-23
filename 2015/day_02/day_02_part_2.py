"""
--- Part Two ---

The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

For example:

    A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
    A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.

How many total feet of ribbon should they order?

"""

class Gift:
    all_the_ribbon_needed = 0 # Pour toute la classe
    def __init__(self, l, w, h): # Lors de la création d'une instance
        self.l = l # lenght
        self.w = w # width
        self.h = h # height
        self.rn = ribbon_needed(l, w, h)
        Gift.all_the_ribbon_needed += self.rn

def ribbon_needed(l, w, h):
    # a, b and c are areas
    a = 2*l
    b = 2*w
    c = 2*h
    # wrap is the ribbon needed to wrap
    wrap = a + b + c - max([a, b, c])
    # bow is the ribbon needed to make the bow
    bow = l*w*h
    return wrap + bow

def resolve_problem(data_file):
    Gift.all_the_ribbon_needed = 0 # Initialisons cette variable pour lui faire oublier sa valeur lors de précédents problèmes
    data = open(data_file, 'r')
    data_in_list = data.read().splitlines() # les lignes de l'input sont maintenant des éléments de liste
    
    list_of_gifts = []
    
    for gift_dimensions_str in data_in_list:
        # On extrait les valeurs de l, w et h mais de type str
        gift_dimensions_list = gift_dimensions_str.split('x')
        
        gdl = gift_dimensions_list
        
        list_of_gifts.append(Gift(int(gdl[0]), int(gdl[1]), int(gdl[2])))
    
    
    return Gift.all_the_ribbon_needed
    

print(resolve_problem('day_02_test_input_1'))
print(resolve_problem('day_02_test_input_2'))
print(resolve_problem('day_02_my_input'))





