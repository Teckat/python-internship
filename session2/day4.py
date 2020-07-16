
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


def checkWord():
    print()


def play():
    p1 = input('enter player 1 name')
    p2 = input('enter player 2 name')

    print('welcome '+p1)
    print('welcome '+p2)
    pp1 = 0
    pp2 = 0

    turn = 0   # 0 -> player 1's turn  , 1 -> player 2's turn
    while(1):
        word = ranWord()

        jumbled = jumWord(word)
        print(jumbled)


play()
# w = ranWord()
# print(w)

# jumWord('camel')
