# File:    proj1.py
# Author:  Sarah Lunn
# Date:    10/16/2018
# Section: 05
# E-mail:  sarahl2@umbc.edu
# Description:
#    Text game (Project 1) based on Stranger Things [Love that show!]

##################################
#### DO NOT TOUCH THESE LINES ####
from random import randint, seed #
seed(100)                        #
##################################

# Constants for player/Demogorgon health
MAX_HEALTH = 100
MIN_HEALTH = 0

DEM_MAX_HEALTH = 300

#Constants for survival
SURVIVE_DAYS = 7
SURVIVE_DIST = 150

#Constants: lists of food & items
FOODS = ["Reese's Pieces", "Pop Rocks", "Ovaltine", "Wonder Bread", "Twinkies"]
ITEMS = ["Sword", "Bicycle", "Hi-C", "Heelys", "Walkman", "Laser Cannon", \
         "Rubber Band"]

#other constants
#menus
MAIN_MENU = ["View Inventory", "View Current Stats", "Eat an Eggo Waffle", \
             "Nothing Else"]
STAY_GO_MENU = ["Pack up your camp and go", "Stay where you are"]
FIGHT_MENU = ["Fight!", "Flail!", "Flee!"]
FOOD_MENU = ["Absolutely! You need the calories.", "NO WAY! GROSS!"]
INVEN_MENU = ["Equip", "Unequip", "I changed my mind"]

#items boost/damages
DEM_BASE_ATTACK = 20
FOOD_BOOST = ["30", "5", "15", "25", "30"]

BIKE_BOOST = 1.5
HEEL_BOOST = 1.25

HIC_DAMAGE = .5
WALKMAN_DAMAGE = .75

FLASHLIGHT_DAMAGE = 5
WALK_TALK_DAMAGE = 10
RUB_BAND_DAMAGE = 25
SWORD_DAMAGE = 50
LASER_CANNON_DAMAGE = 100

#Functions
# displayMenu()  Menu of option at start of day;
# input:   choices - what are your choices?
# outputs: none
def displayMenu(choices):
    index = 0
    print()
    print("Your options are:")
    while index < len(choices):
        print(str(index + 1), "-", str(choices[index]))
        index += 1
    print()

# getUserChoice()  check to make sure the menu option selected is valid
# input:      maxx: max menu option
# output:     valid number
def getUserChoice(maxx):
    
    newInt = int(input("Enter a choice: "))
    while newInt < 1 or newInt > maxx:
        print()
        print("That number is not allowed.")
        newInt = int(input("Enter a choice from the options above: "))
    return newInt

# checkStat()   You review/Print your current stats
# input:   playerHealth   total health count
#          totDist     total distance walked
#          item   any items you've equiped
# output:  none
def checkStat(playerHealth, totDist, item):
    print()
    print("Health:", str(playerHealth))
    print("Distance:", str(totDist))
    print("Equipped item:", str(item))
    
# eatEggo()  Eat an Eggo Waffle; gain 10 health [1x / day]
# input:     playerHealth: current overall health
# output:    playerHealth: updated health score
def eatEggo(playerHealth):

    if playerHealth < 90:
        playerHealth += 10
        print()
        print("You eat the Eggo Waffle. So bad, yet so good.")
        print("Your health increases by 10 points: to", str(playerHealth))

    elif playerHealth >= 90:
        print()
        print("You eat the Eggo Waffle. So bad, yet so good.")
        print("Your health increases and you're now back to full power.")
        playerHealth = MAX_HEALTH
        
    return playerHealth

# inventory()    check/list inventory
# input     inventory (list of what's in your backpack)
#           equip: what you're holding, if anything
# output    equip:    any item you decided to equip (use)
def inventory(inventory, item):
    print()
    print("Here is what your inventory looks like:")
    print(inventory)
    print()
    print("Do you want to equip an item?")
    displayMenu(INVEN_MENU)   
    userNum = getUserChoice(len(INVEN_MENU))

    #Equip
    if userNum == 1:
        displayMenu(inventory)   
        equipPick = getUserChoice(len(inventory))
        print()
        print("You have equipped your", inventory[equipPick - 1])
        equip = inventory[equipPick - 1]
        return equip

    #Unequip
    if userNum == 2:
        print()
        print("Your hands are now empty.")
        item = "N/A"
        return item

    #Do Nothing
    else:
        print()
        print("Ok, that's fine.")
        return item

