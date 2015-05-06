#In the NFL, due to team name concerns, Washington is essentially referred to as "The Washington Washington"
# "year" for NFL refers to the regular season year (aka "league year") even though the Super Bowl occurs in the winter of the following year.

def setDivisions(year):

    if year >= 2002:

        divisions = {
            'Patriots': 'AFC East',
            'Bills': 'AFC East',
            'Dolphins': 'AFC East',
            'Jets': 'AFC East',

            'Steelers': 'AFC North',
            'Bengals': 'AFC North',
            'Ravens': 'AFC North',
            'Browns': 'AFC North',

            'Colts': 'AFC South',
            'Texans': 'AFC South',
            'Jaguars': 'AFC South',
            'Titans': 'AFC South',

            'Broncos': 'AFC West',
            'Chiefs': 'AFC West',
            'Chargers': 'AFC West',
            'Raiders': 'AFC West',

            'Cowboys': 'NFC East',
            'Eagles': 'NFC East',
            'Giants': 'NFC East',
            'Washington': 'NFC East',

            'Packers': 'NFC North',
            'Lions': 'NFC North',
            'Vikings': 'NFC North',
            'Bears': 'NFC North',

            'Panthers': 'NFC South',
            'Saints': 'NFC South',
            'Falcons': 'NFC South',
            'Buccaneers': 'NFC South',

            'Seahawks': 'NFC West',
            'Cardinals': 'NFC West',
            '49ers': 'NFC West',
            'Rams': 'NFC West'
            }

    elif year < 2002:
        print "sorry, but I haven't set divisions before 2002 yet :("
        exit()

    return divisions


# format starting in 2002
def runPlayoffs(seedsAFC, seedsNFC, year):

    from playseries import playSeries

    if year >= 2002:

        # WILD CARD GAMES
        wcA1 = playSeries(seedsAFC[3], seedsAFC[6], 1)
        wcA2 = playSeries(seedsAFC[4], seedsAFC[5], 1)
        wcN1 = playSeries(seedsNFC[3], seedsNFC[6], 1)
        wcN2 = playSeries(seedsNFC[4], seedsNFC[5], 1)

    else:
        print "Sorry, I haven't programmed this format yet :("
        exit()

    # DIVISIONAL ROUND
    
    if wcA1.seed > wcA2.seed:
        afc1 = playSeries(seedsAFC[1], wcA1, 1)
        afc2 = playSeries(seedsAFC[2], wcA2, 1)
    else:
        afc1 = playSeries(seedsAFC[1], wcA2, 1)
        afc2 = playSeries(seedsAFC[2], wcA1, 1)

    if wcN1.seed > wcN2.seed:
        nfc1 = playSeries(seedsNFC[1], wcN1, 1)
        nfc2 = playSeries(seedsNFC[2], wcN2, 1)
    else:
        nfc1 = playSeries(seedsNFC[1], wcN2, 1)
        nfc2 = playSeries(seedsNFC[2], wcN1, 1)

    # CONFERENCE CHAMPIONSHIPS
    champAFC = playSeries(afc1, afc2, 1)
    champNFC = playSeries(nfc1, nfc2, 1)

    # SUPER BOWL
    champSB = playSeries(champAFC, champNFC, 1)

    # #Print statements
    # print "\nWild Card winners:"
    # print wcA1.name
    # print wcA2.name
    # print wcN1.name
    # print wcN2.name, "\n"

    # print "Divisional winners:"
    # print afc1.name
    # print afc2.name
    # print nfc1.name
    # print nfc2.name, "\n"

    # print "Conference champions:"
    # print champAFC.name
    # print champNFC.name, "\n"

    # print "Super Bowl champions:"
    # print champSB.name, "\n"

    return champSB