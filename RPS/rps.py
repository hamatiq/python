
from random import randrange
import json
import sys

# map = {
#     1:"sizors",
#     2:"paper",
#     3:"rock"
# }
class player:
    def __init__(self,name,games,wins,looses,ties):
        self.name = name
        self.games = games
        self.wins = wins
        self.looses = looses 
        self.ties = ties

    # def __init__(self):
    #     self.id = 0
    #     self.games = 0
    #     self.wins = 0
    #     self.looses = 0 
    #     self.ties = 0

    def get_games(self):
        return self.games
    def get_wins(self):
        return self.wins
    def get_losses(self):
        return self.looses
    def add_a_win(self):
        self.wins = self.wins+1
        self.games = self.games+1
    def add_a_loss(self):
        self.looses= self.looses+1
        self.games = self.games+1
    def add_a_tie(self):
        self.ties = self.ties +1
        self.games = self.games+1    
    def print_stats(self):
        print(self.name+"\n"+'games: ' +str(self.games)+ ' , wins: '+str(self.wins)+ ' , losses: '+str(self.looses)+ ' , ties: '+str(self.ties))
    def get_player_json(self):
        return (json.dumps({'name': self.name, 'games':self.games, 'w' : self.wins, 'l':self.looses,'t':self.ties}))

def load_json_data(exists,p):
    # if player is not appart of data adds it to data other wise update data
    if (exists == False):
        data.append(eval(p.get_player_json()))
        # print (eval(p.get_player_json()))
    else:
        for i in range (len(data)):
            d = data[i]
            if (d['name'] == name):
                data[i]  = eval(p.get_player_json())

    # update json file
    file = open('player_data.json','w')
    json.dump(data,file)
    file.close()
    # print (data)


def rps (p):
    map = {1:"rock",2:'paper',3:'sizors'}
    while True:
        i = input("Round "+str(p.get_games()+1)+":\n\n1. Rock\n2. Paper\n3. Scissors\n\nWhat will it be?")
        i = int(i)
        rand = randrange(1,3)
    
        if (i >=1 and i <=3):
            if (i == rand-1 or (i== 3 and rand == 1)):
                print ("You chose "+map[i]+" The computer chose "+map[rand]+". lose!")
                p.add_a_loss()
                break
            elif (i == rand):
                print ("You chose "+map[i]+" The computer chose "+map[rand]+". You tie!")
                p.add_a_tie()
                break
            else:
                print ("You chose "+map[i]+" The computer chose "+map[rand]+". You win!")
                p.add_a_win()
                break
        else:
            print("invalid input")
            continue


# load results of previus games in 
file = open('player_data.json','r+')
data = json.load(file)
file.close
while(True):
    i = input("Welcome to Rock, Paper, Scissors!\n\n1. Start New Game\n2. Load Game\n3. Quit\n\nEnter choice:")

    if(i == '1'):
        name = input("What is your name? ")
        p = player(name,0,0,0,0)
        rps(p)
        while (True):
            
            i = input("What would you like to do?\n\n1. Play Again\n2. View Statistics\n3. Quit\n\nEnter choice:")
            if (i == '1'):
                rps(p)
            elif (i == '2'):
                p.print_stats()
            elif(i == '3'):
                load_json_data(False,p)
                break
            else:
                print ("invalid input")
        break


    elif (i == '2'):
        # determin "id"
        name = input("What is your name? ")
        # print (type(data))
        exists = False
        # finds the player name
        for d in data:
            # print(type(d))
            if (d['name'] == name):
                p = player(d['name'],d['games'],d['w'],d['l'],d['t'])
                exists = True
                break

        if (exists == True):
            print("Welcome back "+ name+". Let’s play!")
            while (True):
                i = input("What would you like to do?\n\n1. Play\n2. View Statistics\n3. Quit\n\nEnter choice:")
                if (i == '1'):
                    rps(p)
                elif (i == '2'):
                    p.print_stats()
                elif(i == '3'):
                    break
                else:
                    print ("invalid input")
                    continue
        else:
            print (name+", your game could not be found.")
    elif (i == '3'):
        break
    else:
        print("invvalid input try again!")















