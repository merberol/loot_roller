#! /usr/bin/python3
from data import treashuretable_3_5 as t3_5
import sys
import pprint


def parse_coins(coins_data):
    return  f"*    {coins_data}\n*"


def parse_goods(goods_data):
    if goods_data == "NONE":
        return "*    NONE\n*"
    # print(f"{goods_data=}")
    out = "*    "
    length = 0
    for key in goods_data.get_table().keys():
        if len(key) > length:
            length = len(key)
    # print(length)
    for key, values in goods_data.get_table().items():
        tmp = f"{key}{" " * (length-len(key))}  :  "
        for value in values:
            out += tmp + value+"\n*    "
    return out


def parse_items(items_data):
    print(f"{items_data=}")
    if items_data == "NONE":
        return f"*    {items_data}\n*"
    out = "*    "
    length = 50
    for key in items_data.get_table().keys():
        if len(key) > length and "SCROLL" not in key:
            length = len(key)
    # print(length)
    for key, values in items_data.get_table().items():
        tmp = f"{key}{" " * (length-len(key))}  :  "
        for value in values:
            out += tmp + value+"\n*    "
    return out


def main(level = 1):
    result = t3_5.roll_random_treasure(level)
    coins = f"* COINS:\n{
        parse_coins(result.get('COINS'))
    }"
    goods = f"* GOODS:\n{
        parse_goods(result.get('GOODS'))
    }"
    items = f"* ITEMS:\n{
        parse_items(result.get('ITEMS'))
    }"

    out = f"{"*" * 80}\n*\n{coins}\n{goods}\n{items}\n{"*" * 80}"

    print(out)


if __name__ == "__main__":
    level = int(sys.argv[1])
    # print(level)
    main(level)