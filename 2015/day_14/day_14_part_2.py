"""

--- Part Two ---

Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.

Instead, at the end of each second, he awards one point to the reindeer currently in the lead. (If there are multiple reindeer tied for the lead, they each get one point.) He keeps the traditional 2503 second time limit, of course, as doing otherwise would be entirely ridiculous.

Given the example reindeer from above, after the first second, Dancer is in the lead and gets one point. He stays in the lead until several seconds into Comet's second burst: after the 140th second, Comet pulls into the lead and gets his first point. Of course, since Dancer had been in the lead for the 139 seconds before that, he has accumulated 139 points by the 140th second.

After the 1000th second, Dancer has accumulated 689 points, while poor Comet, our old champion, only has 312. So, with the new scoring system, Dancer would win (if the race ended at 1000 seconds).

Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, how many points does the winning reindeer have?


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

def giving_points(reindeers_distances, reindeers_points):
    winning_dist = max(reindeers_distances.values())
    winners = []
    for r, d in reindeers_distances.items():
       if d == winning_dist:
           winners.append(r)
    for w in winners:
        reindeers_points[w] += 1
    

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
    reindeers_points = {}
    
    for r in reindeers:
        reindeers_points[r[0]] = 0
    
    
    timer = 1
    
    while timer <= race_lenght:
        
        for r in reindeers:
            reindeers_distances[r[0]] = race(r, timer)
        
        giving_points(reindeers_distances, reindeers_points)
        
        timer += 1
    
    
    
    print(f'Après {race_lenght} secondes de course, le tableau des scores est :')
    print(reindeers_points)
    
    points_gagnants = max(reindeers_points.values())
    
    print(f'Le score le plus élevé est {points_gagnants} points.')


resolve_problem('day_14_my_input', 2503)



