#Team class used by every league
#teamData input array:
# [SEED] [NAME] [WINS] [LOSSES] [TIES (optional)]
class Team:

    def __init__(self, teamData):

        global divisions

        self.seed = int(teamData[0])
        self.name = teamData[1]
        self.wins = int(teamData[2]) #regular season wins (can also be runs scored, goals scored, etc.)
        self.losses = int(teamData[3]) #regular season losses (can also be runs allowed, goals against, etc.)

        if len(teamData) > 4:
            self.ties = int(teamData[4]) #ties, if applicable (overtime losses in hockey)


        [self.conference, self.division] = divisions[self.name].split(' ') #calling it "conference" but it's the AL or NL

        self.points = self.wins #in MLB, a team's "points" is given by regular season wins

        #print self.seed, self.name, self.wins, self.losses, self.conference, self.division


#MAIN FUNCTION

from sys import argv

# leagueType = argv[1]
# leagueYear = argv[2]
# fileName = argv[3]
# numTrials = int(argv[4])

fileName = argv[1]
numTrials = int(argv[2])


from mlb2014 import divisions2014 as setDivisions
from mlb2014 import format2014 as runPlayoffs

global divisions
divisions = setDivisions()

# print divisions

seedsAL = {}
seedsNL = {}

totalWins = {}


with open(fileName, 'r') as teamsFile:


    for line in teamsFile:

        #lines are given as [SEED] - [NAME] - [WINS] - [LOSSES] - [TIES (optional)]
        teamData = line.split(' - ')
        #print teamData

        currentTeam = Team(teamData)

        if currentTeam.conference == 'AL':
            seedsAL[currentTeam.seed] = currentTeam
        elif currentTeam.conference == 'NL':
            seedsNL[currentTeam.seed] = currentTeam

        totalWins[currentTeam.name] = 0

    # print "AL seeds: ", seedsAL
    # print "NL seeds: ", seedsNL


# SIMULATING A FUCKLOAD OF PLAYOFFS
for i in range(0,numTrials):

    winner = runPlayoffs(seedsAL, seedsNL)

    totalWins[winner.name] += 1



# PRINTING RESULTS
print "\nChampionships (%d Trials):\n" % numTrials 

for team in totalWins:

    print team, totalWins[team], "\n"














