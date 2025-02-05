from bottles import *

def quit():
    print("******************************************************************")
    confirm = input("If you wish to start again - 1\n"
                    "Any other key to quit program:\n ")

    if confirm == "1":
        spill(bottle_5)
        spill(bottle_3)
        game()


def game ():
    def stop_game(action):
        if action == "4":
            print("Puzzle stopped.")
            return True
    game = "on"
    while game == "on":

        print(f"In 5 l. bottle is {bottle_5["content"]} l.\nIn in 3 l. bottle is {bottle_3["content"]} l.")
        print("******************************************************************")

        sel_bot = input(f"Select bottle: \n5 - for 5 l.;  \n3 - for 3 l.;\n4 - to reset game;\n")
        print("******************************************************************")
        if stop_game(sel_bot):
            break

        action = input(
            "Select action \n1 - to fill with watter; \n2 - spill out; \n3 - pour in another; \n4 - to reset game;\n")
        if stop_game(action):
            break

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



        if bottle_5["content"] == 4:
            game = "win"
            print("*******************")
            print("**     !!!!!     **")
            print("** !!! WOHOO !!! **")
            print("**     !!!!!     **")
            print("*******************")

    quit()

