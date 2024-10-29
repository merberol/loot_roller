from utils.utils import *
from data.magic_armor_and_shields import ARMOR_COSTS_BY_BONUS

def test_handle_bonus_value():
    print(handle_bonus_value("+2", {"NAME":'+1 Full plate', "VALUE" : "265 gp"}, ARMOR_COSTS_BY_BONUS))



def test_add_spec_abilities():
    spec_abilities = [
         {"NAME" :   "Glamered", "VALUE" : "270 gp"},
         {"NAME" :   "Fortification: light",     "VALUE" : "+1 bonus"}
    ]
    
    res = add_spec_abilities(
            {"NAME":'+1 Full plate', "VALUE" : "265 gp"}, 
            spec_abilities, 
            ARMOR_COSTS_BY_BONUS
        )
    print(res)