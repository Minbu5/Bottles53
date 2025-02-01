from bottles import *

print("******************************************************************")
print('''
# This is puzzle program.
# You have two bottles with capacities 5 liters and 3 liters.
# Both vessels don't have markings except for full capacities (5 l. and 3 l.) respectively.
# You can fill bottles with water, spill out or pour from one to another unlimited times.
# The goal is to get 4 liters in 5 l. bottle
''')
print("******************************************************************")

game = "on"
while game == "on":

    print(f"In 5 l. bottle is {bottle_5["content"]} l.\nIn in 3 l. bottle is {bottle_3["content"]} l.")
    print("******************************************************************")

    sel_bot = input(f"Select bottle: \n5 -  for 5 l.;  \n3 - for 3 l.;")
    print("******************************************************************")

    action = input(
        "Select action \n1 - to fill with watter; \n2 - spill out; \n3 - pour in another; \n4 - to stop game;\n")

    print("******************************************************************")

    if sel_bot == "5":
        if action == "1":
            fill(bottle_5)
        if action == "2":
            spill(bottle_5)
        if action == "3":
            transfer(bottle_5, bottle_3)

    if sel_bot == "3":
        if action == "1":
            fill(bottle_3)
        if action == "2":
            spill(bottle_3)
        if action == "3":
            transfer(bottle_3, bottle_5)
    if action == "4":
        game = "stop"
        print("Game stopped. Bye.")

    if bottle_5["content"] == 4:
        game = "win"
        print("*******************")
        print("**     !!!!!     **")
        print("** !!! WOHOO !!! **")
        print("**     !!!!!     **")
        print("*******************")

    print("******************************************************************")
