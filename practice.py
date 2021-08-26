

def bia(dice_roll, goal=None):
    """"D&D bardic inspiration dice assistant, that make you choose correct decision"""
    if dice_roll >= 17:
        print('No bardic inspiration dice needed')
    else:
        if goal:
            bardic_dice_max_value = 6
            if goal - dice_roll <= bardic_dice_max_value:
                print('Use bardic inspiration dice')
            else:
                print('No bardic inspiration dice needed')
        else:
            print("It's risky, dude!!!")

bia(12, 6)

