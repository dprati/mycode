#!/usr/bin/env python3

# This will be an interactive decision tree
import random

print("Welcome to Dallas Driving!!!\nWe are going to guide you through this!")

error = ["You don't follow directions too good. I said 'Y' or 'N'. Now try again!",
         "How'd you get past the DMV with those eyes? I said 'Y' or 'N'. Now try again!",
         "Let's try this again. Put 'Y' or 'N'."]
#####################################################################
# DEF SURVEY
#####################################################################


def survey():

    def question1():
        print()
        q1 = "First question: are you obeying the speed limit? Y/N"
        print(q1)
        a1 = input()
        a1 = a1.upper()
        print()
        if a1 == 'Y':
            print("You must be new around here. Get off the freeway!\n Better luck next time.")
        elif a1 == 'N':
            print("Right. Speed limits are for the weak and the elderly! Keep on truckin'!")
        else:
            print(random.choice(error))
            question1()

    def question2():
        print()
        q2 = "Second question: are you keeping a safe following distance? Y/N"
        print(q2)
        a2 = input()
        a2 = a2.upper()
        print()
        if a2 == 'Y':
            print("Wrong! You're leaving room for some jack-wagon to sneak in!"
                  "\nToo bad. Try again when you get some nerve.")
        elif a2 == 'N':
            print("Good. This is a no-fault insurance state anyways. Ride 'em!")
        else:
            print(random.choice(error))
            question2()

    def question3():
        print()
        q3 = "Third question: when changing lanes, do you signal first? Y/N"
        print(q3)
        a3 = input()
        a3 = a3.upper()
        print()
        if a3 == 'Y':
            print("Wrong! You'll tip everyone off! See a safe following distances somewhere? GET IN THERE!")
        elif a3 == 'N':
            print("Excellent. Always keep 'em guessing. I can see you've been here a while.")
        else:
            print(random.choice(error))
            question3()

        def play_again():
            Q = "Would you like to play again?"
            print(Q)
            answer = input()
            answer = answer.upper()
            if answer == 'N':
                print()
                print("Well, you can always give horses a try...")
            elif answer == 'Y':
                survey()
            else:
                print()
                print(random.choice(error))
                play_again()

        play_again()

    question1()
    question2()
    question3()

survey()
print()