# camp()   you stay at camp and nothing eventful happens
# input    none
# output   playerHealth: restore health to 100
def camp():
    print()
    print("You choose to stay where you are.")
    print("\'Cause, you know, it looks like rain...")
    print("...Maybe if you don't move, someone will come to save you...")
    print("You wait all day. No rescue to be seen. But no Demogorgon either.")
    print("And you are feeling rested and healthier. Back to 100%, in fact.")
    print("Win some; lose some.")
    playerHealth = 100
    return playerHealth

# fight()   you fight the monster
# input:       playerHealth: health, how long you can fight
#              backpack: items to potentially increase/decrease attacks
#              equip: if you have anything to attack with
# output:      playerHealth - remaining health as you run away
def fight(playerHealth, backpack, item):
    print()
    print("THE DEMOGORGON FINDS YOU!")
    print("It's face opens up like a flower to display rows of teeth.")
    print("It came here for a fight.")
    menuOpt = 0
    escaped = 0
    demDamage = calcDemDamage(backpack)
    youDamage = calcDamage(item)
    
    demHealth = DEM_MAX_HEALTH
    if "Hi-C" in backpack:
        demHealth /= 2

    while playerHealth > 0 and demHealth > 0 and escaped == 0:
        
        print()
        print("Your current health:", str(playerHealth))
        print("The Demogorgon's current health:", str(demHealth))
        displayMenu(FIGHT_MENU)
        menuOpt = getUserChoice(len(FIGHT_MENU))

        #fight
        if menuOpt == 1:
            if youDamage == 0:
                print("You strike the Demogorgon with your bare hands", \
                      "with seemingly no affect.")

            else:
                print("You strike the Demogorgon with your", str(item), \
                      "for", str(youDamage), "damage.")
                
            print()
            print("The Demogorgon strikes you back for", str(demDamage), \
                  "damage.")
            playerHealth -= demDamage
            demHealth -= youDamage
            
            if demHealth <= 0:
                print("Your attacks scare the Demogorgon away... for now.")

        #flail        
        elif menuOpt == 2:
            print()
            print("You're just not a great fighter.")
            print("You flail at the Demogorgon but nothing seems to land.")
            print()
            print("The Demogorgon lands a solid hit. You can't breath...")
            print("Everything goes black...")
            playerHealth = 0

        #escape?
        else:
            randNum = randint(1,10)
            #Successfully escape
            if randNum <= 3:
                escaped += 1
                print()
                print("You try to run away from the fight.")
                print("You are successful and live to die another day.")
            #Don't manage it
            else:
                print()
                print("You try escaping, but the Demogorgon catches you.")
                print("The hit knocks the wind out of you,", \
                      "but you manage to dodge the main impact.")
                playerHealth -= (demDamage / 2)
    return playerHealth


# calcDamage: how hard you hit
# input: EquipItem - what you're hitting with
# output: damage - what damage you do
def calcDamage(item):

    if "Flashlight" in item:
        damage = FLASHLIGHT_DAMAGE

    elif "Walkie Talkie" in item:
        damage = WALK_TALK_DAMAGE

    elif "Rubber Band" in item:
        damage = RUB_BAND_DAMAGE

    elif "Sword" in item:
        damage = SWORD_DAMAGE
        
    elif "Laser Cannon" in item:
        damage = LASER_CANNON_DAMAGE

    else:
        damage = 0

    return damage

# calcDemDamage: how much you get hit with
# input:  backpack - anything you have for protection?
# output: demDamage - how much you get hit back with
def calcDemDamage(backpack): 
    totAttack = DEM_BASE_ATTACK
    if "Walkman" in backpack:
        totAttack = totAttack * 3 / 4
    return totAttack


# walk()   You walk in the forest; nothing happens
# input:   playerHealth: how far do you go?
# output:  travDist: how far you go
def walk(playerHealth, backpack):

    print()
    print("You quickly pack up your camp.")
    print("You begin heading in the direction of the nearest town.")
    print()
    print("You walk all day. It's a nice day.")
    print("Probably would be nicer if you weren't running for your life.")
    travDist = distTrav(playerHealth, backpack)
    print("But you manage to walk", str(travDist), "miles", \
          "before it is too dark.")
    return travDist
    
# ditch()  You fall in a ditch; lose a day and travel half normal distance
# input:   playerHealth: how far do you go?
#          backpack: what are you carrying
# output:  travDist - how far you traveled b/c of ditch
def ditch(playerHealth, backpack):
    print()
    print("You fall in a ditch because you are busy", \
          "looking over your shoulder in fear.")
    print("It takes a whole extra day to climb out. " \
          "(How deep *is* this ditch??)")
    travDist = distTrav(playerHealth, backpack)
    travDist /= 2    
    print("But somehow, you manage to travel", str(travDist), "miles today.")
    return travDist           

