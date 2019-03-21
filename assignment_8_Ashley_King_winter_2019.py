'''
    Assignment: 8 - How To Cheat At Vegas!
    Author: Ashley King
    Date: 2019-02-26
    Description: A simulated slot machine
'''

# import random module
import random

# instantiate global variables
POSSIBILITY_ONE = 'CHERRIES'
POSSIBILITY_TWO = 'BAR'
POSSIBILITY_THREE = '7'
POSSIBILITY_FOUR = 'SPACE'
flag_30_seen = False
flag_50_seen = False
counter = 0

# Triple String Class
class TripleString:
    """ encapsulates a 3-string object """

    # intended class constants ------------------------------------
    MIN_LEN = 1
    MAX_LEN = 50
    DEFAULT_STRING = "(undefined)"

    # constructor method ------------------------------------
    def __init__(self, string1 = DEFAULT_STRING, string2 = DEFAULT_STRING,
                 string3 = DEFAULT_STRING ):
        # instance attributes
        self.string1 = string1
        self.string2 = string2
        self.string3= string3

    # mutator ("set") methods -------------------------------
    def set_string1(self, new_string):
        if self.valid_string(new_string):
            self.string1 = new_string
            return True
        else:
            return False

    def set_string2(self, new_string):
        if self.valid_string(new_string):
            self.string2 = new_string
            return True
        else:
            return False

    def set_string3(self, new_string):
        if self.valid_string(new_string):
            self.string3 = new_string
            return True
        else:
            return False

    # accessor ("get") methods -------------------------------
    def get_string1(self):
        return self.string1

    def get_string2(self):
        return self.string2

    def get_string3(self):
        return self.string3

    # helper methods for entire class -----------------
    def valid_string(self, a_string):
        if(len(a_string) >= TripleString.MIN_LEN and len(a_string) <=
            TripleString.MAX_LEN):
            return True
        else:
            return False

# Global Score Functions

# gets bet from user; $0 to $50; returns user input
# gets input until legal input obtained
def get_bet():
    bet = -1
    bet_question = "Please place a bet between 0 and 50 dollars, 0 to quit: "
    while bet < 0 or bet > 50:
        print(bet_question, end = ' ')
        bet = input()
        try:
            bet = int(bet)
        except:
            bet = -1
    return bet

# returns cherries, bar, 7 or space based on random  number
def rand_string():
    num = random.randrange(1, 101, 1)
    if num <= 40:
        return POSSIBILITY_ONE
    elif num > 40 and num <= 78:
        return POSSIBILITY_TWO
    elif num > 78 and num <= 93:
        return POSSIBILITY_THREE
    else:
        return POSSIBILITY_FOUR

# gets random slot machine string and loads them into a TripleString instance
# returns the TripleString instance
def pull():
    reels = TripleString()
    str1 = rand_string()
    reels.set_string1(str1)
    str2 = rand_string()
    reels.set_string2(str2)
    str3 = rand_string()
    reels.set_string3(str3)
    return reels

# -----------------  MAIN PROGRAM  ------------------------------------------
def get_pay_multiplier(reels):
    strings = [reels.get_string1(), reels.get_string2(), reels.get_string3()]
    # first string is CHERRIES
    if strings[0] == POSSIBILITY_ONE:
        # CHERRIES, CHERRIES, CHERRIES
        if strings[1] == POSSIBILITY_ONE and strings[2] == POSSIBILITY_ONE:
            return 30
        # CHERRIES, CHERRIES, something else
        elif strings[1] == POSSIBILITY_ONE:
            return 15
        # CHERRIES, something else, anything
        else:
            return 5
    # all 3 strings are BAR
    elif strings[0] == POSSIBILITY_TWO and strings[1] == POSSIBILITY_TWO and \
        strings[2] == POSSIBILITY_TWO:
        return 50
    # all 3 strings are 7
    elif strings[0] == POSSIBILITY_THREE and strings[1] == POSSIBILITY_THREE \
        and strings[2] == POSSIBILITY_THREE:
        return 100
    # not any of the above
    else:
        return 0

# a method to display winnings
def display(reels, winnings):
    print(reels.get_string1() + ' ' + reels.get_string2() + ' ' \
          + reels.get_string3())
    if winnings == 0:
        print('Sorry, you lose.')
    else:
        print('You won $' + str(winnings))

# ask user for a bet, and while it isn't 0 keep playing
# stop when you have seen ch,ch,ch AND b,b,b and at least 40 legal runs

while flag_30_seen != True and flag_50_seen != True and counter <= 40:
    user_bet = get_bet()
    # increment counter after legal bet placed
    counter += 1
    while user_bet != 0:
            reels = pull()
            multiplier = get_pay_multiplier(reels)
            if multiplier == 30 and flag_30_seen == False:
                flag_30_seen = True
            if multiplier == 50 and flag_50_seen == False:
                flag_50_seen = True
            winnings = user_bet * multiplier
            display(reels, winnings)
            # if we've seen ch,ch,ch & b,b,b & have at least 40 legal runs, stop
            if flag_30_seen == True and flag_50_seen == True and counter > 40:
                break
            # get another bet
            user_bet = get_bet()
            # increment counter after legal bet placed
            counter += 1
# print end message with the original run numbers for ch,ch,ch and b,b,b
print('GAME OVER!!')

'''--------------- WINNING RUNS
CHERRIES CHERRIES CHERRIES was seen at successful run number 15
BAR BAR BAR was seen at successful run number 6
----------------------------'''

