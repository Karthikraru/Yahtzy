from scoresheets import YahtzyScoreSheet
from hands import YahtzyHand
from dice import D6
from player import Player
import sys


def stars():
    return ("***************************")


def testIfInt(value):
    try:
        value = int(value)
        user.updateScore(value)
        return
    except ValueError:
        return
    except TypeError:
        return


user = Player()
quit = False
numRoll = 0

print("Welcome to Yahtzy. If you would like to quit at any time, type 'QUIT'")

while quit == False or len(user.scoreSheet.upperSection) > 0 or len(user.scoreSheet.lowerSection) > 0:
    numRoll = numRoll + 1
    if quit == False:
        hand = user.rollDice()
        done = False
        print("Roll {}:".format(numRoll))
        while (done == False):
            if len(hand) < 2:
                break
            print(hand)
            print("The available categories in the top section are {}".format(user.scoreSheet.upperSection))
            print("The available categories in the bottom section are {}".format(user.scoreSheet.lowerSection))
            print(
                "What category would you like to test? NOTE: Must enter the category exactly as stated above. If you do not see any category that applies to the dice, type 'NEXT' to get new dice")
            category = input("")
            category = category.lower()
            if category != "":
                value = 0
                if category == "next":
                    print("")
                    print(stars())
                    done = True

                elif category == "quit":
                    print("You are ending with {} points after {} rolls".format(user.score, numRoll))
                    sys.exit(0)
                elif category == "1":
                    value = YahtzyScoreSheet().score_one_pair(hand, user, 1)

                elif category == "2":
                    value = YahtzyScoreSheet().score_one_pair(hand, user, 2)

                elif category == "3":
                    value = YahtzyScoreSheet().score_one_pair(hand, user, 3)

                elif category == "4":
                    value = YahtzyScoreSheet().score_one_pair(hand, user, 4)

                elif category == "5":
                    value = YahtzyScoreSheet().score_one_pair(hand, user, 5)

                elif category == "6":
                    value = YahtzyScoreSheet().score_one_pair(hand, user, 6)

                elif category == "3 of a kind":
                    value = YahtzyScoreSheet().three_of_a_kind(hand, user)

                elif category == "4 of a kind":
                    value = YahtzyScoreSheet().four_of_a_kind(hand, user)

                elif category == "yahtzy":
                    value = YahtzyScoreSheet().YAHTZY(hand, user)

                elif category == "small straight":
                    value = YahtzyScoreSheet().smallStraight(hand, user)

                elif category == "large straight":
                    value = YahtzyScoreSheet().largeStraight(hand, user)
                elif category == "full house":
                    value = YahtzyScoreSheet().fullHouse(hand, user)
                else:
                    pass

                if value != 0:
                    testIfInt(value)
                    print("")
                    try:
                        if "No" in value:
                            print(value)
                    except TypeError:
                        print("You received {} points!".format(value))
                    print("Total points: {}".format(user.score))
                print("")
                value = 0
                if len(user.scoreSheet.upperSection) == 0 and len(user.scoreSheet.upperSection) == 0:
                    quit = True
                    break

