from sys import argv
from random import seed, random
from math import pow


fileName = argv[1]


class Team:

    def __init__(self, teamData):
        self.seed = int(teamData[0])
        self.name = teamData[1]
        self.rwins = int(teamData[2])
        self.rlosses = int(teamData[3])

        [self.league, self.division] = DivisionsMLB[self.name].split(' ')

        #print self.seed, self.name, self.wins, self.losses, self.league, self.division




DivisionsMLB = {
    'Orioles': 'AL East',
    'Red Sox': 'AL East',
    'Yankees': 'AL East', 
    'Rays': 'AL East',
    'Blue Jays': 'AL East',

    'White Sox': 'AL Central',
    'Indians': 'AL Central',
    'Tigers': 'AL Central',
    'Royals': 'AL Central',
    'Twins': 'AL Central',

    'Astros': 'AL West',
    'Angels': 'AL West',
    'Athletics': 'AL West',
    'Mariners': 'AL West',
    'Rangers': 'AL West',

    'Braves': 'NL East',
    'Marlins': 'NL East',
    'Mets': 'NL East',
    'Phillies': 'NL East',
    'Nationals': 'NL East',

    'Cubs': 'NL Central',
    'Reds': 'NL Central',
    'Brewers': 'NL Central',
    'Pirates': 'NL Central',
    'Cardinals': 'NL Central',

    'Diamondbacks': 'NL West',
    'Rockies': 'NL West',
    'Dodgers': 'NL West',
    'Padres': 'NL West',
    'Giants': 'NL West'
    }


def playSeries(team1, team2, numGames):
#teams 1 and 2 are Team objects, numGames is the maximum series length

    gameThresh = pow(team1.rwins, 2) / (pow(team1.rwins, 2) + pow(team2.rwins, 2))

    winsNeeded = (numGames + 1)/2

    team1Wins = 0
    team2Wins = 0
    currentGame = 1

    seed() #seed the random number generator

    while currentGame <= numGames:

        if random() <= gameThresh:
            team1Wins += 1
        else:
            team2Wins += 1

        if team1Wins == winsNeeded:
            return team1
        elif team2Wins == winsNeeded:
            return team2

        currentGame += 1





#MAIN FUNCTION
with open(fileName, 'r') as teamsFile:

    teamsList = []
    seedsAL = {}
    seedsNL = {}

    for line in teamsFile:

        #teamData is [SEED] [NAME] [WINS] [LOSSES]
        teamData = line.split(' ')
        #print teamData

        currentTeam = Team(teamData)

        if currentTeam.league == 'AL':
            seedsAL[currentTeam.seed] = currentTeam
        elif currentTeam.league == 'NL':
            seedsNL[currentTeam.seed] = currentTeam

        teamsList.append(currentTeam)

    # DEBUGGING

    # for team in teamsList:
    #     print team.name

    # print "AL: ", seedsAL
    # print "NL: ", seedsNL

    # for i in range(1,6):
    #     print "%d:" % i, seedsAL[i].name
    # for i in range(1,6):
    #     print "%d:" % i, seedsNL[i].name


    # WILD CARD GAMES
    wcAL = playSeries(seedsAL[4], seedsAL[5], 1)
    wcNL = playSeries(seedsNL[4], seedsNL[5], 1)

    print "\nWild Card winners:"
    print wcAL.name
    print wcNL.name, "\n"


    # DIVISION SERIES

    alcs1 = playSeries(seedsAL[1], wcAL, 5)
    alcs2 = playSeries(seedsAL[2], seedsAL[3], 5)

    nlcs1 = playSeries(seedsNL[1], wcNL, 5)
    nlcs2 = playSeries(seedsNL[2], seedsNL[3], 5)

    print "ALDS winners:"
    print alcs1.name
    print alcs2.name, "\n"

    print "NLDS winners:"
    print nlcs1.name
    print nlcs2.name, "\n"

    champAL = playSeries(alcs1, alcs2, 7)
    champNL = playSeries(nlcs1, nlcs2, 7)

    print "League champions:"
    print champAL.name
    print champNL.name, "\n"

    champWS = playSeries(champAL, champNL, 7)

    print "World Series champions:"
    print champWS.name, "\n"













