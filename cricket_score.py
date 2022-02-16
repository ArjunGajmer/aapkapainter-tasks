"""
Write a code that prints out individual scores of two players in a game of cricket 
where score is given as runs per ball in an array. In a game of cricket a person changes strike if he scores an odd number, 
and keeps strike with him if he scores an even number. No need to consider changing strike after every 6 balls or an over """

def extract_individual_score(arr):
    total_player_one_runs = 0
    total_player_two_runs = 0
    
    first_player_strike = True
    for runs in arr:
        if first_player_strike:
            total_player_one_runs += runs
        else:
            total_player_two_runs += runs
        if runs&1:
            first_player_strike = not first_player_strike
    return total_player_one_runs, total_player_two_runs
            
    
assert extract_individual_score([1, 2]) == (1, 2)

assert extract_individual_score([2, 2]) == (4, 0)

assert extract_individual_score([1,2,3,2,1]) == (4, 5)

assert extract_individual_score([1,2,2,2,1]) == (1, 7)

assert extract_individual_score([1,2,1,2,1]) == (4, 3)
