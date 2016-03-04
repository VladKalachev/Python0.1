#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Mathematics Trainer v0.64 (pre-alpha) by Aunmag

# Loading:
import random
game = 1
trues = 0
mistakes = 0
target = 100

# Welcome:
print("Hello it's the Mathematics Trainer v0.64 (pre-alpha) by Aunmag.\n"
      "Here you can improve your brain by means of arithmetical tasks." + "\n"
      "If you want to finish the game write 'end' in answer.\n")

# Difficulty configs:
difficulty = input("To start enter any value of difficulty level (1 to 7) here: ")
if difficulty.lower() == "end":
    raise SystemExit(1)
elif int(difficulty) < 1:
    difficulty = 1
elif int(difficulty) > 7:
    difficulty = 7

print("\nGood luck, begin! =)\n")

while game:

    # Mode generation (0 - addition, 1 - subtraction, 2 - multiplication, 3 - division):
    max_mod = 3
    if int(difficulty) < 3:
        max_mod = 1
    mode = random.randrange(max_mod + 1)

    # Numbers generation:
    max_num = 10 ** int(difficulty)
    x = random.randrange(1, max_num)
    y = random.randrange(1, max_num)

    # General text of tasks:
    ask = ("How much is " + "task" + "? Write answer: ")

    #  Host monitoring (optional):
    '''print("HOST. Difficulty: " + str(difficulty) + ". Mode: " + str(mode) + ". Nums: " + str(x) + ", " + str(y))'''

    # Converting numbers for multiplication and division modes by difficulty:
    if mode >= 2:
        if int(difficulty) < 5:
            x //= 10 ** (int(difficulty) - 1)
            if x == 0:
                x = random.randrange(1, 10)
        elif int(difficulty) >= 5:
            x //= 10 ** (int(difficulty) - 2)
            if x == 0:
                x = random.randrange(10, 100)
        if int(difficulty) < 7:
            y //= 10 ** (int(difficulty) - 1)
            if y == 0:
                y = random.randrange(1, 10)
        elif int(difficulty) == 7:
            y //= 10 ** (int(difficulty) - 2)
            if y == 0:
                y = random.randrange(10, 100)

    # Asks (0 - addition, 1 - subtraction, 2 - multiplication, 3 - division):
    if mode == 0:
        task = x + y
        answer = input(ask.replace("task", str(x) + "+" + str(y)))
    elif mode == 1:
        task = x - y
        answer = input(ask.replace("task", str(x) + "-" + str(y)))
    elif mode == 2:
        task = x * y
        answer = input(ask.replace("task", str(x) + "*" + str(y)))
    elif mode == 3:
        task = (x * y) / y
        answer = input(ask.replace("task", str(x*y) + "/" + str(y)))

    # Checking of answer:
    if answer.lower() == "end":
        print("\nGame has ended. You got " + str(trues - mistakes) + " scores."
              "\nTrue answers: " + str(trues) +
              "\nFalse answers: " + str(mistakes))
        end = input("Enter 'end' again to exit: ")
        if end.lower() == "end":
            break
    elif int(answer) == task:
        trues += 1
        print("Right!\n")
    elif int(answer) != task:
        mistakes += 1
        print("Wrong!! Is " + str(int(task)) + "!\n")
    if int(difficulty) < 7:
        print("Current level is completed by " + str(int((trues - mistakes)/target*100)) + "%!\n")

    # Level control:
    if int(trues - mistakes) == target and int(difficulty) < 7:
        difficulty = int(difficulty) + 1
        print("Hooray! You have " + str(target) + " scores "
              "(" + str(trues) + " true and " + str(mistakes) + " false answers). "
              "Welcome to " + str(difficulty) + " level!\n")
        trues = 0
        mistakes = 0
        continue
    elif int(trues - mistakes) <= -3 and int(difficulty) > 1:
        difficulty = int(difficulty) - 1
        print("You have enough mistakes to return back "
              "(" + str(trues) + " true and " + str(mistakes) + " false answers). "
              "Practice on " + str(difficulty) + " level else.\n")
        trues = 0
        mistakes = 0
        continue