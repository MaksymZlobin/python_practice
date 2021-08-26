from typing import Optional

bardic_dice_max_value = 6


def bardic_inspiration_assistant(dice_roll: int, goal: Optional[int] = None) -> str:
    """"D&D bardic inspiration dice assistant, that make you choose correct decision"""
    bardic_formula = goal - dice_roll <= bardic_dice_max_value if goal else False
    x = dice_roll >= goal if goal else False
    if type(dice_roll) != int or type(goal) not in [int, None]:
        return 'Invalid data type!'
    elif dice_roll >= 17 or (goal and not bardic_formula) or x:
        return 'No bardic inspiration dice needed'
    elif goal and bardic_formula:
        return 'Use bardic inspiration dice'
    elif not goal:
        return "It's risky, dude!!!"


print(bardic_inspiration_assistant('pipa'))