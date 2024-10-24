from data import treashuretable_3_5 as t3_5
import json
import random as rand


def is_in(a_string : str, roll : int) -> bool:
    val = eval(a_string)
    print(val, roll)
    assert isinstance(val, tuple), "val is not tuple something went wrong"
    if not val:
        return False
    res = val[0] <= roll and roll <= val[1]
    print(res)
    return res


def roll_random(level):
    res = {}
    table = t3_5.TABLE[level]
    for key, value in table.items():
        print("rolling for " + key)
        roll = rand.randint(1,100)
        print(roll)
        for cand , val in value.items():
            if is_in(cand, roll):
                res[key] = val
                break
        else:
            print("Something went wrong", res)
            exit()
                


def main():

    print(roll_random(1))
    

if __name__ == "__main__":
    main()