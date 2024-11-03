from data.magic_armor_and_shields import *
from data.magic_weapons import *
from utils.utils import roll_table
from utils.dice import roll_dice
from utils.map_list import MapList
from data.mundane_weapons import *
from data.mundane_armor import roll_mundane_armor

ALCHEMICAL_ITEM = {
    "(1,12)"         : {"NAME":"Alchemist's fire", "VALUE":"1 d4 * 2 gp"},
    "(13,24)"        : {"NAME": "Acid", "VALUE": "2 d4 * 1 gp"},
    "(25,36)"        : {"NAME": "Smokestiks", "VALUE" : "1 d4 * 2 gp"},
    "(37,48)"        : {"NAME": "Holy water", "VALUE" : "1 d4 * 25 sp"}, 
    "(49,62)"        : {"NAME": "Antitoxin", "VALUE" : "1 d4 * 5 gp"}, 
    "(63,74)"        : {"NAME": "Everburning Torch", "VALUE" : "200 sp"}, 
    "(75,88)"        : {"NAME": "Tanglefoot bags", "VALUE" : "1 d4 * 5 gp"}, 
    "(89,100)"       : {"NAME": "Thunderstones", "VALUE" : "1 d4 * 3 gp"}
}

TOOLS_AND_GEAR = {
    "(1,3)"         : {"NAME":"Backpack, empty", "VALUE": "2 sp"},
    "(4,6)"         : {"NAME":"Crowbar", "VALUE": "2 sp"},
    "(7,11)"        : {"NAME":"Lantern, Bullseye", "VALUE": "12 sp"},
    "(12,16)"       : {"NAME":"Lock, Simple", "VALUE": "2 gp"},
    "(17,21)"       : {"NAME":"Lock, Average", "VALUE": "4 gp"},
    "(22,28)"       : {"NAME":"Lock, Good", "VALUE": "8 gp"},
    "(29,35)"       : {"NAME":"Lock, Superior", "VALUE": "15 gp"},
    "(36,40)"       : {"NAME":"Manacles, masterwork", "VALUE": "5 gp"},
    "(41,43)"       : {"NAME":"Mirror, small steel", "VALUE": " 1 gp"},
    "(44,46)"       : {"NAME":"Rope, silk (50 ft)", "VALUE": "1 gp"},
    "(47,53)"       : {"NAME":"Spyglass", "VALUE": "100 gp"},
    "(54,58)"       : {"NAME":"Artisan's tools, masterwork", "VALUE": "55 sp"},
    "(59,63)"       : {"NAME":"Climber's kit", "VALUE": "8 gp"},
    "(64,68)"       : {"NAME":"Disguise kit", "VALUE": "5 sp"},
    "(69,73)"       : {"NAME":"Healer's kit", "VALUE": "5 gp"},
    "(74,77)"       : {"NAME":"Holy symbol, silver", "VALUE": "25 sp"},
    "(78,81)"       : {"NAME":"Hourglass", "VALUE": "25 sp"},
    "(82,88)"       : {"NAME":"Magnifying glass", "VALUE": "10 gp"},
    "(89,95)"       : {"NAME":"Muical instrument, masterwork", "VALUE": "10 gp"},
    "(96,100)"      : {"NAME":"Theives' tools, masterwork", "VALUE": "5 gp"}
}

MUNDANE_ITEMS = {
    "(1,170)"        : "ALCHEMICAL_ITEM",
    "(18,50)"       : "ARMOR",
    "(51,83)"       : "WEAPONS",
    "(84,100)"      : "TOOLS_AND_GEAR"
}



def roll_alchemical_item(result : MapList):
    print("running roll alchemical")
    item_data = roll_table(ALCHEMICAL_ITEM)
    name = item_data.get("NAME")
    value = item_data.get("VALUE")
    if len(value.split()) == 2:
        result.add(name, value)
    else:
        value_data = value.split()
        num_items = roll_dice(value_data[1] ,int(value_data[0]) )
        print(value)
        for _ in range(num_items):
            value = " ".join(value_data[3:])
            result.add(name, value)


def roll_mundane_weapon(result : MapList):
    item_data = roll_table(roll_table(MUNDANE_WEAPONS)["VALUE"])
    if type(item_data["VALUE"]) == dict:
        print("Rolling for Ammunition")
        item_data = roll_table(item_data["VALUE"])
    result.add(
        item_data.get("NAME"),
        item_data.get("VALUE")
    )


def roll_tools_and_gear(result : MapList):
    item_data = roll_table(TOOLS_AND_GEAR)
    result.add(
        item_data.get("NAME"),
        item_data.get("VALUE")
    )

ITEM_TYPES = {
    "ALCHEMICAL_ITEM" : roll_alchemical_item,
    "ARMOR" : roll_mundane_armor,
    "WEAPONS" : roll_mundane_weapon,
    "TOOLS_AND_GEAR" : roll_tools_and_gear
}

def roll_mundane_item(num_items):
    print(f"rolling: {num_items} mundane items")
    result = MapList()
    for _ in range(num_items):
        item_type = roll_table(MUNDANE_ITEMS)
        print(item_type)
        ITEM_TYPES[item_type](result)

    return result


