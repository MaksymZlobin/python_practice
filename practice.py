bardic_dice_max_value = 6


def bardic_inspiration_assistant(dice_roll, goal=None):
    """"D&D bardic inspiration dice assistant, that make you choose correct decision"""
    if dice_roll >= 17:
        return 'No bardic inspiration dice needed'
    else:
        if goal:
            if goal - dice_roll <= bardic_dice_max_value:
                return 'Use bardic inspiration dice'
        else:
            return "It's risky, dude!!!"


print(bardic_inspiration_assistant(16, 24))