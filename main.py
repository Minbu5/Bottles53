from Game import run_game


# This is program - puzzle.
# You have two bottles with capacities 5 liters and 3 liters
# Both vessels don't have markings except for full capacities ( 5 l. and 3 l.) respectively
# You can fill bottles with water, spill out or pour from one to another unlimited times.
# The goal is to get 4 liters in any bottle (obviously in 5 l. bottle)


print('''# You have two bottles with capacities 5 liters and 3 liters.
# Both vessels don't have markings except for full capacities ( 5 l. and 3 l.) respectively.
# You can fill bottles with water, spill out or pour from one to another unlimited times.
# The goal is to get 4 liters in any bottle (obviously in 5 l. bottle)''')


print("******************************************************************")



bot_5 = 0
bot_3 = 0
Game_on = True
while (Game_on):

    run_game(bot_5, bot_3)

    if run_game(bot_5, bot_3) == "4":
        Game_on = False




    # # 5 ltr bottle
    # if action == "1" and sel_bot == "5":
    #     bot_5 += 5
    #
    # if action == "2" and sel_bot == "5":
    #     bot_5 -= bot_5
    #
    #
    # if action == "3" and sel_bot == "5":
    #     bot_5 -= bot_5
    #     bot_3 += bot_5
    #     if bot_3 > 3:
    #         bot_3 = bot_3 - (bot_3 - 3)
    #
    # # 3 ltr bottle
    # if action == "1" and sel_bot == "3":
    #     bot_3 += 3
