"""

--- Day 15: Science for Hungry People ---

Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon:

    capacity (how well it helps the cookie absorb milk)
    durability (how well it keeps the cookie intact when full of milk)
    flavor (how tasty it makes the cookie)
    texture (how it improves the feel of the cookie)
    calories (how many calories it adds to the cookie)

You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.

For instance, suppose you have these two ingredients:

Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties:

    A capacity of 44*-1 + 56*2 = 68
    A durability of 44*-2 + 56*3 = 80
    A flavor of 44*6 + 56*-2 = 152
    A texture of 44*3 + 56*-1 = 76

Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, which happens to be the best score possible given these ingredients. If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?


"""

import itertools

def proportions_generation(nb_total_teaspoons, nb_total_ingredients):
    '''
    le nombre total de cuillères doit être réparti dans les différents ingrédients.
    Chaque possibilité s'appelle proportion.
    On stocke toutes les possibilités dans une collection appelée "proportions".
    '''
    proportions = set() # évite les doublons
    for i in itertools.combinations(range(nb_total_teaspoons+1), nb_total_ingredients): # Pas toutes les combinaisons possibles mais toujours des valeurs croissantes entre les items 
        if sum(i) == nb_total_teaspoons: # On ne garde que les combinaisons possibles 
            if i not in proportions: # inutile de travailler pour rien
                for p in itertools.permutations(i): # on accède à toutes les permutations d'ingrédients de cette combinaison possible
                    proportions.add(p)
    return proportions

def score_calculation(ingredients, proportion):  # ingredients est une liste de dicos et proportion un tuple
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    j = 0 # permet d'accéder à la proportion de cette ingredient dans le tuple
    for i in ingredients:
        capacity += (proportion[j] * i['capacity'])
        durability += (proportion[j] * i['durability'])
        flavor += (proportion[j] * i['flavor'])
        texture += (proportion[j] * i['texture'])
        j += 1
    
    if capacity < 0 or durability < 0 or flavor < 0 or texture < 0:
        score = 0
    else:
        score = capacity * durability * flavor * texture
    
    return score

def resolve_problem(data_file):
    data = open(data_file, 'r')
    data_list = data.read().splitlines()
    
    ingredients = []
    
    for line in data_list:
        properties = line.split()
        # cleaning terminal caracters in the input (: or ,)
        properties[0] = properties[0][:-1]
        properties[2] = properties[2][:-1]
        properties[4] = properties[4][:-1]
        properties[6] = properties[6][:-1]
        properties[8] = properties[8][:-1]
        
        ingredient = {'name': properties.pop(0)}
        
        i = 0
        
        while i != len(properties):
            ingredient[properties[i]] = int(properties[i+1])
            i+= 2
        
        ingredients.append(ingredient)
    
    #print(ingredients)
    
    
    total_teaspoons = 100
    
    proportions = proportions_generation(total_teaspoons, len(ingredients))
    
    #print(proportions)
    
    #print(len(proportions))
    
    scores = []
    
    for p in proportions:
        score = score_calculation(ingredients, p)
        scores.append(score)
        '''
        if score > 0:
            print(p, score)
        '''
    
    return max(scores)


print()
print('Test : ', resolve_problem('day_15_test'))
print()
print('Mon input : ', resolve_problem('day_15_my_input'))
print()


