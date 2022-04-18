"""

--- Day 14: Reindeer Olympics ---

This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy. Santa would like to know which of his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state.

For example, suppose you have the following Reindeer:

    Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
    Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.

After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km. On the 12th second, both reindeer are resting. They continue to rest until the 138th second, when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.

In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point). So, in this situation, Comet would win (if the race ended at 1000 seconds).

Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled?



"""


def race(reindeer, race_lenght):
    # reindeer tuple :
    # (nom, vitesse, temps de vol, temps de repos)
    #   0       1         2               3
    
    t_cycle = reindeer[2] + reindeer[3]
    nb_cycles_entiers = race_lenght // t_cycle
    t_reste = race_lenght % t_cycle
    
    d = nb_cycles_entiers * reindeer[1] * reindeer[2]
    
    if t_reste >= reindeer[2]:
        d += reindeer[1] * reindeer[2]
    else : # t_reste < temps de vol
        d += reindeer[1] * t_reste
    
    return d

def resolve_problem(data_file, race_lenght):
    data = open(data_file, 'r')
    data_list = data.read().splitlines()
    
    reindeers = []
    
    # attributions
    for line in data_list:
        line = line.split()
        # (nom, vitesse, temps de vol, temps de repos)
        reindeers.append((line[0], int(line[3]), int(line[6]), int(line[13])))
    
    reindeers_distances = {}
    
    for r in reindeers:
        reindeers_distances[r[0]] = race(r, race_lenght)
        
    print(f'Après {race_lenght} secondes de course, le tableau des scores est :')
    print(reindeers_distances)
    
    distance_gagnante = max(reindeers_distances.values())
    
    print(f'La distance gagnante est {distance_gagnante} km.')


resolve_problem('day_14_my_input', 2503)



