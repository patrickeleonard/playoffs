#Team class used by every league
#teamData input array:
#GENERIC: [SEED] - [NAME] - [WINS] - [LOSSES] - [TIES (optional)]
#MLB/NBA: [NAME] [WINS]
class Team:

    def __init__(self, leagueType, teamData):

        global divisions

        # PARSING INPUT DATA, SETTING SEEDS
        # currently MLB is done by the setSeeds() algorithm, others aren't yet
        # right now others are hard coded because that's easier to get up and running
        # eventually this will be done by a league- and year-specific algorithm
        if leagueType == 'mlb' or leagueType == 'nba':
            self.name = teamData[0]
            self.wins = int(teamData[1])
        else:
            if leagueType == 'nhl':
                self.seed = teamData[0]
            else:
                self.seed = int(teamData[0])

            self.name = teamData[1] #currently just using names - hometowns/locations aren't relevant right now
            self.wins = int(teamData[2]) #regular season wins (can also be runs scored, goals scored, etc.)
            self.losses = int(teamData[3]) #regular season losses (can also be runs allowed, goals against, etc.)

            if len(teamData) > 4:
                self.ties = int(teamData[4]) #ties, if applicable (overtime losses in hockey)
            else:
                self.ties = 0

        # SETTING CONFERENCE AND DIVISION
        if leagueType == 'mls':
            self.conference = divisions[self.name]
        else:
            self.division = divisions[self.name]
            self.conference = divisions[self.name].split(' ')[0]
            # self.justDivision = divisions[self.name].split(' ')[1]
            # [self.conference, self.justDivision] = divisions[self.name].split(' ') #calling it "conference" but it's the AL or NL

        # SETTING POINT-COUNTING SCHEME
        if leagueType == 'mlb' or leagueType == 'nba':
            self.points = self.wins
        elif leagueType == 'nfl' or leagueType == 'nhl':
            self.points = (2*self.wins) + (self.ties)
        elif leagueType == 'mls':
            self.points = (3*self.wins) + (self.ties)

        #print self.seed, self.name, self.wins, self.losses, self.conference, self.division

#################
# MAIN FUNCTION #
#################

# PARSING INPUT AND IMPORTING LEAGUE RULES
from sys import argv

arguments = {
    'league': 'mlb',
    'year': '2014',
    'trials': '100',
    'format': '1-5-7-7'
    }

#scriptName = argv[0]
if len(argv) > 1:
    for argItem in argv[1:len(argv)]:
        temp = argItem.split('=')
        arguments[temp[0]] = temp[1]


leagueType = arguments['league']
leagueYear = int(arguments['year'])
numTrials = int(arguments['trials'])
playoffFormat = arguments['format']


if leagueType == 'mlb' or leagueType == 'MLB':
    leagueType = 'mlb'
    from mlb import setDivisions, runPlayoffs, setSeeds

elif leagueType == 'nfl' or leagueType == 'NFL':
    leagueType = 'nfl'
    from nfl import setDivisions, runPlayoffs

elif leagueType == 'nba' or leagueType == 'NBA':
    leagueType = 'nba'
    from nba import setDivisions, runPlayoffs

elif leagueType == 'nhl' or leagueType == 'NHL':
    leagueType = 'nhl'
    from nhl import setDivisions, runPlayoffs

elif leagueType == 'mls' or leagueType == 'MLS':
    leagueType = 'mls'
    from mls import setDivisions, runPlayoffs

global divisions
divisions = setDivisions(leagueYear)

# print divisions


teamsList = []


seeds1 = {}
seeds2 = {}
totalWins = {}

# DOING STUFF WITH THE INPUT FILE
fileName = leagueType + '-' + str(leagueYear) + '.txt'

if leagueType == 'mlb':
    fileName = 'mlb-data/'+fileName

with open(fileName, 'r') as teamsFile:

    for line in teamsFile:

        #lines are given as [SEED] - [NAME] - [WINS] - [LOSSES] - [TIES (optional)]
        teamData = line.split(' - ')
        # print teamData

        currentTeam = Team(leagueType, teamData)

        teamsList.append(currentTeam)

        if leagueType != 'mlb':
            if currentTeam.conference == 'AFC' or currentTeam.conference == 'Eastern':
                seeds1[currentTeam.seed] = currentTeam
            elif currentTeam.conference == 'NFC' or currentTeam.conference == 'Western':
                seeds2[currentTeam.seed] = currentTeam

        totalWins[currentTeam.name] = 0

    # print "AL seeds: ", seeds1
    # print "NL seeds: ", seeds2

    # for team in teamsList:
    #     print team.name, team.points

    teamsList.sort(key=lambda Team: Team.name)

if leagueType == 'mlb':
    #print teamsList
    qualifiers = setSeeds(teamsList, divisions, leagueYear)

#SIMULATING A FUCKLOAD OF PLAYOFFS
for i in range(0,numTrials):
    if leagueType == 'mlb':
        winner = runPlayoffs(qualifiers, leagueYear, playoffFormat)
    else:
        winner = runPlayoffs(seeds1, seeds2, leagueYear)


    if leagueType == 'mlb':
        if winner.name == 'Expos':
            totalWins['Nationals'] += 1
        elif winner.name == 'Devil Rays':
            totalWins['Rays'] += 1
        else:
            totalWins[winner.name] += 1

    else:
        totalWins[winner.name] += 1



# PRINTING RESULTS
print "\n", leagueYear, leagueType, "championships (%d trials):\n" % numTrials 
for team in totalWins:
    if totalWins[team] > 0:
        print team, totalWins[team], "\n"














