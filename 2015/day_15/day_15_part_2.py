"""

--- Part Two ---

Your cookie recipe becomes wildly popular! Someone asks if you can make another recipe that has exactly 500 calories per cookie (so they can use it as a meal replacement). Keep the rest of your award-winning process the same (100 teaspoons, same ingredients, same scoring system).

For example, given the ingredients above, if you had instead selected 40 teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds to 100), the total calorie count would be 40*8 + 60*3 = 500. The total score would go down, though: only 57600000, the best you can do in such trying circumstances.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make with a calorie total of 500?


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
    calories = 0
    j = 0 # permet d'accéder à la proportion de cette ingredient dans le tuple
    for i in ingredients:
        capacity += (proportion[j] * i['capacity'])
        durability += (proportion[j] * i['durability'])
        flavor += (proportion[j] * i['flavor'])
        texture += (proportion[j] * i['texture'])
        calories += (proportion[j] * i['calories'])
        j += 1
    
    if capacity < 0 or durability < 0 or flavor < 0 or texture < 0 or calories != 500:
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



