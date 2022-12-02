"""

--- Part Two ---

The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

    In the first round, your opponentt will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
    In the second round, your opponentt will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
    In the third round, you will defeat your opponentt's Scissors with Rock for a score of 1 + 6 = 7.

Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?


"""

def my_shape(opponent_shape, score): #opponent_shape is a string containing "ABC" (Rock-Paper-Sissors)
    if opponent_shape == 'A': # Rock
        if score == 0: # loose
            return 'sissors'
        elif score == 3: # draw
            return 'rock'
        elif score == 6: # win
            return 'paper'
    elif opponent_shape == 'B': # Paper
        if score == 0: # loose
            return 'rock'
        elif score == 3: # draw
            return 'paper'
        elif score == 6: # win
            return 'sissors'
    elif opponent_shape == 'C': # Sissors
        if score == 0: # loose
            return 'paper'
        elif score == 3: # draw
            return 'sissors'
        elif score == 6: # win
            return 'rock'

def calculating_score(match): # match is a string containing "ABC XYZ" (Rock-Paper-Sissors Loose-Draw-Win)
    match_list = match.split()
    
    score = 0
    opponent_shape = match_list[0]
    outcome = match_list[1]
    
    #print('opponent_shape', opponent_shape)
    
    if outcome == 'X': # loose
        pass
    elif outcome == 'Y': # draw
        score += 3
    elif outcome == 'Z': # win
        score += 6
    
    #print('my_shape', my_shape(opponent_shape, score))
    
    if my_shape(opponent_shape, score) == 'rock':
        score += 1
    elif my_shape(opponent_shape, score) == 'paper':
        score += 2
    elif my_shape(opponent_shape, score) == 'sissors':
        score += 3
    
    #print(score)
    
    return score
    

def resolve_problem(data_file):
    data = open(data_file, 'r')
    data_list = data.read().splitlines()
    
    total_score = 0
    
    for line in data_list:
        total_score += calculating_score(line)
        #print(total_score)
    
    return total_score


print(resolve_problem('day_02_test_input'))
print(resolve_problem('day_02_my_input'))

