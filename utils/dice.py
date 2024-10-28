
"""
Dice rolling module.

Functions

    d(num_sides: int) -> int:
a variable-wrapper around random.randint(1, numsides)


    _roll_n_type(num_rolls: int , num_sides: int, times: int = 1) -> int:

function for rolling a number of dice
"""

import random as r 
def _d(num_sides : int) -> int:
    """
Roll a dice with num_sides
    
Params

    num_sides : the number of sides the dice shuld have
    
Returns
    random int between 1 and num_sides
"""
    return r.randint(1, num_sides)

def _roll_n_type(num_rolls : int , num_sides : int, times : int = 1):
    res = 0
    for _ in range(times):
        for _ in range(num_rolls):
            res += _d(num_sides)
    return res


def roll_dice(dice_type : str, num_rolls : int = 1, times : int = 1):
    match dice_type:
        case "d2":
            return _roll_n_type(num_rolls, 2, times)
        case "d3":
            return _roll_n_type(num_rolls, 3, times)
        case "d4":
            return _roll_n_type(num_rolls, 4, times)
            
        case "d6":
            return _roll_n_type(num_rolls, 6, times)
            
        case "d8":
            return _roll_n_type(num_rolls, 8, times)
            
        case "d10":
            return _roll_n_type(num_rolls, 10,times)
            
        case "d12":
            return _roll_n_type(num_rolls, 12, times)
            
        case "d20":
            return _roll_n_type(num_rolls, 20, times)
            
        case "d100":
            return _roll_n_type(num_rolls, 100, times)
        
    print(f"ERROR Unknown {dice_type=}")
            