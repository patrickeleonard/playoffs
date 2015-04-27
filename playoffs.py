from sys import argv
from random import seed, random
from math import pow

fileName = argv[1]
numTrials = int(argv[2])


#I think this should conceivably work for any team, in any league, in any year
def playSeries(team1, team2, numGames):
    
    #teams 1 and 2 are Team objects, numGames is the maximum series length

    #threshold set from a Bill James-style pythagorean formula, based on points from Team objects
    gameThresh = pow(team1.points, 2) / (pow(team1.points, 2) + pow(team2.points, 2))

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


#scoped to overall MLB level
class Team:

    def __init__(self, teamData):

        global divisions

        self.seed = int(teamData[0])
        self.name = teamData[1]
        self.rwins = int(teamData[2]) #regular season wins
        self.rlosses = int(teamData[3]) #regular season losses

        if len(teamData) > 4:
            self.rties = int(teamData[4]) #ties, if applicable (overtime losses in hockey)


        [self.league, self.division] = divisions[self.name].split(' ')

        self.points = self.rwins #in MLB, a team's "points" is given by regular season wins

        #print self.seed, self.name, self.wins, self.losses, self.league, self.division


def runPlayoffs(seedsAL, seedsNL):

    # WILD CARD GAMES
    wcAL = playSeries(seedsAL[4], seedsAL[5], 1)
    wcNL = playSeries(seedsNL[4], seedsNL[5], 1)

    # DIVISION SERIES
    alcs1 = playSeries(seedsAL[1], wcAL, 5)
    alcs2 = playSeries(seedsAL[2], seedsAL[3], 5)

    nlcs1 = playSeries(seedsNL[1], wcNL, 5)
    nlcs2 = playSeries(seedsNL[2], seedsNL[3], 5)

    # LEAGUE CHAMPIONSHIP SERIES
    champAL = playSeries(alcs1, alcs2, 7)
    champNL = playSeries(nlcs1, nlcs2, 7)

    # WORLD SERIES
    champWS = playSeries(champAL, champNL, 7)

    # Print statements
    # print "\nWild Card winners:"
    # print wcAL.name
    # print wcNL.name, "\n"

    # print "ALDS winners:"
    # print alcs1.name
    # print alcs2.name, "\n"

    # print "NLDS winners:"
    # print nlcs1.name
    # print nlcs2.name, "\n"

    # print "League champions:"
    # print champAL.name
    # print champNL.name, "\n"

    # print "World Series champions:"
    # print champWS.name, "\n"

    return champWS


#MAIN FUNCTION

from mlb2014 import setDivisions

global divisions
divisions = setDivisions()

# print divisions

seedsAL = {}
seedsNL = {}

totalWins = {}


with open(fileName, 'r') as teamsFile:


    for line in teamsFile:

        #teamData is [SEED] [NAME] [WINS] [LOSSES]
        teamData = line.split(' ')
        #print teamData

        currentTeam = Team(teamData)

        if currentTeam.league == 'AL':
            seedsAL[currentTeam.seed] = currentTeam
        elif currentTeam.league == 'NL':
            seedsNL[currentTeam.seed] = currentTeam

        totalWins[currentTeam.name] = 0

    # print "AL seeds: ", seedsAL
    # print "NL seeds: ", seedsNL


# SIMULATING A FUCKLOAD OF PLAYOFFS
for i in range(0,numTrials):

    winner = runPlayoffs(seedsAL, seedsNL)

    totalWins[winner.name] += 1



# PRINTING RESULTS
print "\nWorld Series Championships (%d Trials):\n" % numTrials 

for team in totalWins:

    print team, totalWins[team], "\n"














