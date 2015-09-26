def setPastChamps():

    pastChamps = {
        2014: 'Giants',
        2013: 'Red Sox',
        2012: 'Giants',
        2011: 'Cardinals',
        2010: 'Giants',
        2009: 'Yankees',
        2008: 'Phillies',
        2007: 'Red Sox',
        2006: 'Cardinals',
        2005: 'White Sox',
        2004: 'Red Sox',
        2003: 'Marlins',
        2002: 'Angels',
        2001: 'Diamondbacks',
        2000: 'Yankees',
        1999: 'Yankees',
        1998: 'Yankees',
        1997: 'Marlins',
        1996: 'Yankees',
        1995: 'Braves',
        1994: False
    }

    return pastChamps


def setDivisions(year):

    if year >= 2013:

        divisions = {

            'All': ['AL', 'AL East', 'AL Central', 'AL West', 'NL', 'NL East', 'NL Central', 'NL West'],

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

            'All': ['AL', 'AL East', 'AL Central', 'AL West', 'NL', 'NL East', 'NL Central', 'NL West'],

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

            'All': ['AL', 'AL East', 'AL Central', 'AL West', 'NL', 'NL East', 'NL Central', 'NL West'],

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

            'All': ['AL', 'AL East', 'AL Central', 'AL West', 'NL', 'NL East', 'NL Central', 'NL West'],

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


def setBettingOdds(year):

    if year == 2014:

        bettingOdds = {

            'Nationals': 4.5,
            'Angels': 4.5,
            'Dodgers': 4.5,
            'Orioles': 7.0,
            'Tigers': 7.0,
            'Cardinals': 7.0,
            'Athletics': 10.0,

        # couldn't find odds for Royals, Giants, or Pirates but they're worse than Athletics'
            'Royals': 11.0,
            'Giants': 11.0,
            'Pirates': 11.0
        }



def setSeeds(teamsList, divisions, year):

    if year >= 2012:
        numWildCardTeams = 2
    elif year >= 1994:
        numWildCardTeams = 1


    #rankedTeams = sorted(teamsList, key=lambda Team: Team.points, reverse=True)
    #sorts all teams on points, highest first
    qualifiers = {}

    for division in divisions['All']:
        qualifiers[division] = []

    #qualifiers = {'AL East': [], 'AL Central': [], 'AL West': [], 'AL': [], 'NL East': [], 'NL Central': [], 'NL West': [], 'NL': []}

    for thisTeam in teamsList:
        #if there's no division champ yet, or thisTeam has the same number of wins as the current champ, append it
        if (len(qualifiers[thisTeam.division]) == 0) or (thisTeam.points == qualifiers[thisTeam.division][0].points):
            qualifiers[thisTeam.division].append(thisTeam)
            #print 'added ', thisTeam.name, ' to ', thisTeam.division

        #if thisTeam is better than the current division 'champ', replace it and move the previous one to the wild card list
        elif thisTeam.points > qualifiers[thisTeam.division][0].points:
            for team in qualifiers[thisTeam.division]:
                qualifiers[thisTeam.conference].append(team) #append current division champ(s) to the wild card list    
                #print 'moved ', team.name, ' to wild card'

            qualifiers[thisTeam.division] = [] #clear out the division champ(s) to make room for the new one

            qualifiers[thisTeam.division].append(thisTeam)
            #print 'added ', thisTeam.name, ' to ', thisTeam.division
        
        #if thisTeam is worse than the current division champ, append it to the wild card list
        elif thisTeam.points < qualifiers[thisTeam.division][0].points:
            qualifiers[thisTeam.conference].append(thisTeam)
            #print 'added ', thisTeam.name, ' to ', thisTeam.conference, ' wild card'


    for league in ['AL', 'NL']:

        qualifiers[league].sort(key=lambda Team: Team.points, reverse=True)

        for i in range(numWildCardTeams,len(qualifiers[league])):
            if qualifiers[league][i].points < qualifiers[league][i-1].points:
                for j in range(i,len(qualifiers[league])):
                    removedTeam = qualifiers[league].pop()
                    #print 'removed ', removedTeam.name, ' from ', league, ' WC list'

                break

        # print league, ' wild card teams are: '
        # for team in qualifiers[league]:
        #     print team.name

    #if a one-game playoff is needed to break ties, I'll do it as part of runPlayoffs

    # print '\n', 'Playoff Qualifying Teams: \n'
    # for key in qualifiers.keys():
    #     for team in qualifiers[key]:
    #         print key, team.name, team.points


    return qualifiers



def runPlayoffs(qualifiers, year, format):

    from playseries import playSeries

    #parse the playoff format and set round lengths
    temp = format.split('-')
    format = []
    for roundLen in temp:
        format.append(int(roundLen))

    [lenWC, lenDS, lenCS, lenWS] = format

    # DEFAULT LENGTHS: (2012-present)
    # lenWC = 1
    # lenDS = 5
    # lenCS = 7
    # lenWS = 7    

    if year >= 2012:
        numWildCardTeams = 2
    elif year >= 1994:
        numWildCardTeams = 1

    #TIEBREAKING: THIS PROCESS IS ANNOYING AND COMPLEX BUT UNFORTUNATELY NECESSARY ON RARE OCCASIONS
    for division in qualifiers.keys():
        if division != 'AL' and division != 'NL':
            if len(qualifiers[division]) == 2:
                winner = playSeries(qualifiers[division][0], qualifiers[division][1], 1) #one-game playoff to settle the division

                if winner == qualifiers[division][0]:
                    loser = qualifiers[division][1]
                else:
                    loser = qualifiers[division][0]

                qualifiers[division].remove(loser)
                qualifiers[loser.conference].append(loser) #add loser to the wild card pool

            #I'll wait to add 3-team tiebreakers until I need to, because fuck it.
            #So far MLB has never had a 3-way tie.

    for league in ['AL', 'NL']:
        qualifiers[league].sort(key=lambda Team: Team.points, reverse=True)
        #print 'there are ', len(qualifiers[league]), 'WC teams in the ', league, '.'
        while len(qualifiers[league]) > numWildCardTeams:
            if qualifiers[league][numWildCardTeams].points == qualifiers[league][numWildCardTeams-1].points:
                loser = playSeries(qualifiers[league][numWildCardTeams-1], qualifiers[league][numWildCardTeams], 1)
                #it's technically the winner, but it's a one-game playoff and they have the same number of wins so fuck it.
                #print 'loser is ', loser.name
                qualifiers[league].remove(loser)
            else:
                qualifiers[league].pop()


    # print '\n', 'Updated Qualifying Teams: \n'
    # for key in qualifiers.keys():
    #     for team in qualifiers[key]:
    #         print key, team.name, team.points


    #WILD CARD
    if year >= 2012:
        wcAL = playSeries(qualifiers['AL'][0], qualifiers['AL'][1], lenWC)
        wcNL = playSeries(qualifiers['NL'][0], qualifiers['NL'][1], lenWC)
    elif year >= 1994:
        wcAL = qualifiers['AL'][0]
        wcNL = qualifiers['NL'][0]
    else:
        print "Sorry, I haven't programmed this format yet :("
        exit()

    #BUILDING THE BRACKET

    seedsAL = []
    seedsNL = []

    for division in qualifiers.keys():
        if division != 'AL' and division != 'NL':
            if qualifiers[division][0].conference == 'AL':
                seedsAL.append(qualifiers[division][0])
            elif qualifiers[division][0].conference == 'NL':
                seedsNL.append(qualifiers[division][0])

    seedsAL.sort(key=lambda Team: Team.points, reverse=True)
    seedsNL.sort(key=lambda Team: Team.points, reverse=True)

    if year >= 2012:
        champWS = playSeries(playSeries(playSeries(seedsAL[0], wcAL, lenDS), playSeries(seedsAL[1], seedsAL[2], lenDS), lenCS), playSeries(playSeries(seedsNL[0], wcNL, lenDS), playSeries(seedsNL[1], seedsNL[2], lenDS), lenCS), lenWS)
    elif year >= 1994:
        if (wcAL.division == seedsAL[0].division) or ((wcAL.division == seedsAL[1].division) and (seedsAL[0].points == seedsAL[1].points)):
            alcs1 = playSeries(seedsAL[1], wcAL, lenDS)
            alcs2 = playSeries(seedsAL[0], seedsAL[2], lenDS)
        else:
            alcs1 = playSeries(seedsAL[0], wcAL, lenDS)
            alcs2 = playSeries(seedsAL[1], seedsAL[2], lenDS)

        if (wcNL.division == seedsNL[0].division) or ((wcNL.division == seedsNL[1].division) and (seedsNL[0].points == seedsNL[1].points)):
            nlcs1 = playSeries(seedsNL[1], wcNL, lenDS)
            nlcs2 = playSeries(seedsNL[0], seedsNL[2], lenDS)
        else:
            nlcs1 = playSeries(seedsNL[0], wcNL, lenDS)
            nlcs2 = playSeries(seedsNL[1], seedsNL[2], lenDS)

        champWS = playSeries(playSeries(alcs1, alcs2, lenCS), playSeries(nlcs1, nlcs2, lenCS), lenWS)

    
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
