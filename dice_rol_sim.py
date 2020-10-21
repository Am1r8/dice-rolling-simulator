print("Version: 2.1.3\nPublisher: AlPHA83,Unknown\nGame: dice rolling simulator\nThanks for using my code!:)")

try:
    import random
    from time import sleep
except:
    print("Can't open modules please check the code")
sleep(2)
def start():
    print("Welcome to Dice rolling simulator")
    sleep(2)
    dice_num = int(input("how many dice you wanna play with???!\none\ntwo\n"))
    how_many = int(input("how many times you wanna play???\n"))
    start_r = input("are you ready??!\nyes\nno\n")
    sleep(1)
    if start_r == "yes" or start_r == "y":
        if dice_num == 1:
            for i in range(how_many):
                dice_1()
            sleep(1)
            again()
        elif dice_num == 1:
            for i in range(how_many):
                dice_2()
            sleep(1)
            again()
        else:
            return exit()
    else:
        return exit()


def dice_1():

    dice_s_1 = """

     _______
    |       |
    |   X   |   1
    |       |
     _______
    """
    dice_s_2 = """
     _______
    | X     |
    |       |   2
    |      X|
     _______
    """
    dice_s_3 = """
     _______
    |      X|
    |   X   |   3
    |X      |
     _______
    """
    dice_s_4 = """
     _______
    |X     X|
    |       |   4
    |X     X|
     _______
    """
    dice_s_5 = """
     _______
    |X     X|
    |   X   |   5
    |X     X|
     _______
    """
    dice_s_6 = """
     _______
    |X     X|
    |X     X|   6
    |X     X|
     _______
    """


    for i in range(1,4):
        print(i,"\n")
        sleep(0.5)
    dices = [dice_s_1,dice_s_2,dice_s_3,dice_s_4,dice_s_5,dice_s_6]

    print(random.choice(dices))



def dice_2():
    dice_s_1 = """

     _______
    |       |
    |   X   |   1
    |       |
     _______
    """
    dice_s_2 = """
     _______
    | X     |
    |       |   2
    |      X|
     _______
    """
    dice_s_3 = """
     _______
    |      X|
    |   X   |   3
    |X      |
     _______
    """
    dice_s_4 = """
     _______
    |X     X|
    |       |   4
    |X     X|
     _______
    """
    dice_s_5 = """
     _______
    |X     X|
    |   X   |   5
    |X     X|
     _______
    """
    dice_s_6 = """
     _______
    |X     X|
    |X     X|   6
    |X     X|
     _______
    """



    for i in range(1,4):
        print(i,"\n")
        sleep(0.5)
    dices = [dice_s_1,dice_s_2,dice_s_3,dice_s_4,dice_s_5,dice_s_6]

    print(random.choice(dices),random.choice(dices))

def start_again():
    ask = int(input("how many times you wanna play?"))
    num = int(input("one or two?\n"))
    if num == 1:
        for i in range(ask):
            dice_1()

    if num == 2:
        for i in range(ask):
            dice_2()
    sleep(1)
    again()

def again():
    again1 = input("Do you wanna roll another time?\nyes\nno\n")
    if again1 == "yes" or again1 == "y":
        start_again()
    elif again1 == "no" or again1 == "n":
        sleep(5)
        return exit()
    else:
        return exit()

try:
    start()
except:
    print("There is an error please check the code\nthanks")