# eat()   you find a backpack/food and decide to eat it (or not)
# input:       playerHealth - total health
#              foodIndex - what number in the food list you found
# output:      playerHealth - updated with +/-/0 based on food
def eat(playerHealth, foodIndex):

    print()
    print("Are you going to eat that?")
    displayMenu(FOOD_MENU)
    yesNo = getUserChoice(len(FOOD_MENU))

    #Yes plz
    if yesNo == 1:
        print()
        print("You devour the " + str(FOODS[foodIndex]) + ". Delicious.")

        if foodIndex == 0 or foodIndex == 1:
            print()
            print("You start to feel sick.")
            print("Those", FOODS[foodIndex], "didn't agree with your stomach.")
            print("Your health has decreased by", FOOD_BOOST[foodIndex], \
                  "points.")
            print("Worth it.")
            print()
            playerHealth -= int(FOOD_BOOST[foodIndex])

            if playerHealth < 0:
                playerHealth = 0

        else:
            print()
            if playerHealth >= 90:
                print("You feel your strength returning.", \
                      "You're now at full power.")
            else:
                print("Your health has increased by", FOOD_BOOST[foodIndex], \
                      "points.")

            playerHealth += int(FOOD_BOOST[foodIndex])
            if playerHealth > 100:
                playerHealth = 100

    #no way!
    else:
        print()
        print("You're right. You don't know where it's been.")
        print("You put the", FOODS[foodIndex], "back in the backpack", \
              "and keep walking.")

    return playerHealth

# findItem() works through scenario for when you find an item
# input:     backpack - what's in your inventory
# output:    none - backpack a list, so automatically updates
def findItem(backpack):    
    itemNum = randint(0,(len(ITEMS) - 1))
    print()
    print("You pass by an old shed and decide to go inside.")
    print("Something on the shelf catches your eye.")
    print("You reach up and grab the item. It's a", ITEMS[itemNum])
    print("The", ITEMS[itemNum], "has been added to your inventory.")
    print()

    if itemNum == 1 or itemNum == 3:
        print("The", ITEMS[itemNum], "will improve your traveling time.")

    elif itemNum == 0 or itemNum == 5 or itemNum == 6:
        print("The", ITEMS[itemNum], "will help you fight the Demogorgon.")

    else:
        print("The", ITEMS[itemNum], \
              "will help protect you from the Demogorgon.")

    print("You try not to think of it as stealing...")
    print("You'll return it as soon as you're safe.")
    backpack.append(ITEMS[itemNum])
    print()

# distTrav() calculates how far you've travelled that day
# input:     playerHealth: how far you can go without an item
#            backpack:  any items in your backpack
# output:    travDist:  How far you went today
def distTrav(playerHealth, backpack):
    
    travDist = ((playerHealth / 4) + 5)
    
    if "Bicycle" in backpack:
        travDist = travDist * 1.5
    elif "Heelys" in backpack:
        travDist = travDist * 1.25

    return travDist
    
# deadEnd()  You died
# input:     dayCount:   how many days you were in the woods
#            totDist:    how far you traveled
# output:    None
def deadEnd(dayCount, totDist, playerHealth, item):

    dist = SURVIVE_DIST - totDist

    print()
    print("OH NO! After walking for", str(dayCount), \
          "days, you sadly perished.")
    print("You were only", str(dist), "miles from safety.")
    print("Oh well... C'est la vie.")
    print()
    print("Final Stats:")
    checkStat(playerHealth, totDist, item)

# survived()  You made it! Yay!
# input:      dayCount:   how many days you were in the woods
#             totDist:    how far you traveled
# output:     None
def survived(dayCount, totDist, playerHealth, item): 
    print()
    print("CONGRATULATIONS!")
    print("You made it back to safety ... somehow.")
    print("Maybe hold off on any more camping for a while?")
    print("It took", str(dayCount), "days to go", str(totDist), "miles.")
    print()
    print("Final Stats:")
    checkStat(playerHealth, totDist, item)
    

