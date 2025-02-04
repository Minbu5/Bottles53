bottle_5 = {"max quantity": 5,
            "content": 0,
            "empty space": 5
            }

bottle_3 = {"max quantity": 3,
            "content": 0,
            "empty space": 3
            }


def fill(bottle):
    bottle["content"] = bottle["max quantity"]
    bottle["empty space"] = 0


def spill(bottle):
    bottle["content"] = 0
    bottle["empty space"] = bottle["max quantity"]


def transfer(bottle_from, botttle_to):
    if bottle_from["content"] >= botttle_to["empty space"]:
        transfer_quantity = bottle_from["content"] - (
                bottle_from["content"] - botttle_to["empty space"])  # (5 - (5 - 3)  = 3

    else:
        transfer_quantity = bottle_from["content"]

    bottle_from["content"] -= transfer_quantity
    botttle_to["content"] += transfer_quantity
    bottle_from["empty space"] += transfer_quantity
    botttle_to["empty space"] -= transfer_quantity


def test():
    print("*******************************")
    print(f"Content b5: {bottle_5["content"]}")
    print(f"Free space b5: {bottle_5["empty space"]}")
    print("*******************************")
    print("*******************************")
    print(f"Content b3: {bottle_3["content"]}")
    print(f"Free space b3: {bottle_3["empty space"]}")
    print("*******************************")
    print("*******************************")

# solution 1
###########################
# fill(bottle_5)
# transfer(bottle_5, bottle_3)
# spill((bottle_3))
# transfer(bottle_5, bottle_3)
# fill(bottle_5)
# transfer(bottle_5, bottle_3)


# solution 2
#############################
# fill(bottle_3)
# transfer(bottle_3, bottle_5)
# fill(bottle_3)
# transfer(bottle_3, bottle_5)
# spill(bottle_5)
# transfer(bottle_3, bottle_5)
# fill(bottle_3)
# transfer(bottle_3, bottle_5)
