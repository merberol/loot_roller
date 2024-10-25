#! /usr/bin/python3
from data import treashuretable_3_5 as t3_5
import json
import random as rand
import sys


def is_in(a_string : str, roll : int) -> bool:
    val = eval(a_string)
    # print(val, roll)
    assert isinstance(val, tuple), "val is not tuple something went wrong"
    if not val:
        return False
    res = val[0] <= roll and roll <= val[1]
    # print(f"{(val[0] <= roll and roll <= val[1])=}")
    return res


def roll_random(level):
    res = {}
    table = t3_5.TREASHURE_START[level]
    for key, value in table.items():
        # print("rolling for " + key)
        roll = rand.randint(1,100)
        # print(roll)
        for cand , val in value.items():
            if is_in(cand, roll):
                res[key] = val
                break
        else:
            print("Something went wrong", res)
            exit()
    return res

def handle_coins(coins : str):
    a_list = coins.split()
    assert len(a_list) == 5, f"{a_list=} is not 5 elements"

def handle_goods(goods : str):
    pass

def handle_items(items : str):
    pass

def main(level = 1):

    random_result = roll_random(level)
    print(random_result)
    coins = handle_coins(random_result["COINS"])
    goods = handle_goods(random_result["GOODS"])
    items = handle_items(random_result["ITEMS"])
    

if __name__ == "__main__":
    level = int(sys.argv[1])
    # print(level)
    main(level)