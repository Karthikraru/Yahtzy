class YahtzyScoreSheet:

    def __init__(self):
        self.upperSection = [1, 2, 3, 4, 5, 6]
        self.lowerSection = ["3 of a kind", "4 of a kind", "Full House", "Small Straight", "Large Straight", "YAHTZY"]

    def score_ones(self, hand):
        return sum(hand.ones)

    def score_twos(self, hand):
        return sum(hand.twos)

    def score_threes(self, hand):
        return sum(hand.threes)

    def score_fours(self, hand):
        return sum(hand.fours)

    def score_fives(self, hand):
        return sum(hand.fives)

    def score_sixes(self, hand):
        return sum(hand.sixes)

    def _score_set(self, hand, set_size, user):
        scores = [0]
        for worth, count in hand._sets.items():
            if count == set_size:
                scores.append(worth * set_size)
        maxScore = max(scores)
        if maxScore == 0:
            return "No pairs of {}".format(set_size)
        if set_size == 3:
            user.scoreSheet.lowerSection.remove("3 of a kind")
        if set_size == 4:
            user.scoreSheet.lowerSection.remove("4 of a kind")
        if set_size == 5:
            user.scoreSheet.lowerSection.remove("YAHTZY")
            return 50
        for _ in range(set_size):
            hand.remove(maxScore / set_size)
        return maxScore

    def twoPair(self, hand, user, value):
        numVal = 0
        if value not in user.scoreSheet.upperSection:
            return "No pair of {} available for scoring".format(value)
        for val in hand:
            if val == value:
                numVal = numVal + 1
        if numVal >= 2:
            user.scoreSheet.upperSection.remove(value)
            for _ in range(numVal):
                hand.remove(value)
            return value * numVal
        else:
            return "No pairs of {}".format(value)

    def score_one_pair(self, hand, user, value):
        return self.twoPair(hand, user, value)

    def three_of_a_kind(self, hand, user):
        if "3 of a kind" in user.scoreSheet.lowerSection:
            return self._score_set(hand, 3, user)
        return

    def four_of_a_kind(self, hand, user):
        if "4 of a kind" in user.scoreSheet.lowerSection:
            return self._score_set(hand, 4, user)
        return

    def YAHTZY(self, hand, user):
        return self._score_set(hand, 5, user)

    def smallStraight(self, hand, user):
        if not "Small Straight" in user.scoreSheet.lowerSection:
            return "Small straight previously completed"
        x = 0
        while x < 2:
            lastValue = hand[x]
            y = x + 1
            t = x + 4
            while (y < (t)):
                if hand[y] == lastValue:
                    t = t + 1
                else:
                    if hand[y] != lastValue + 1:
                        break
                lastValue = hand[y]
                y = y + 1
                if y == x + 3:
                    user.scoreSheet.lowerSection.remove("Small Straight")
                    for _ in range(4):
                        hand.remove(hand[x])
                    return 30

            x = x + 1
        return "No small straight"

    def largeStraight(self, hand, user):
        if not "Large Straight" in user.scoreSheet.lowerSection:
            return "Large straight previously completed"
        x = 1
        lastValue = hand[0]
        while x < 5:
            if hand[x] != lastValue + 1:
                return "No large straight"
            lastValue = hand[x]
            x = x + 1
        user.scoreSheet.lowerSection.remove("Large Straight")
        for x in range(5):
            hand.remove(hand[0])
        return 40

    def fullHouse(self, hand, user):
        if not "Full House" in user.scoreSheet.lowerSection:
            return "Full house previously completed"
        three = YahtzyScoreSheet().three_for_fullHouse(hand, 3, user)
        try:
            int(three)
        except ValueError:
            return "No full house found(3)"
        two = YahtzyScoreSheet().twoPairFullHouse(hand, user)
        try:
            int(two)
        except ValueError:
            return "No full house found(2)"
        for val in hand:
            hand.remove(val)
        user.scoreSheet.lowerSection.remove("Full House")
        return 25

    def three_for_fullHouse(self, hand, set_size, user):
        scores = [0]
        for worth, count in hand._sets.items():
            if count == set_size:
                scores.append(worth * set_size)
        maxScore = max(scores)
        if maxScore == 0:
            return "No pairs of {}".format(set_size)
        return maxScore

    def twoPairFullHouse(self, hand, user):
        for x in range(5):
            value = x
            numVal = 0
            for val in hand:
                if val == value:
                    numVal = numVal + 1
            if numVal == 2:
                return value * numVal
        return "No pairs of {}".format(value)