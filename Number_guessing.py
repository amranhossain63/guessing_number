#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 00:52:24 2020

@author: hossain
"""

#Guessing Number

# Import package for random numbor

import random

#TO DO : Get one number by user from 1 to 100

list_guesnum = []   #create empty list

machine_num = random.randint(1,100)     #machine random number

# User input

user_num =int(input("Plesae enter any number betwwen 1 and 100 :"))

list_guesnum.append(user_num)

# TO Do : Compare user number with machine number

while user_num != machine_num:
    if user_num > machine_num:
        print("Your Guess number is too high !! Please try again ")

    else:
        print("Your Guess number is too low !! Please try again")

    # input another user number to check
    user_num =int(input("Plesae enter any number betwwen 1 and 100 :"))

    list_guesnum.append(user_num)

# print result

else:
    print("Well done !! you guess the same number as machine")

    # print how many times tried
    print("You have try {} times to guess correct number".format(len(list_guesnum)))

    #print user numbers

    print("Your guesses numbers are :")
    print(list_guesnum)
