#scoped for just 2014 ()
def divisions2014():

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

    return divisions

# format starting in 2012
def format2014(seedsAL, seedsNL):

    from playseries import playSeries

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
