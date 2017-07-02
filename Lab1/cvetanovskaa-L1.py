import random
import math

def enter_balls_number(x):
    '''
Function used for two different purposes: to ask for an initial number of balls, and to ask how many balls the user
wants to take out. It takes one argument -> 1 or 0, to indicate which is the purpose of the function.
'''
    if x==1:
        balls_int=int(raw_input("Please enter the number of balls for this game: "))
        while (balls_int < 15) :
            print("I am sorry but that number is too small.")
            balls_int=int(raw_input("Please try again: "))
        return balls_int
    else:
        balls=int(raw_input("How many balls would you like to take out? "))
        while (balls>4):
            print ("I am sorry but that number is too big.")
            balls=int(raw_input("Please try again: "))
        return balls

def game_play(x):
    '''
    It takes one input parameter - the number of balls that the user wants to play with. It checks whether
    there are that many balls left, and if yes then it takes that number out of the sum. Aferwards it asks the
    computer to choose a number and if there are no more balls left, it announces the winner.
    :return:
    '''
    s=0
    player=enter_balls_number(s)
    print("So, you want to take " + str(player) +" balls.")
    while (player>x):
        print "I am sorry but we don't have that many balls. Please try again."
        player=enter_balls_number(s)
    x=x-player
    if x==0:
        print "Congratulations! You won!"
    else:
        print "\n"
        result=comp_choose(x)
        x=result
        if x==0:
            print "Sorry, but the computer won. Thank you for playing."
    return x

def comp_choose(x):
    '''
    It takes one parameter -> the number of balls left in the pile.
    It decides how many balls the computer should take out. If it is possible to leave the pile as a multiple of 5
    then it takes that many, else it chooses randomly
    '''
    if ((x-1)%5)==0:
        comp=1
    elif((x-2)%5)==0:
        comp=2
    elif((x-3)%5)==0:
        comp=3
    elif((x-4)%5)==0:
        comp=4
    else:
        numbers=[1,2,3,4]
        comp=random.choice(numbers)
        while(x<comp):
            comp=random.choice(numbers)
    print "Computer took " + str(comp) + " balls."
    return x-comp


def main():
    '''
    main function. It contains the whole gameplay
    '''
    flag=1
    balls=enter_balls_number(flag)
    while balls != 0:
        balls=game_play(balls)

main()