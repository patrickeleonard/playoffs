def setDivisions(year):
#NHL most recently realigned prior to the 2013-14 season

    if year >= 2014:

        divisions = {

            'Bruins': 'Eastern Atlantic',
            'Sabres': 'Eastern Atlantic',
            'Red Wings': 'Eastern Atlantic',
            'Panthers': 'Eastern Atlantic',
            'Canadiens': 'Eastern Atlantic',
            'Senators': 'Eastern Atlantic',
            'Lightning': 'Eastern Atlantic',
            'Maple Leafs': 'Eastern Atlantic',

            'Hurricanes': 'Eastern Metropolitan',
            'Blue Jackets': 'Eastern Metropolitan',
            'Devils': 'Eastern Metropolitan',
            'Islanders': 'Eastern Metropolitan',
            'Rangers': 'Eastern Metropolitan',
            'Flyers': 'Eastern Metropolitan',
            'Penguins': 'Eastern Metropolitan',
            'Capitals': 'Eastern Metropolitan',

            'Ducks': 'Western Pacific',
            'Coyotes': 'Western Pacific',
            'Flames': 'Western Pacific',
            'Oilers': 'Western Pacific',
            'Kings': 'Western Pacific',
            'Sharks': 'Western Pacific',
            'Canucks': 'Western Pacific',

            'Blackhawks': 'Western Central',
            'Avalanche': 'Western Central',
            'Stars': 'Western Central',
            'Wild': 'Western Central',
            'Predators': 'Western Central',
            'Blues': 'Western Central',
            'Jets': 'Western Central'

            }

    elif year < 2014:
        print "sorry, but I haven't set divisions before 2014 yet :("
        exit()

    return divisions


# "year" for NBA refers to the year in which the playoffs occur (not the year the season starts)
# we can debate the merits of this decision, but it is what it is
def runPlayoffs(seedsEastern, seedsWestern, year):

    from playseries import playSeries

    if year >= 2003:
    #Current format has existed since the 2013-14 season
    #NHL playoffs' bracket structure is based on the way Wikipedia presents the playoff bracket
    #The wild cards are still assigned manually - I haven't yet written an algorithm to do it automatically

        #FIRST ROUND
        ES1 = playSeries(seedsEastern['A1'], seedsEastern['WC2'], 7)
        ES2 = playSeries(seedsEastern['A2'], seedsEastern['A3'], 7)
        ES3 = playSeries(seedsEastern['M1'], seedsEastern['WC1'], 7)
        ES4 = playSeries(seedsEastern['M2'], seedsEastern['M3'], 7)

        WS1 = playSeries(seedsWestern['C1'], seedsWestern['WC2'], 7)
        WS2 = playSeries(seedsWestern['C2'], seedsWestern['C3'], 7)
        WS3 = playSeries(seedsWestern['P1'], seedsWestern['WC1'], 7)
        WS4 = playSeries(seedsWestern['P2'], seedsWestern['P3'], 7)

        #CONFERENCE SEMIFINALS
        EF1 = playSeries(ES1, ES2, 7)
        EF2 = playSeries(ES3, ES4, 7)

        WF1 = playSeries(WS1, WS2, 7)
        WF2 = playSeries(WS3, WS4, 7)

        #CONFERENCE FINALS
        EC = playSeries(EF1, EF2, 7)
        WC = playSeries(WF1, WF2, 7)

        #NBA FINALS
        champSC = playSeries(EC, WC, 7)

    else:
        print "Sorry, I haven't programmed this format yet :("
        exit()

    # #PRINT STATEMENTS
    # print '\nConference Quarterfinal winners:'
    # print ES1.name
    # print ES2.name
    # print ES3.name
    # print ES4.name, '\n'

    # print WS1.name
    # print WS2.name
    # print WS3.name
    # print WS4.name, '\n'

    # print '\n Conference Semifinal winners:'
    # print EF1.name
    # print EF2.name, '\n'

    # print WF1.name
    # print WF2.name, '\n'

    # print '\n Conference Final winners:'
    # print EC.name
    # print WC.name, '\n'

    # print '\nStanley Cup champions:'
    # print champSC.name, '\n'

    return champSC

