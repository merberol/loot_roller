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



def test_add_coins():
    coin_str_a = "500 gp, 17 sp, 15 cp"
    coin_str_b = "444 gp, 4 sp, 9 cp"
    result = add_coins(coin_str_a, coin_str_b)
    assert result == "9 pp, 46 gp, 3 sp, 4 cp", f"{result=}"

    coin_str_a = "5 gp, 7 sp, 5 cp"
    coin_str_b = "4 gp, 5 cp"
    result = add_coins(coin_str_a, coin_str_b)
    assert result == "9 gp, 8 sp", f"{result=}"

    coin_str_a = "5 gp"
    coin_str_b = "4 gp"
    result = add_coins(coin_str_a, coin_str_b)
    assert result == "9 gp", f"{result=}"



def test_convert_coins_to_cp():
    res = convert_coins_to_cp("1 pp, 2 gp, 3 sp, 4 cp")
    print(res)

    assert res == (10_000 + 200 + 30 + 4)



def test_round_coins():
    res = round_coins(10_234)
    print(res)

    assert res == "1 pp, 2 gp, 3 sp, 4 cp"