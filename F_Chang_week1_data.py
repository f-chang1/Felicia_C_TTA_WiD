# Week 1

# Task 1

import random

num_list = list(range(1, 11))
rand_num = random.randint(1, 10)
name = input("What is your name?")
print("Hi, " + name + ".")
guess = input("I am thinking of an integer between 1 and 10. Can you guess what it is?")
valid = False

while not valid:
    try:
        int_guess = int(guess)
        if int_guess not in num_list:
            guess = input("Please try an integer between 1 and 10.")
        else:
            valid = True
    except ValueError:
        guess = input("Please make sure your guess is an integer. Try again?")

if int_guess == rand_num:
    print("Well done, " + name + ", you guessed correctly.")
else:
    print("Sorry, " + name + f", better luck next time. The number I had chosen was {rand_num}.")

# Task 2

num = input("Give me an integer between 1 and 100, and I'll tell you a joke.")
num_list = list(range(1, 101))

fibonacci = [1]
a = 1
b = 1
while b <= 100:
    fibonacci.append(b)
    c = a + b
    a = b
    b = c

odds = list(range(1, 101, 2))
evens = list(range(2, 101, 2))
valid = False

while not valid:
    try:
        int_num = int(num)
        if int_num not in num_list:
            num = input("Please try an integer between 1 and 100.")
        else:
            valid = True
    except ValueError:
        num = input("Please make sure your guess is an integer. Try again?")

if int_num in fibonacci:
    print("Want to hear my latest joke about the Fibonacci sequence?\n"
          "It's as good as my previous two Fibonacci sequence jokes put together!")
elif int_num in odds:
    print("Do you know what's odd?\nEvery other number.")
else:
    print("I know a person who can only use even numbers.\nWhat are the odds?!")

# Task 3

starter = input("What is your favourite starter?")
main_meal = input("How about your favourite main meal?")
dessert = input("And your favourite dessert?")
drink = input("And finally, what is your favourite drink?")

print("Your favourite meal is " + starter + " and " + main_meal + " followed by " + dessert + ", with a glass of " + drink + ".")

# Task 4

cost = 2000.00
count = 0

while cost >= 1000:
    count += 1
    cost = 0.9 * cost
    if count == 1:
        print("After %d year, the cost of the motorbike = £%.2f" % (count, cost))
    else:
        print("After %d years, the cost of the motorbike = £%.2f" % (count, cost))

# Task 5

op_list = ["a", "s", "d", "m", "p", "sq"]

in_num1 = input("Hi, this is a simple calculator. Please enter your first number.")

valid1 = False

while not valid1:
    try:
        num1 = float(in_num1)
        valid1 = True
    except ValueError:
        in_num1 = input("Please make sure your input is a number. Try again?")

in_num2 = input("Now please enter your second number.")

valid2 = False

while not valid2:
    try:
        num2 = float(in_num2)
        valid2 = True
    except ValueError:
        in_num2 = input("Please make sure your input is a number. Try again?")

op = input("Please choose an operator.\nEnter a for addition, s for subtraction, d for division, m for multiplication, "
                 "p for to the power of and sq for squared.").strip()

while op not in op_list:
    op = input("Please make sure you choose an operator using the key given."
                "\nEnter a for addition, s for subtraction, d for division, m for multiplication, "
                "p for to the power of and sq for squared. \nTry again?").strip()

if op == "a":
    ans = num1 + num2
    print(f"The sum of your numbers = {ans}")
elif op == "s":
    ans = num1 - num2
    print(f"The difference between your numbers = {ans}")
elif op == "d":
    try:
        ans = num1 / num2
        print(f"Dividing your first number by your second number gives {ans}")
    except ZeroDivisionError:
        print("Oops, dividing by 0 is undefined.")
elif op == "m":
    ans = num1*num2
    print(f"The product of your numbers = {ans}")
elif op == "p":
    ans = num1**num2
    print(f"Your first number to the power of your second number = {ans}")
elif op == "sq":
    ans1 = num1**2
    ans2 = num2**2
    print(f"Your numbers squared are {ans1} and {ans2} respectively.")