def main():

    #Main variables:
    playerHealth = MAX_HEALTH
    totDist = 0
    dayCount = 1
    item = "N/A"
    backpack = ["Walkie Talkie", "Flashlight"]
    travDist = 0

    #Intro: You're camping, demagorgon escapes, good luck
    print()
    print("After miles and miles of hiking in the woods,", \
          "you finally setup your camp.")
    print("You decided to go camping on the wrong weekend.")
    print("You catch a clip of a distress call on your walkie talkie...")
    print("\tTHE DEMOGORGON HAS ESCAPED.\t\tRUN!")
    print()

    #main loop/game play
    while playerHealth > MIN_HEALTH and dayCount < SURVIVE_DAYS \
          and totDist < SURVIVE_DIST:

        print()
        print("The sun rises on day", str(dayCount), "in the forest.")
        ateEggo = 0
        menuOpt = 0

        #main menu/daily tasks: while menuOpt != 4, continue loop
        while menuOpt != len(MAIN_MENU):
            print()
            print("What would you like to do this morning?")
            displayMenu(MAIN_MENU)
            menuOpt = getUserChoice(len(MAIN_MENU))
            
            #You want to look at your inventory; maybe equip an item
            if menuOpt == 1:
                item = inventory(backpack, item)

            #You want to look at your stats    
            if menuOpt == 2:
                checkStat(playerHealth, totDist, item)

            #You want to eat an eggo    
            if menuOpt == 3:
                if ateEggo == 0:
                    ateEggo += 1
                    playerHealth = eatEggo(playerHealth)
                else:
                    print()
                    print("You can only eat one eggo per day.") 
                    print("You are trying to watch your weight.")
                    
        #menuOpt == 4: exit main menu, decide if you will stay or walk 
        print()
        print("The Demogorgon looms in the distance.")
        print("Do you leave your camp, or do you stay?")
        displayMenu(STAY_GO_MENU)
        stayGoPick = getUserChoice(len(STAY_GO_MENU))

        #random event section
        #Stay at camp events
        if stayGoPick == 2:
            randNum = randint(1,10)
            #if randint 1-7: fight the Demogorgon
            if randNum <= 7:
                travDist = distTrav(playerHealth, backpack)
                playerHealth = fight(playerHealth, backpack, item)
                if playerHealth > MIN_HEALTH:
                    print("You limp away, managing to go", travDist, \
                          "miles before it is too dark.")

            #if randint 8-10: uneventfully stay at camp
            else:
               playerHealth = camp()
               travDist = 0
               
        #Leave camp events
        if stayGoPick == 1:
            print()
            print("You quickly pack up your camp.")
            print("You begin heading in the direction of the nearest town.")
            randNum = randint(1,10)

            #if randint 1-2: find food, decide to eat/not eat it
            if randNum <= 2:
                #eat()
                travDist = distTrav(playerHealth, backpack)
                foodNum = randint(0,(len(FOODS) - 1))
                print("As you are walking, you find a backpack.")
                print("Inside the backpack, there is some", FOODS[foodNum])
                playerHealth = eat(playerHealth, foodNum)

                if playerHealth > MIN_HEALTH:
                    print("After eating, you get back on the trail and", \
                          "manage to go", travDist, "miles before it is dark.")

            #if randint 3-4: find an item; steal it
            elif randNum <= 4:
                findItem(backpack)
                travDist = distTrav(playerHealth, backpack)
                print("You get back on the trail and manage to", \
                      "go", travDist, "miles before it is too dark.")
                
            #if randint 5-6: fall in a ditch
            elif randNum <= 6:
                travDist = ditch(playerHealth, backpack)
                dayCount += 1

            #if randint 7-9: fight the monster
            elif randNum <= 9:
                travDist = distTrav(playerHealth, backpack)
                playerHealth = fight(playerHealth, backpack, item)

                if playerHealth > MIN_HEALTH:
                    print("You limp away, managing to go", travDist, \
                          "miles before it is too dark.")
                
            #if randint 10: uneventfully walk in the woods   
            else:
                travDist = walk(playerHealth, backpack)

        #once finished day's events: eval status
        totDist += travDist
        if playerHealth > MIN_HEALTH and dayCount < SURVIVE_DAYS \
           and totDist < SURVIVE_DIST:
            print()
            print("You traveled", str(totDist), "miles in total.")
            print("You're getting closer to safety.")
            dayCount += 1
             
    #exit loop   
    #You made it! ending
    if (dayCount >= SURVIVE_DAYS or totDist >= SURVIVE_DIST) \
       and playerHealth > 0:
        survived(dayCount, totDist, playerHealth, item) 
        
    #You're dead... sorry dude... ending
    if playerHealth <= 0:
        deadEnd(dayCount, totDist, playerHealth, item)
    
main()
