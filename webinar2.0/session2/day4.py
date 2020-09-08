
import random as r

# global and local variables


# x = 10  # global variable


# def sum():

#     x = 12  # local variable
#     print("x - sum() = ", x)


# sum()
# print("x = ", x)


# x = 10  # global variable


# def sum():
#     global x
#     x = 12  # local variable
#     print("x - sum() = ", x)


# print("before sum global - x = ", x)
# sum()
# print("after sum global -x = ", x)


#  random module


# 1. random() -> get a float value between 0.0 to 1.0

# a = r.random()
# print(a)


# 2. randrange(start, stop[, step]) -> give you a number between the range but 8(not included)

# a = r.randrange(1, 8)
# print(a)


# 3. randint()-> give you a number between the range include both

# a = r.randint(1, 3)
# print(a)

# 4. choice()

# l = ['apple', 'banana', 'coconut', 'mango', 'guava']

# a = r.choice(l)
# print(a)

# 5. sample()

# l = ['apple', 'banana', 'coconut', 'mango', 'guava']

# a = r.sample(l, k=2)
# print(a)


#  jumbled words :-
#  usage -> control structures, random module, functions, sequences

# player setup :-
#  main function -> play()
#  2 players -> p1 , p2
#  2 points counting variables -> pp1  pp2
#  turn shifting variable -> turn

#  code setup :-

#  random word  -> ranWord()
#  jumbling the random word -> jumWord()
#  checking system -> checkWord()


def ranWord():
    words = ['rain', 'forest', 'parliament', 'railway', 'cartoon', 'creature']
    c = r.choice(words)
    return c


def jumWord(w):

    l = "".join(r.sample(w, len(w)))
    return(l)


def checkWord(word, ans, points):
    if (ans == word):
        print("Congrat's you are correct")
        points += 1
    else:
        print("oooho! you are wrong.....")

    return(points)


def play():
    p1 = input('enter player 1 name')
    p2 = input('enter player 2 name')

    print('welcome '+p1)
    print('welcome '+p2)
    pp1 = 0
    pp2 = 0

    turn = 0   # 0 -> player 1's turn  , 1 -> player 2's turn

    choice = 'y'

    while(choice == 'y'):
        word = ranWord()

        jumbled = jumWord(word)
        print(jumbled)

        if(turn == 0):
            print(p1+"'s Turn")
            ans = input('Enter the correct word')

            pp1 = checkWord(word, ans, pp1)

            turn = 1
        elif(turn == 1):

            print(p2+"'s Turn")
            ans = input('Enter the correct word')

            pp2 = checkWord(word, ans, pp2)

            turn = 0

        choice = input('enter y to continue or x to stop')
        if(choice != 'y'):
            print("player 1 " + p1 + " scored = " + str(pp1))
            print("player 2 " + p2 + " scored = " + str(pp2))
            break


play()
# w = ranWord()
# print(w)

# jumWord('camel')
