from data.armor_and_shields import *
from data.magic_weapons import *
from utils.utils import roll_table, handle_coins
from utils.map_list import MapList
from data.weapons import *

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

MASTER_WORK_SHIELDS = {
    "(1,17)"         : {"NAME": "Buckler", "VALUE": "205 sp"},
    "(18,40)"        : {"NAME": "Light wooden shield", "VALUE" : "153 sp"},
    "(41,60)"        : {"NAME": "Light steel shield", "VALUE" : "159 sp"},
    "(61,83)"        : {"NAME": "Heavy wooden shield", "VALUE" : "157 sp"},
    "(84,100)"       : {"NAME": "Heavy steel shield", "VALUE" : "170 sp"}
}

MUNDANE_ARMOR = {
    "(1,12)"        : {"NAME": "Chain shirt", "VALUE" : "10 gp"},
    "(13,18)"       : {"NAME": "mwk studded leather", "VALUE" : "175 sp"}, 
    "(19,26)"       : {"NAME": "Breastplate", "VALUE" : "20 gp"}, 
    "(27,34)"       : {"NAME": "banded mail", "VALUE" : "25 gp"}, 
    "(35,54)"       : {"NAME": "half plate", "VALUE" : "60 gp"}, 
    "(55,80)"       : {"NAME": "full plate", "VALUE" : "150 gp"}, 
    "(81,85)"       : {"NAME": "darkwood buckler", "VALUE" : "205 sp"}, 
    "(86,90)"       : {"NAME": "darkwood shield", "VALUE" : "257 sp"}, 
    "(91,100)"      : {"NAME": "Masterwork Shield", "VALUE" : MASTER_WORK_SHIELDS}, 
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

MINOR_ITEMS = {
    "(1,140)"  : roll_armor_and_shield_minor,
    "(5,9)"  : "WEAPONS_MINOR",
    "(10,44)"  : "Potions",
    "(45,46)"  : "Rings",
    "(47,81)"  : "Scrolls",
    "(82,91)"  : "Wands",
    "(92,100)" : "Wondrous items"
}

MEDIUM_ITEMS = {
    "(1-10)" : "ARMOR_AND_SHIELD_MEDIUM",
    "(11-20)" : "WEAPONS_MEDIUM",
    "(21-30)" : "Potions",
    "(31-40)" : "Rings",
    "(41-50)" : "Rods",
    "(51-65)" : "Scrolls",
    "(66-68)" : "Staffs",
    "(69-83)" : "Wands",
    "(84-100)" : "Wondrous items"
}

MAJOR_ITEMS = {
    "(1-10)" : "ARMOR_AND_SHIELD_MAJOR",
    "(11-20)" : "WEAPONS_MAJOR",
    "(21-25)" : "Potions",
    "(26-35)" : "Rings",
    "(36-45)" : "Rods",
    "(46-55)" : "Scrolls",
    "(56-75)" : "Staffs",
    "(76-80)" : "Wands",
    "(81-100)" : "Wondrous items"
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
        num_items = int(value_data[0])
        print(value)
        for _ in range(num_items):
            value = handle_coins("1 " + " ".join(value_data[1:]))
            result.add(name, value)

def roll_mundane_armor(result : MapList):
    item_data = roll_table(MUNDANE_ARMOR)
    if type(item_data["VALUE"]) == dict:
        print("Rolling for masterwork shield")
        item_data = roll_table(item_data["VALUE"])
    result.add(
        item_data.get("NAME"),
        item_data.get("VALUE")
    )

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


def roll_minor_item(num_items):
    print("rolling minor")
    result = MapList()
    item_type = roll_table(MINOR_ITEMS)
    if type(item_type) == str:
        print(item_type)
    else:
        item_type(result)

    return result

def roll_medium_item(num_items):
    print("rolling medium")
    result = MapList()
    item_type = roll_table(MEDIUM_ITEMS)
    if type(item_type) == str:
        print(item_type)
    else:
        item_type(result)
    return result

def roll_major_item(num_items):
    print("rolling major")
    result = MapList()
    item_type = roll_table(MAJOR_ITEMS)
    if type(item_type) == str:
        print(item_type)
    else:
        item_type(result)
    return result