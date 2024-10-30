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
    print(f"Handlings Coins {coins=}")
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

def round_coins(cp_value : int):
    sp_value = cp_value // 10
    cp_value = cp_value - sp_value * 10

    gp_value = sp_value // 10 
    sp_value = sp_value - gp_value * 10

    pp_value = gp_value // 100
    gp_value = gp_value - pp_value * 100


    vals = []

    if pp_value:
        vals.append(f"{pp_value} pp")
    if gp_value:
        vals.append(f"{gp_value} gp")
    if sp_value:
        vals.append(f"{sp_value} sp")
    if cp_value:
        vals.append(f"{cp_value} cp")

    out = ", ".join(vals)
    print(f"round coins {out=}")
    return out


def add_coins(a_value : str, b_value: str):
    # print(f"adding {a_value=} to {b_value=}")
    a_value = convert_coins_to_cp(a_value)
    b_value = convert_coins_to_cp(b_value)

    return round_coins(a_value + b_value)


def _convertion_helper(raw_val, coin_type):
    match (coin_type):
        case "cp":
            return raw_val
        case "sp":
            return raw_val * 10
        case "gp":
            return raw_val * 100
        case "pp":
            return raw_val * 10_000


def convert_coins_to_cp(coins_str : str) -> int:
    # print(f"converting {coins_str=} to cp")
    result = 0
    for val in coins_str.split(", "):
        # print(val)
        data = val.split()
        result += _convertion_helper(int(data[0]), data[1])

    return result


def subtract_coins(a_val : str, b_val : str):
    print(f"subtracting {b_val=} from {a_val=}")

    # convert to coppers
    a_as_cp = convert_coins_to_cp(a_val)
    b_as_cp = convert_coins_to_cp(b_val)
    res = a_as_cp - b_as_cp
    print(f"res of subraction : {res=}")
    return res


def handle_bonus_value(ability_bonus_str, item_data, bonus_cost_table):
    ability_bonus_str = ability_bonus_str.split()[0]
    current_bonus = item_data["NAME"].split()[0]
    new_bonus = int(current_bonus[1:]) + int(ability_bonus_str[1:])
    # print(f"{new_bonus=}")
    if new_bonus > 10:
        return False, item_data
    new_bonus_str = f"+{new_bonus}"
    # print(f"{new_bonus_str=}")
    new_value_as_cp = convert_coins_to_cp(bonus_cost_table[new_bonus_str])
    # print(f"{new_value_as_cp=}")
    current_bonus_value = bonus_cost_table[current_bonus]
    # print(f"{current_bonus_value=}")
    difference = subtract_coins(item_data["VALUE"], current_bonus_value)
    # print(f"{difference=}")

    new_value = round_coins(new_value_as_cp + difference)
    # print(f"{new_value=}")
    item_data["VALUE"] = new_value

    return True , item_data


def add_spec_abilities(item_data, spec_abilities, bonus_cost_table):
    print(f"adding {spec_abilities=} to {item_data=}")
    if not spec_abilities:
        print("NO spec abilities ")
        return True, item_data
    

    ability_names = []
    for ability in spec_abilities:
        ability_names.append(ability["NAME"])
        ability_value = ability["VALUE"]
        if "+" in ability_value:
            res, item_data = handle_bonus_value(ability_value, item_data, bonus_cost_table)
            if not res:
                return False, item_data
        else:
            new_value = add_coins(item_data["VALUE"], ability_value)
            print(f"{new_value=}")
            item_data["VALUE"] = new_value
    
    item_data["NAME"] += " of " + ability_names[0]
    for name in ability_names[1:]:
        item_data["NAME"] += " and " + name 

    return True, item_data


def roll_spec_ability(table):
    spec_ability = roll_table(table)
    if spec_ability["NAME"] == "Roll twice again":
        return roll_spec_ability(table) + roll_spec_ability(table)
    return [spec_ability] 


def special_ability_and_roll_again(spec_table, item_table):
    spec_abilities = roll_spec_ability(spec_table)
    items_data = roll_table(item_table)
    
    if items_data["NAME"] == "Special ability and roll again":
        data = special_ability_and_roll_again(spec_table, item_table)
        spec_abilities.extend(data[0])
        items_data = data[1]

    print(spec_abilities)
    print(items_data)
    return spec_abilities, items_data
