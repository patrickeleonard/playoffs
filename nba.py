def setPastChamps():

    pastChamps = {
        2014: 'Spurs',
        2013: 'Heat',
        2012: 'Heat',
        2011: 'Mavericks',
        2010: 'Lakers',
        2009: 'Lakers',
        2008: 'Celtics',
        2007: 'Spurs',
        2006: 'Heat',
        2005: 'Spurs',
        2004: 'Pistons',
        2003: 'Spurs',
        2002: 'Lakers',
        2001: 'Lakers',
        2000: 'Lakers',
        1999: 'Spurs',
        1998: 'Bulls',
        1997: 'Bulls',
        1996: 'Bulls',
        1995: 'Rockets',
        1994: 'Rockets',
        1993: 'Bulls',
        1992: 'Bulls',
        1991: 'Bulls'
    }

    return pastChamps

def setDivisions(year):

    if year >= 2015:
        # Charlotte Bobcats changed name to Hornets
        divisions = {

            'Celtics': 'Eastern Atlantic',
            'Nets': 'Eastern Atlantic',
            'Knicks': 'Eastern Atlantic',
            '76ers': 'Eastern Atlantic',
            'Raptors': 'Eastern Atlantic',

            'Bulls': 'Eastern Central',
            'Cavaliers': 'Eastern Central',
            'Pistons': 'Eastern Central',
            'Pacers': 'Eastern Central',
            'Bucks': 'Eastern Central',

            'Hawks': 'Eastern Southeast',
            'Hornets': 'Eastern Southeast',
            'Heat': 'Eastern Southeast',
            'Magic': 'Eastern Southeast',
            'Wizards': 'Eastern Southeast',

            'Nuggets': 'Western Northwest',
            'Thunder': 'Western Northwest',
            'Timberwolves': 'Western Northwest',
            'Trail Blazers': 'Western Northwest',
            'Jazz': 'Western Northwest',

            'Warriors': 'Western Pacific',
            'Clippers': 'Western Pacific',
            'Lakers': 'Western Pacific',
            'Suns': 'Western Pacific',
            'Kings': 'Western Pacific',

            'Mavericks': 'Western Southwest',
            'Rockets': 'Western Southwest',
            'Grizzlies': 'Western Southwest',
            'Pelicans': 'Western Southwest',
            'Spurs': 'Western Southwest'
            }

    elif year >= 2014:
        # New Orleans changed name to Pelicans
        # Nets moved from New Jersey to Brooklyn starting in "2013" season
        divisions = {

            '76ers': 'Eastern Atlantic',
            'Celtics': 'Eastern Atlantic',
            'Knicks': 'Eastern Atlantic',
            'Nets': 'Eastern Atlantic',
            'Raptors': 'Eastern Atlantic',

            'Bucks': 'Eastern Central',
            'Bulls': 'Eastern Central',
            'Cavaliers': 'Eastern Central',
            'Pacers': 'Eastern Central',
            'Pistons': 'Eastern Central',

            'Hawks': 'Eastern Southeast',
            'Heat': 'Eastern Southeast',
            'Bobcats': 'Eastern Southeast',
            'Magic': 'Eastern Southeast',
            'Wizards': 'Eastern Southeast',

            'Jazz': 'Western Northwest',
            'Nuggets': 'Western Northwest',
            'Thunder': 'Western Northwest',
            'Timberwolves': 'Western Northwest',
            'Trail Blazers': 'Western Northwest',
            
            'Clippers': 'Western Pacific',
            'Kings': 'Western Pacific',
            'Lakers': 'Western Pacific',
            'Suns': 'Western Pacific',
            'Warriors': 'Western Pacific',

            'Grizzlies': 'Western Southwest',
            'Mavericks': 'Western Southwest',
            'Pelicans': 'Western Southwest',
            'Rockets': 'Western Southwest',
            'Spurs': 'Western Southwest'
        }

    elif year >= 2009:
        # SuperSonics changed name to Thunder following 07-08 season
        divisions = {

            '76ers': 'Eastern Atlantic',
            'Celtics': 'Eastern Atlantic',
            'Knicks': 'Eastern Atlantic',
            'Nets': 'Eastern Atlantic',
            'Raptors': 'Eastern Atlantic',

            'Bucks': 'Eastern Central',
            'Bulls': 'Eastern Central',
            'Cavaliers': 'Eastern Central',
            'Pacers': 'Eastern Central',
            'Pistons': 'Eastern Central',

            'Bobcats': 'Eastern Southeast',
            'Hawks': 'Eastern Southeast',
            'Heat': 'Eastern Southeast',
            'Magic': 'Eastern Southeast',
            'Wizards': 'Eastern Southeast',

            'Jazz': 'Western Northwest',
            'Nuggets': 'Western Northwest',
            'Thunder': 'Western Northwest',
            'Timberwolves': 'Western Northwest',
            'Trail Blazers': 'Western Northwest',
            
            'Clippers': 'Western Pacific',
            'Kings': 'Western Pacific',
            'Lakers': 'Western Pacific',
            'Suns': 'Western Pacific',
            'Warriors': 'Western Pacific',

            'Grizzlies': 'Western Southwest',
            'Mavericks': 'Western Southwest',
            'Hornets': 'Western Southwest',
            'Rockets': 'Western Southwest',
            'Spurs': 'Western Southwest'
        }

    elif year >= 2005:
        # Divisions realigned starting in the 04-05 season
        divisions = {

            '76ers': 'Eastern Atlantic',
            'Celtics': 'Eastern Atlantic',
            'Knicks': 'Eastern Atlantic',
            'Nets': 'Eastern Atlantic',
            'Raptors': 'Eastern Atlantic',

            'Bucks': 'Eastern Central',
            'Bulls': 'Eastern Central',
            'Cavaliers': 'Eastern Central',
            'Pacers': 'Eastern Central',
            'Pistons': 'Eastern Central',

            'Bobcats': 'Eastern Southeast',
            'Hawks': 'Eastern Southeast',
            'Heat': 'Eastern Southeast',
            'Magic': 'Eastern Southeast',
            'Wizards': 'Eastern Southeast',

            'Jazz': 'Western Northwest',
            'Nuggets': 'Western Northwest',
            'SuperSonics': 'Western Northwest',
            'Timberwolves': 'Western Northwest',
            'Trail Blazers': 'Western Northwest',
            
            'Clippers': 'Western Pacific',
            'Kings': 'Western Pacific',
            'Lakers': 'Western Pacific',
            'Suns': 'Western Pacific',
            'Warriors': 'Western Pacific',

            'Grizzlies': 'Western Southwest',
            'Mavericks': 'Western Southwest',
            'Hornets': 'Western Southwest',
            'Rockets': 'Western Southwest',
            'Spurs': 'Western Southwest'
        }

    elif year < 2005:
        print "sorry, but I haven't set divisions before 2005 yet :("
        exit()

    return divisions


