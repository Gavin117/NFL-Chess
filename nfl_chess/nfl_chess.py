import csv
import time

def get_data(file):
    csvfile = open(file,newline='')
    reader = csv.reader(csvfile)
    header = next(reader)
    data = [row for row in reader]
    return data

def get_start(file):
    data = get_data(file)
    team1 = [row[4] for row in data]
    team2 = [row[6] for row in data]
    teams = team1+team2
    teams= set(teams)
    start = []
    for team in teams:
        start.append([team,1000])
    return start
    

def elo(playera,playerb):    
    awins = 1/(1 + 10**((playerb-playera)/400))
    print(awins)


def get_rating(name):
    for team in ratings:
        if name in team:
            return team[1]

def update_winner(win,lose):
    winner = get_rating(win)
    loser = get_rating(lose)
    wins = 1/(1 + 10**((loser-winner)/400))
    update = (winner+32*(1-wins))
    return update

def update_loser(lose,win):
    loser = get_rating(lose)
    winner = get_rating(win)
    wins = 1/(1 + 10**((winner-loser)/400))
    update = (loser-32*(1-wins))
    return update
    
    
    
def process_schedule(file):
    data = get_data(file)
    winners = [row[4] for row in data]
    losers = [row[6] for row in data]
    x = list(zip(winners,losers))
    return x


filename = 'win_loss_.csv'

ratings = get_start(filename)

games_list = process_schedule(filename)

for game in games_list:
    #print(game)

    for team in ratings:
        if game[0] in team:
            winner = get_rating(game[0])
            loser = get_rating(game[1])
            team[1] = update_winner(winner, loser)
            #print(team[1])
        if game[1] in team:
            winnr = get_rating(game[0])
            losr = get_rating(game[1])
            team[1] = update_loser(losr, winnr)
            #print(team[1])
            
ratings.sort(key= lambda x: x[1])

for result in reversed(ratings):
    print(result)
    





