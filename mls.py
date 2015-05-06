def setDivisions(year):
#MLS is weird because all the teams have different conventions
#there's a lot of realignment but I haven't put in a lot of the changes yet. Stay tuned.

    if year >= 2015:
    # new for 2015:
        # Columbus Crew renamed to Columbus Crew SC
        # Expansion teams New York City FC and Orlando City SC added
        # Houston Dynamo moved to Western conference
        # Chivas USA contracted
        divisions = {
            'Chicago Fire': 'Eastern',
            'Columbus Crew SC': 'Eastern',
            'D.C. United': 'Eastern',
            'Montreal Impact': 'Eastern',
            'New England Revolution': 'Eastern',
            'New York City FC': 'Eastern',
            'New York Red Bulls': 'Eastern',
            'Orlando City SC': 'Eastern',
            'Philadelphia Union': 'Eastern',
            'Toronto FC': 'Eastern',

            'Colorado Rapids': 'Western',
            'FC Dallas': 'Western',
            'Houston Dynamo': 'Western',
            'LA Galaxy': 'Western',
            'Portland Timbers': 'Western',
            'Real Salt Lake': 'Western',
            'San Jose Earthquakes': 'Western',
            'Seattle Sounders FC': 'Western',
            'Sporting Kansas City': 'Western',
            'Vancouver Whitecaps FC': 'Western'
            }


    elif year >= 2012:

        divisions = {
            'Chicago Fire': 'Eastern',
            'Columbus Crew': 'Eastern',
            'D.C. United': 'Eastern',
            'Houston Dynamo': 'Eastern',
            'Montreal Impact': 'Eastern',
            'New England Revolution': 'Eastern',
            'New York Red Bulls': 'Eastern',
            'Philadelphia Union': 'Eastern',
            'Sporting Kansas City': 'Eastern',
            'Toronto FC': 'Eastern',

            'Chivas USA': 'Western',
            'Colorado Rapids': 'Western',
            'FC Dallas': 'Western',
            'LA Galaxy': 'Western',
            'Portland Timbers': 'Western',
            'Real Salt Lake': 'Western',
            'San Jose Earthquakes': 'Western',
            'Seattle Sounders FC': 'Western',
            'Vancouver Whitecaps FC': 'Western'
            }

    else:
        print "sorry, but I haven't set divisions that far back yet"
        exit()


    return divisions

# format starting in 2012
def runPlayoffs(seedsEast, seedsWest, year):
#soccer is weird because of the home-and-home format and the away-goals tiebreaker, among other things

    from playseries import playSeries

    if year >= 2015:

        # KNOCKOUT ROUND
        wcE1 = playSeries(seedsEast[3], seedsEast[6], 1)
        wcE2 = playSeries(seedsEast[4], seedsEast[5], 1)

        wcW1 = playSeries(seedsWest[3], seedsWest[6], 1)
        wcW2 = playSeries(seedsWest[4], seedsWest[5], 1)

        # CONFERENCE SEMIFINALS
        # in the future this can use a max() function to determine who plays whom, once team seed structure is better
        if wcE1.seed > wcE2.seed:
            EF1 = playSeries(seedsEast[1], wcE1, 1)
            EF2 = playSeries(seedsEast[2], wcE2, 1)
        else:
            EF1 = playSeries(seedsEast[1], wcE2, 1)
            EF2 = playSeries(seedsEast[2], wcE1, 1)

        if wcW1.seed > wcW2.seed:
            WF1 = playSeries(seedsWest[1], wcW1, 1)
            WF2 = playSeries(seedsWest[2], wcW2, 1)
        else:
            WF1 = playSeries(seedsWest[1], wcW2, 1)
            WF2 = playSeries(seedsWest[2], wcW1, 1)
            

    elif year >= 2011:

        # KNOCKOUT ROUND
        wcEast = playSeries(seedsEast[4], seedsEast[5], 1)
        wcWest = playSeries(seedsWest[4], seedsWest[5], 1)

        # CONFERENCE SEMIFINALS
        EF1 = playSeries(seedsEast[1], wcEast, 1)
        EF2 = playSeries(seedsEast[2], seedsEast[3], 1)

        WF1 = playSeries(seedsWest[1], wcWest, 1)
        WF2 = playSeries(seedsWest[2], seedsWest[3], 1)

    else:
        print "Sorry, I haven't programmed this format yet :("
        exit()



    # CONFERENCE FINALS
    champEast = playSeries(EF1, EF2, 1)
    champWest = playSeries(WF1, WF2, 1)

    # MLS CUP FINAL
    champMLS = playSeries(champEast, champWest, 1)

    # #Print statements
    # print "\nKnockout winners:"
    # print wcEast.name
    # print wcWest.name, "\n"

    # print "Conference Semifinal winners:"
    # print EF1.name
    # print EF2.name
    # print WF1.name
    # print WF2.name, "\n"

    # print "Conference champions:"
    # print champEast.name
    # print champWest.name, "\n"

    # print "MLS Cup champions:"
    # print champMLS.name, "\n"

    return champMLS