# "year" for NBA refers to the year in which the playoffs occur (not the year the season starts)
# we can debate the merits of this decision, but it is what it is
def runPlayoffs(seedsEastern, seedsWestern, year):

    from playseries import playSeries

    if year >= 2003:
    #Current format has existed since the 2002-03 season
    #NBA playoffs' bracket structure is based on the way Wikipedia presents the playoff bracket

        #FIRST ROUND
        ES1 = playSeries(seedsEastern[1], seedsEastern[8], 7)
        ES2 = playSeries(seedsEastern[4], seedsEastern[5], 7)
        ES3 = playSeries(seedsEastern[3], seedsEastern[6], 7)
        ES4 = playSeries(seedsEastern[2], seedsEastern[7], 7)

        WS1 = playSeries(seedsWestern[1], seedsWestern[8], 7)
        WS2 = playSeries(seedsWestern[4], seedsWestern[5], 7)
        WS3 = playSeries(seedsWestern[3], seedsWestern[6], 7)
        WS4 = playSeries(seedsWestern[2], seedsWestern[7], 7)

        #CONFERENCE SEMIFINALS
        EF1 = playSeries(ES1, ES2, 7)
        EF2 = playSeries(ES3, ES4, 7)

        WF1 = playSeries(WS1, WS2, 7)
        WF2 = playSeries(WS3, WS4, 7)

        #CONFERENCE FINALS
        EC = playSeries(EF1, EF2, 7)
        WC = playSeries(WF1, WF2, 7)

        #NBA FINALS
        champFinals = playSeries(EC, WC, 7)

    else:
        print "Sorry, I haven't programmed this format yet :("
        exit()

    # #PRINT STATEMENTS
    # print '\nFirst Round winners:'
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

    # print '\n NBA Finals winner:'
    # print champFinals.name, '\n'

    return champFinals

