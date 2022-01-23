"""
--- Day 2: I Was Told There Would Be No Math ---

The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

For example:

    A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
    A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.

All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

"""

class Gift:
    all_the_paper_needed = 0 # Pour toute la classe
    def __init__(self, l, w, h): # Lors de la création d'une instance
        self.l = l # lenght
        self.w = w # width
        self.h = h # height
        self.pn = paper_needed(l, w, h)
        Gift.all_the_paper_needed += self.pn

def paper_needed(l, w, h):
    # a, b and c are areas
    a = 2*l*w
    b = 2*h*w
    c = 2*l*h
    # d is the lowest area
    d = int(min([a, b, c])/2)
    
    return a+b+c+d

def resolve_problem(data_file):
    Gift.all_the_paper_needed = 0 # Initialisons cette variable pour lui faire oublier sa valeur lors de précédents problèmes
    data = open(data_file, 'r')
    data_in_list = data.read().splitlines() # les lignes de l'input sont maintenant des éléments de liste
    
    list_of_gifts = []
    
    for gift_dimensions_str in data_in_list:
        # On extrait les valeurs de l, w et h mais de type str
        gift_dimensions_list = gift_dimensions_str.split('x')
        
        gdl = gift_dimensions_list
        
        list_of_gifts.append(Gift(int(gdl[0]), int(gdl[1]), int(gdl[2])))
    
    
    return Gift.all_the_paper_needed
    

print(resolve_problem('day_02_test_input_1'))
print(resolve_problem('day_02_test_input_2'))
print(resolve_problem('day_02_my_input'))





