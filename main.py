#! /usr/bin/python3
from data import treashuretable_3_5 as t3_5
import sys
import pprint

def parse_goods(goods_data):
    if goods_data == "NONE":
        return "NONE"
    print(f"{goods_data=}")
    out = "*    "
    length = 0
    for key in goods_data.get_table().keys():
        if len(key) > length:
            length = len(key)
    print(length)
    for key, values in goods_data.get_table().items():
        tmp = f"{key}{" " * (length-len(key))}  :  "
        for value in values:
            out += tmp + value+"\n*    "
    return out


def parse_items(items_data):
    return items_data

def main(level = 1):

    result = t3_5.roll_random_treasure(level)
    coins = f"* COINS:\n*    {result.get('COINS')}\n*    "
    goods = f"* GOODS:\n{parse_goods(result.get('GOODS'))}"
    items = f"* ITEMS:\n{parse_items(result.get('ITEMS'))}"
    out = f"{"*" * 80}\n{coins}\n{goods}\n{items}"
    
    print(out)

if __name__ == "__main__":
    level = int(sys.argv[1])
    # print(level)
    main(level)