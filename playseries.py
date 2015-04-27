#I think this should conceivably work for any team, in any league, in any year
def playSeries(team1, team2, numGames):
    
    from random import seed, random
    from math import pow

    #teams 1 and 2 are Team objects, numGames is the maximum series length

    #threshold set from a Bill James-style pythagorean formula, based on points from Team objects
    gameThresh = pow(team1.points, 2) / (pow(team1.points, 2) + pow(team2.points, 2))

    winsNeeded = (numGames + 1)/2

    team1Wins = 0
    team2Wins = 0
    currentGame = 1

    #seed() #seed the random number generator

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