def setDivisions(year):

    if year >= 2013:

        divisions = {
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

    elif year >= 2005:

        divisions = {
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

            'Angels': 'AL West',
            'Athletics': 'AL West',
            'Mariners': 'AL West',
            'Rangers': 'AL West',

            'Braves': 'NL East',
            'Marlins': 'NL East',
            'Mets': 'NL East',
            'Phillies': 'NL East',
            'Nationals': 'NL East',

            'Astros': 'NL Central',
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

    elif year >= 1998:

        divisions = {
            'Orioles': 'AL East',
            'Red Sox': 'AL East',
            'Yankees': 'AL East', 
            'Devil Rays': 'AL East',
            'Blue Jays': 'AL East',

            'White Sox': 'AL Central',
            'Indians': 'AL Central',
            'Tigers': 'AL Central',
            'Royals': 'AL Central',
            'Twins': 'AL Central',

            'Angels': 'AL West',
            'Athletics': 'AL West',
            'Mariners': 'AL West',
            'Rangers': 'AL West',

            'Braves': 'NL East',
            'Marlins': 'NL East',
            'Mets': 'NL East',
            'Phillies': 'NL East',
            'Expos': 'NL East',

            'Astros': 'NL Central',
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

    elif year >= 1994:

        divisions = {
            'Orioles': 'AL East',
            'Red Sox': 'AL East',
            'Yankees': 'AL East', 
            'Blue Jays': 'AL East',
            'Tigers': 'AL East',

            'White Sox': 'AL Central',
            'Indians': 'AL Central',
            'Royals': 'AL Central',
            'Twins': 'AL Central',
            'Brewers': 'AL Central',

            'Angels': 'AL West',
            'Athletics': 'AL West',
            'Mariners': 'AL West',
            'Rangers': 'AL West',

            'Braves': 'NL East',
            'Marlins': 'NL East',
            'Mets': 'NL East',
            'Phillies': 'NL East',
            'Expos': 'NL East',

            'Astros': 'NL Central',
            'Cubs': 'NL Central',
            'Reds': 'NL Central',
            'Pirates': 'NL Central',
            'Cardinals': 'NL Central',

            'Rockies': 'NL West',
            'Dodgers': 'NL West',
            'Padres': 'NL West',
            'Giants': 'NL West'
            }

    elif year < 1994:

        print "sorry, but I haven't set divisions before 1994 yet"
        exit()


    return divisions


def setSeeds(teamsList, divisions, year):

    #find each division champ for both AL and NL

    #find next 2 best teams in each league (wild card teams)

    #in each league, wild card teams become seeds 4-5 and do the 1-game playoff

    #other division champs are ranked 1-2-3 w/ relevant tiebreakers(?)

    #then it's a typical 1-4 and 2-3 playoff for AL and NL, right?

    if year >= 2012:
        numWildCardTeams = 2
    elif yea >= 1994:
        numWildCardTeams = 1


    #rankedTeams = sorted(teamsList, key=lambda Team: Team.points, reverse=True)
    #sorts all teams on points, highest first

    qualifyingTeams = {'AL East': [], 'AL Central': [], 'AL West': [], 'AL': [], 'NL East': [], 'NL Central': [], 'NL West': [], 'NL': []}

    for thisTeam in teamsList:
        #if there's no division champ yet, or thisTeam has the same number of wins as the current champ, append it
        if (len(qualifyingTeams[thisTeam.division]) == 0) or (thisTeam.points == qualifyingTeams[thisTeam.division][0].points):
            qualifyingTeams[thisTeam.division].append(thisTeam)
            print 'added ', thisTeam.name, ' to ', thisTeam.division

        #if thisTeam is better than the current division 'champ', replace it and move the previous one to the wild card list
        elif thisTeam.points > qualifyingTeams[thisTeam.division][0].points:
            for team in qualifyingTeams[thisTeam.division]:
                qualifyingTeams[thisTeam.conference].append(team) #append current division champ(s) to the wild card list    
            
            qualifyingTeams[thisTeam.division] = []
            qualifyingTeams[thisTeam.division].append(thisTeam)
            print 'added ', thisTeam.name, ' to ', thisTeam.division
        
        #if thisTeam is worse than the current division champ, append it to the wild card list
        elif thisTeam.points < qualifyingTeams[thisTeam.division][0].points:
            qualifyingTeams[thisTeam.conference].append(thisTeam)
            print 'added ', thisTeam.name, ' to ', thisTeam.conference, ' wild card'


    for league in ['AL', 'NL']:

        qualifyingTeams[league].sort(key=lambda Team: Team.points, reverse=True)

        for i in range(numWildCardTeams,len(qualifyingTeams[league])):
            if qualifyingTeams[league][i].points < qualifyingTeams[league][i-1].points:
                for j in range(i,len(qualifyingTeams[league])):
                    removedTeam = qualifyingTeams[league].pop()
                    print 'removed ', removedTeam.name, ' from ', league, ' WC list'

                break

        print league, ' wild card teams are: '
        for team in qualifyingTeams[league]:
            print team.name


    # need to trim the wild card teams down
    # if a one-game playoff is needed to break ties, I'll do it as part of runPlayoffs

    # for team in qualifyingTeams['AL']:
    #     print team.name, team.points
    # for team in qualifyingTeams['NL']:
    #     print team.name, team.points

    return qualifyingTeams



# format starting in 2012
def runPlayoffs(seedsAL, seedsNL, year):

    from playseries import playSeries

    lenWC = 1
    lenDS = 5
    lenCS = 7
    lenWS = 7

    if year >= 2012:

        # WILD CARD GAMES
        wcAL = playSeries(seedsAL[4], seedsAL[5], lenWC)
        wcNL = playSeries(seedsNL[4], seedsNL[5], lenWC)

    elif year >= 1994:
        wcAL = seedsAL[4]
        wcNL = seedsNL[4]

    else:
        print "Sorry, I haven't programmed this format yet :("
        exit()

    # DIVISION SERIES
    alcs1 = playSeries(seedsAL[1], wcAL, lenDS)
    alcs2 = playSeries(seedsAL[2], seedsAL[3], lenDS)

    nlcs1 = playSeries(seedsNL[1], wcNL, lenDS)
    nlcs2 = playSeries(seedsNL[2], seedsNL[3], lenDS)

    # LEAGUE CHAMPIONSHIP SERIES
    champAL = playSeries(alcs1, alcs2, lenCS)
    champNL = playSeries(nlcs1, nlcs2, lenCS)

    # WORLD SERIES
    champWS = playSeries(champAL, champNL, lenWS)

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
