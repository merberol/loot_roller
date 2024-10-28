from utils import dice

def is_in(a_string : str, roll : int) -> bool:
    val = eval(a_string)
    assert isinstance(val, tuple), f"val is not tuple something went wrong {a_string=} {roll=}"
    if not val:
        return False
    res = val[0] <= roll and roll <= val[1]
    return res


def roll_table(table):
    roll = dice.roll_dice("d100")
    # print(roll)
    for cand , val in table.items():
        if is_in(cand, roll):
            return  val
    else:
        print("Something went wrong", table)
        exit()


def handle_coins(coins : str):
    # print("Handlings Coins")
    if coins == "NONE":
        return coins
    data = coins.split()
    assert len(data) == 5, f"{data=} is not 5 elements"
    # print(data)

    num_rolls = int(data[0])
    dice_type = data[1]
    times = int(data[3])
    coin_type = data[4]

    num_coins = dice.roll_dice(dice_type, num_rolls, times)
    return f"{num_coins} {coin_type}"

def add_coins(a_value : str, b_value: str):
    print(f"adding {a_value=} to {b_value=}")
    a_value = a_value.split()
    b_value = b_value.split()

    if a_value[1] == b_value[1]:
        return f"{int(a_value[0]) + int(b_value[0])} {a_value[1]}"
