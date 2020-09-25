#  jumble word game

# two players
# random word generator function
# jumble function
# turns
# calculate points
# button to quit
import random


def ranword():
    word = ['rain', 'storm', 'cat', 'apple', 'temple']
    c = random.choice(word)
    return c


def jumword(word):

    d = "".join(random.sample(word, len(word)))
    return d


def play():
    p1 = input("player 1 name")
    p2 = input('player 2 name')
    pp1 = 0
    pp2 = 0
    turn = 0

    while True:

        word = ranword()
        jumbled = jumword(word)

        if(turn == 0):
            print("player 1 turn")
            print(jumbled)
            ans = input('enter the correct word')

            if(ans == word):
                print("congrat's you are correct")
                pp1 = pp1+1
            else:
                print("sorry, you are wrong")

            turn = 1
        elif(turn == 1):

            print("player 2 turn")
            print(jumbled)
            ans = input('enter the correct word')

            if(ans == word):
                print("congrat's you are correct")
                pp2 = pp2+1
            else:
                print("sorry, you are wrong")

            turn = 0
        e = input("enter y to continue or x to quit")

        if(e == 'x'):
            print(p1+" points = " + str(pp1))
            print(p2+" points = " + str(pp2))
            break


play()
