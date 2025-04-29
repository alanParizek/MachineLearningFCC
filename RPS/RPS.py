import random
from itertools import cycle

STATES = ["abbey", "kris", "others"]
state_cycle = cycle(STATES)

def player(prev_play, opponent_history=[], counter=[0], my_history=[], state=[], play_order=[{
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0,
          }]):
    if prev_play == '':
        prev_play = "R"
    opponent_history.append(prev_play)
    counter[0] += 1
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    ## "continuity factor (???), a way of me knowing if the oponent is playing against my last play"
    c_f = 0
    wins = 0
    if not state:
        state.append("abbey")
    if not my_history:
        my_history.append("R")
    ##para abbey

    last_two = "".join(my_history[-2:])
    if len(last_two) == 2:
        play_order[0][last_two] += 1
    potential_plays = [
        my_history[-1] + "R",
        my_history[-1] + "P",
        my_history[-1] + "S",
    ]
    sub_order = {
        k: play_order[0][k]
        for k in potential_plays if k in play_order[0]
    }
    prediction = max(sub_order, key=sub_order.get)[-1:]
    ideal_counter_response = {'P': 'R', 'R': 'S', 'S': 'P'}

    #para kris
    last_ten_op = opponent_history[-10:]
    last_ten_mine = my_history[-10:]
    
    for i in range (len(last_ten_op) - 1):
        if(last_ten_mine[i] == ideal_response[last_ten_op[i]]):
            wins += 1

    if(counter[0]%10 == 0 and wins < 6):
        state[0] = next(state_cycle)

    if(state[0] == "abbey"):
        guess = ideal_counter_response[prediction]
    elif(state[0] == "kris"):
        guess = ideal_counter_response[my_history[-1]]
    else:    
        ##para quincy y mrughesh 
        if prev_play == '':
            prev_play = "R"
        guess = ideal_response[prev_play]
    
    my_history.append(guess)
    return guess