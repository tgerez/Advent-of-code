"""

--- Day 9: All in a Single Night ---

Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141

The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982

The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?

"""

import networkx as nx
import matplotlib.pyplot as plt

import math
import random

# Notons que le module itertools contient la fonction permutations()
# non utilisée ici mais qui aurait permi de sévèrement alléger le code

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
    
    print('\nLe chemin de longueur minimale qui passe par toutes les villes a pour distance : ', min(distances), '\n')
    
    

choix = input('Voulez vous lancer :\n\
1 : les données test\n\
2 : les données d\'input complètes\n')

if choix == '1':
    resolve_problem('day_09_test')
elif choix == '2':
    resolve_problem('day_09_my_input')
else:
    print('choix inconnu')





