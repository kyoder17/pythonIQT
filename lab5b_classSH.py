"""
CPT Kyle Yoder
Lab5b Classes with Super hero
13 Sept 2008
"""
#create a class
class superHero:
    #create an istance of the superhero
    def __init__(self):
        self.name = "Cat-man"
        self.realname= "Michael Cera"
        self.powers = "cat like reflexes"
        self.color = "orange"

    #creates a print statement
    def printHero(self):
        print "\n"
        print "Our hero is {} but no one know he is really {}. ".format(self.name,self.realname)
        print "With powers like {} and a {} colored costum.\n".format(self.powers,self.color)

    #gets for getting all variables
    def getName():
        return self.name
    def getRealName():
        return self.realname
    def getPowers():
        return self.powers
    def getColor():
        return self.color
    
    #trying out sets for changing superhero name
    def setName(self,newName):
        self.name=newName



hero=superHero()
hero.printHero()
hero.setName("Dogman")
hero.printHero()