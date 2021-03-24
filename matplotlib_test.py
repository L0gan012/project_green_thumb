from database import database
from flask import Flask

def main():

    db = database("./plant_data.db")

    print("Welcome to the plant database!")

    user_choices = {'a':db.add_plant, 's':db.get_plants, 'g': ""}
    
    while(True):
        print("To add a plant press (a)")
        print("To view plants press (s)")
        print("To view temperature/humidity graphs press (g)")
        print("To exit press (x)")
        choice = input("Please select an option: ")
        if(choice == 'x'):
            break
        func = user_choices.get(choice)
        func()

main()