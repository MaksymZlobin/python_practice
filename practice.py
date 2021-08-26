from typing import Optional

BARDIC_DICE_MAX_VALUE = 6
APPROPRIATE_DICE_ROLL = 17


def bardic_inspiration_assistant(dice_roll: int, goal: Optional[int] = None) -> str:
    """"D&D bardic inspiration dice assistant, that make you choose correct decision"""
    if type(dice_roll) != int or type(goal) not in [int, type(None)]:
        return 'Invalid data type!'
    bardic_formula = goal - dice_roll <= BARDIC_DICE_MAX_VALUE if goal else False
    is_dice_roll_gte_goal = dice_roll >= goal if goal else False
    if dice_roll >= APPROPRIATE_DICE_ROLL or (goal and not bardic_formula) or is_dice_roll_gte_goal:
        return 'No bardic inspiration dice needed'
    elif goal and bardic_formula:
        return 'Use bardic inspiration dice'
    elif not goal:
        return "It's risky, dude!!!"


print(bardic_inspiration_assistant())
