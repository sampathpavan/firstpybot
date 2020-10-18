"""This is a program for a chatbot...
    1.This bot will ask for the name of the person and greet him
    2.Bot will give choices for the person to select
        choice1 : Know the Weather report of your city
        choice2 : Know the corono updates in your country
        choice3 : Want to motivate yourself 
    3.If the person selected option 1 the bot will ask the person to enter the city name then it will provide the weather report of that city.
    4.If the person selected option 2 the bot will ask the person to enter the country name then it will provide the corona updates of that city.
    5.If the person selected option 3 the bot will provide 4 options
        option1 : WorkFailure Motivation
        option2 : BreakUp Motivation
        option3 : FriendLost Motivation
        option4 : ParentLost Motivation
"""

import random
from datetime import datetime
from corona import coronaUpdates
from weather import weatherReport
from breakup import breakup_motivation
from friendloss import friendlost_grief
from workfailure import workfailure_motivation
from parentloss import parentlost_grief

def greet_and_introduce():
    #list of responses
    responses =[
        "I am glad to help you ",
        "Hope you are fine "       
    ]
    #pick a response at random and return that
    print(f"{get_timeofday_greeting()}! {random.choice(responses)}")

def get_timeofday_greeting():
    current_time = datetime.now()
    timeofday_greeting = "Good morning"
    if current_time.hour > 12 and current_time.hour < 17:
        timeofday_greeting = "Good afternoon"
    elif current_time.hour >=17 and current_time.hour < 22:
        timeofday_greeting = "Good evening"
    elif current_time.hour>= 22:
        timeofday_greeting = "Hi! it's too late"
    return(timeofday_greeting)

def welcome(name):

    messages =[
        "nice to meet u",
        "lets have some good time together"   
    ]
    print()
    print(f"Hi {name.capitalize()}! {random.choice(messages)}")

def show_menu():
    print("***SELECT AN OPTION YOU WANT***")
    print("1.Know the Weather report of your city")
    print("2.Know the corona updates in your country")
    print("3.Want to motivate yourself")
    print("4.Exit")
    print("         ",end="")
    print("---------")
    try:
        return int(input("enter your choice [1-4]: "))
    except:
        print("only enter choice 1,2,3 and 4")
        return 0

def show_motivation_menu():
    print("***SELECT AN OPTION YOU WANT***")
    print("1.WorkFailure Motivation")
    print("2.BreakUp Motivation")
    print("3.FriendLost Motivation")
    print("4.ParentLost Motivation")
    print("5.Exit")
    print("         ",end="")
    print("---------")
    try:
        return int(input("enter your choice [1-5]: "))
    except:
        print("only enter choice 1,2,3 and 4")
        return 0

"""def choice3():
    option=show_motivation_menu()
    while(option!=5):
        if option==1:
            workfailure_motivation()
            print()
            option=show_motivation_menu()
        elif option==2:
            breakup_motivation()
            print()
            option=show_motivation_menu()
        elif option==3:
            friendlost_grief()
            print()
            option=show_motivation_menu()
        elif option==4:
            parentlost_grief()
            print()
            option=show_motivation_menu()
        else:
            showmenu()"""


def bot():
    greet_and_introduce()
    name=input("Can I know your name: ")
    welcome(name)
    choice =show_menu()
    while choice != 5:
        if choice == 1:
            weatherReport()
            choice=show_menu()
        elif choice == 2:
            coronaUpdates()
            choice=show_menu()
        elif choice == 3:
            option=show_motivation_menu()
            while(option!=5):
                if option==1:
                    workfailure_motivation()
                    print()
                    option=show_motivation_menu()
                elif option==2:
                    breakup_motivation()
                    print()
                    option=show_motivation_menu()
                elif option==3:
                    friendlost_grief()
                    print()
                    option=show_motivation_menu()
                elif option==4:
                    parentlost_grief()
                    print()
                    option=show_motivation_menu()
                else:
                    break;
            if(option==5):
                print("Thanks for using my services")
                break;
        elif choice == 4:
            print("Thanks for using my services")
            break;
bot()