'''----------------OUTPUT OF RUNS (run numbers for ch,ch,ch/b,b,b at bottom ---
Please place a bet between 0 and 50 dollars, 0 to quit:  0
Please place a bet between 0 and 50 dollars, 0 to quit:  51
Please place a bet between 0 and 50 dollars, 0 to quit:  100
Please place a bet between 0 and 50 dollars, 0 to quit:  -2
Please place a bet between 0 and 50 dollars, 0 to quit:  string
Please place a bet between 0 and 50 dollars, 0 to quit:  1
SPACE CHERRIES CHERRIES
Sorry, you lose.
Please place a bet between 0 and 50 dollars, 0 to quit:  2
CHERRIES BAR 7
You won $10
Please place a bet between 0 and 50 dollars, 0 to quit:  3
CHERRIES CHERRIES BAR
You won $45
Please place a bet between 0 and 50 dollars, 0 to quit:  4
7 BAR CHERRIES
Sorry, you lose.
Please place a bet between 0 and 50 dollars, 0 to quit:  5
CHERRIES SPACE BAR
You won $25
Please place a bet between 0 and 50 dollars, 0 to quit:  6
BAR BAR BAR
You won $300
Please place a bet between 0 and 50 dollars, 0 to quit:  7
SPACE CHERRIES CHERRIES
Sorry, you lose.
Please place a bet between 0 and 50 dollars, 0 to quit:  8
BAR 7 BAR
Sorry, you lose.
Please place a bet between 0 and 50 dollars, 0 to quit:  9
CHERRIES BAR CHERRIES
You won $45
Please place a bet between 0 and 50 dollars, 0 to quit:  10
CHERRIES BAR BAR
You won $50
Please place a bet between 0 and 50 dollars, 0 to quit:  11
BAR CHERRIES CHERRIES
Sorry, you lose.
Please place a bet between 0 and 50 dollars, 0 to quit:  12
CHERRIES BAR CHERRIES
You won $60
Please place a bet between 0 and 50 dollars, 0 to quit:  13
SPACE CHERRIES BAR
Sorry, you lose.
Please place a bet between 0 and 50 dollars, 0 to quit:  14
BAR CHERRIES 7
Sorry, you lose.
Please place a bet between 0 and 50 dollars, 0 to quit:  15
CHERRIES CHERRIES CHERRIES
You won $450
Please place a bet between 0 and 50 dollars, 0 to quit:  16
CHERRIES CHERRIES CHERRIES
You won $480
Please place a bet between 0 and 50 dollars, 0 to quit:  17
BAR 7 CHERRIES
Sorry, you lose.
Please place a bet between 0 and 50 dollars, 0 to quit:  18
BAR 7 CHERRIES
Sorry, you lose.
Please place a bet between 0 and 50 dollars, 0 to quit:  19
CHERRIES BAR BAR
You won $95
Please place a bet between 0 and 50 dollars, 0 to quit:  20
BAR BAR CHERRIES
Sorry, you lose.
Please place a bet between 0 and 50 dollars, 0 to quit:  21
CHERRIES CHERRIES BAR
You won $315
Please place a bet between 0 and 50 dollars, 0 to quit:  22
BAR CHERRIES 7
Sorry, you lose.
Please place a bet between 0 and 50 dollars, 0 to quit:  23
BAR CHERRIES 7
Sorry, you lose.
Please place a bet between 0 and 50 dollars, 0 to quit:  24
BAR CHERRIES BAR
Sorry, you lose.
Please place a bet between 0 and 50 dollars, 0 to quit:  25
7 CHERRIES CHERRIES
Sorry, you lose.
Please place a bet between 0 and 50 dollars, 0 to quit:  26
7 BAR SPACE
Sorry, you lose.
Please place a bet between 0 and 50 dollars, 0 to quit:  27
CHERRIES BAR BAR
You won $135
Please place a bet between 0 and 50 dollars, 0 to quit:  28
BAR BAR CHERRIES
Sorry, you lose.
Please place a bet between 0 and 50 dollars, 0 to quit:  29
7 BAR CHERRIES
Sorry, you lose.
Please place a bet between 0 and 50 dollars, 0 to quit:  30
CHERRIES CHERRIES CHERRIES
You won $900
Please place a bet between 0 and 50 dollars, 0 to quit:  31
CHERRIES CHERRIES CHERRIES
You won $930
Please place a bet between 0 and 50 dollars, 0 to quit:  32
BAR BAR 7
Sorry, you lose.
Please place a bet between 0 and 50 dollars, 0 to quit:  33
BAR SPACE BAR
Sorry, you lose.
Please place a bet between 0 and 50 dollars, 0 to quit:  34
BAR CHERRIES SPACE
Sorry, you lose.
Please place a bet between 0 and 50 dollars, 0 to quit:  35
BAR BAR BAR
You won $1750
Please place a bet between 0 and 50 dollars, 0 to quit:  36
BAR BAR BAR
You won $1800
Please place a bet between 0 and 50 dollars, 0 to quit:  37
7 7 BAR
Sorry, you lose.
Please place a bet between 0 and 50 dollars, 0 to quit:  38
CHERRIES BAR CHERRIES
You won $190
Please place a bet between 0 and 50 dollars, 0 to quit:  39
CHERRIES BAR CHERRIES
You won $195
Please place a bet between 0 and 50 dollars, 0 to quit:  40
CHERRIES BAR 7
You won $200
GAME OVER!!
---------------OUTPUT OF RUNS'''