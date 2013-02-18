import random
#Set up our constants
teams = {"Red":None, "Blue":None}
positions = ["Catcher", " Pitcher", " 1st Base",
 " 2nd Base", " 3rd Base", " Short Stop",
 " R. fielder", " L. fielder", " C. fielder"]

Field = ["First Base", "Second Base", "Third Base", "Home plate"]
class batter():
    average = 0
    def __str__(self):
        return str(self.average)
    def __init__(self):
        self.Position = 0
        average = random.random()

        #Keep the batting average below .399 
        #but above .200 to reflect professional baseball
        if average > 0.350:
            self.average = average / 3.0
        elif average < 0.200:
            self.average = average + 0.200 
        else:
            self.average = average
    def doSwings(self):
        #Taking a bit of a short cut.
        #Calculating the possiblity of getting a hit in 3 swings.
        #Depending on the difference, we can know how well the batter did.
        return self.average * 2.8 - random.random()


class team():
    score = 0
    def __init__(self, team):
        self.players = team
    
class inning():
    def __init__(self, teamToBat):
        self.isInningTop = True
        self.numOuts = 0
        self.team = teamToBat
        self.Bases = [0, 0, 0]
    def RunBatting(self):
        batters = self.team.players
        #print "Batters inside inning:" + str(batters)
        def RespondToHit(member, advance):
            print member
            print "Responding to advance of " + str(advance)
            if advance <= 0:
                return
            member.position = advance - 1
            #Get all the batters that are on base
            onBase = [p for p in self.Bases if isinstance(p, batter)]
            onBase.append(member)
            #print onBase
            #Advance each batter
            for player in onBase:
                player.Position += advance
            #Score and remove finsihed runners
                print [i.Position for i in onBase]
            for player in onBase:
                if player.Position > 2:
                    self.team.score += 1
                    #print player.Position - advance
                    self.Bases[player.Position - advance] = 0
                    
            #Anyone that is left gets on base
            #print self.Bases
            #print onBase
            for player in onBase:
                if player.position <= 2:
                    #print player.position
                    #print self.Bases
                    self.Bases[player.Position] = player
            #Debug printing the bases
            #print "Bases:" + str(self.Bases)
        
        batter.RespondToHit = RespondToHit
        for member in batters:
            results = member.doSwings()
            print "Results:"+str(results)
            if results > 1:
                member.RespondToHit(4)
            elif results > 0.8:
                member.RespondToHit(3)
            elif results > 0.4:
                member.RespondToHit(2)
            elif results > 0.0:
                member.RespondToHit(1)
            else:
                self.numOuts += 1
                
        del batter.RespondToHit
def runGame():
    getInnings = lambda team: [inning(team) for i in range(1, 9)]
    batters = [batter() for i in range(0,10)]
    #print batters
    teamA = team(batters)
    innings = getInnings(teamA)
    for i in innings:
        i.RunBatting()
    
runGame()
