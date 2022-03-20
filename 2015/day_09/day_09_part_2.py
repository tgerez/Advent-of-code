"""

--- Part Two ---

The next year, just to show off, Santa decides to take the route with the longest distance instead.

He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route?


"""

import networkx as nx
import matplotlib.pyplot as plt

import math
import random

def all_single_paths(l):
    '''
    Dans un graphe, j'appelle "single path" un chemin qui passe une seule fois par chaque noeud.
    Le parcourt d'une liste de tous les noeuds représente un chemin unique qui passe par tous les noeuds.
    Permuter des noeuds dans cette liste, puis parcourir cette nouvelle liste donne un nouveau chemin unique.
    Il y a autant de chemins uniques entre des noeuds que la factorielle du nombre de noeuds.
    
    La fonction all_single_paths prend en argument un tuple qui représente les noeuds,
    et renvoie un ensemble qui contient autant de tuples que de chemins uniques possibles
    '''
    
    paths = set()
    paths.add(l)
    while len(paths) < math.factorial(len(l)):
        t = list(l)
        random.shuffle(t)
        # Un set doit contenir des objets hashables, donc j'imagine imuables.
        # paths ne peut donc pas contenir une liste, mais un tuple oui.
        t = tuple(t)
        paths.add(t)
    return paths


def resolve_problem(data_file):
    data = open(data_file, 'r')
    data_in_list = data.read().splitlines()
    
    # On crée un graph non dirigé, avec une seule arrête possible entre deux noeuds
    G = nx.Graph()
    
    for line in data_in_list:
        distances = line.split()
        from_city = distances[0]
        to_city = distances[2]
        distance = int(distances[4])
        
        G.add_edge(from_city, to_city, length = distance)
        
    afficher_graph = input('Voulez-vous afficher le graphique ? (oui/non) ')
    if afficher_graph == 'oui':
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True)
        nx.draw_networkx_edge_labels(G, pos)
        print('\n\nFermez la fenêtre graphique pour continuer le programme.')
        plt.show()
    
    
    print('\n\nVeuillez patienter (traitement de l\'input...)\n\n')
    
    nodes = tuple(G.nodes)
    
    # All possibles single paths through every node
    all_possibles_single_paths = all_single_paths(nodes)
    
    edges = list(G.edges.data())
    
    distances = []
    
    for path in all_possibles_single_paths:
        distance = 0
        for i, city in enumerate(path): # city are nodes of the graph
            if i < len(path) - 1: # le dernier noeud n'est relié à rien
                
                city_1 = city
                city_2 = path[i+1]
                
                step = 0
                
                for data in edges:
                    if city_1 == data[0]:
                        if city_2 == data[1]:
                            step = int(data[2]['length'])
                    elif city_2 == data[0]:
                        if city_1 == data[1]:
                            step = int(data[2]['length'])
                
                
                distance += step
        
        distances.append(distance)
    
    # Seul endroit du code où on va charger le programme de la partie 1 pour traiter la partie 2
    print('\nLe chemin de longueur minimale qui passe par toutes les villes a pour distance : ', max(distances), '\n')
    
    

choix = input('Voulez vous lancer :\n\
1 : les données test\n\
2 : les données d\'input complètes\n')

if choix == '1':
    resolve_problem('day_09_test')
elif choix == '2':
    resolve_problem('day_09_my_input')
else:
    print('choix inconnu')





