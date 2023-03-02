import math
import random

actions = ["a","d","r"]

class NewFighter():
    hp = 100
    guess = 0
    action = None
    def __init__(self, comp):
        self.comp = comp
    def isDead(abc):
        if abc.hp == 0:
            return True
        return False
    def heal(abc, val):
        if abc.hp < 100:
            abc.hp += val

def randGuess(n, p1, p2):
    if abs(n - p1.guess) == abs(n - p2.guess):
        return None
    elif abs(n - p1.guess) < abs(n - p2.guess):
        return p1
    else:
        return p2
def didNotWin(n, p1, p2):
    if randGuess(n, p1, p2) is p1:
        return p2
    elif randGuess(n, p1, p2) is p2:
        return p1
    return 
def isCritical():
    a = random.randint(0, 100)
    if a < 25:
        print("Critical Hit!")
        return 2.5
    return 1
def stunAction(winner, loser):
    n = random.randint(0,10)
    if winner.comp == True:
        winner.guess = random.randint(0,10)
    else:
        winner.guess = int(input("Enter a num: "))
    if abs(n - winner.guess) == 0:
        loser.hp -= (10 * isCritical)
    else:
        x = 10/abs(n - winner.guess)
        loser.hp -= (x * isCritical)

def doActionRound(n, winner, loser):
    if randGuess(n, winner, loser) is None:
        return
    if winner.action == "a":
        if loser.action == "d":
            if abs(n - loser.guess) <= 2:
                loser.hp -= (5 * isCritical()) 
            else:
                loser.hp -= (10 * isCritical())
        elif loser.action == "r":
            loser.hp -= (15 * isCritical())
        else:
            loser.hp -= (10 * isCritical())
    elif winner.action == "d":
        if loser.action == "d":
            print("Nothing Happened.")
        elif loser.action == "a":
            if abs(n - winner.guess) == 0:
                print("Stun!")
            elif abs(n - winner.guess) <= 2:
                print("Hit Reflected!")
                loser.hp -= (5 * isCritical())
            else:
                print("Blocked")
        elif loser.action == "r":
            print("Oof!")
            loser.hp -= 5
    elif winner.action == "r":
        if loser.action == "r":
            winner.heal(10)
            loser.heal(10)
        elif loser.action == "d":
            if abs(n - winner.guess) == 0:
                print("Stun!")
            else:
                print("Nothing Happened.")
        elif loser.action == "a":
            if abs(n - winner.guess) == 0:
                print("Hit Absorbed!")
                winner.heal(10 * isCritical())
            elif abs(n - winner.guess) <= 2:
                print("Dodged!")
            else:
                winner.hp -= (10 * isCritical())



npc = NewFighter(True)
player = NewFighter(False)
players = [player, npc]
break_out_flag = False
while True:
    print("Your HP: ", player.hp)
    print("Opponent's HP: ", npc.hp)
    player.action = input("Attack, Defend, or Reflect? ")
    npc.action = actions[random.randint(0,2)]
    num = random.randint(0, 10)
    npc.guess = random.randint(0,10)
    player.guess = int(input("Enter a num: "))
    doActionRound(num, randGuess(num, player, npc), didNotWin(num, player, npc))
    for p in players:
        if p.isDead():
            break_out_flag = True
            break
    if break_out_flag:
        break
    

