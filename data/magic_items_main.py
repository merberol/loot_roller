from magic_armor_and_shields import *
from magic_weapons import *

MINOR_ITEMS = {
    "(1,14)"  : roll_armor_and_shield_minor,
    "(5,9)"  : roll_weapon_minor,
    "(10,44)"  : "Potions",
    "(45,46)"  : "Rings",
    "(47,81)"  : "Scrolls",
    "(82,91)"  : "Wands",
    "(92,100)" : "Wondrous items"
}

MEDIUM_ITEMS = {
    "(1-10)" : roll_armor_and_shield_medium,
    "(11-20)" : roll_weapon_medium,
    "(21-30)" : "Potions",
    "(31-40)" : "Rings",
    "(41-50)" : "Rods",
    "(51-65)" : "Scrolls",
    "(66-68)" : "Staffs",
    "(69-83)" : "Wands",
    "(84-100)" : "Wondrous items"
}

MAJOR_ITEMS = {
    "(1-10)" : roll_armor_and_shield_major,
    "(11-20)" : roll_weapon_major,
    "(21-25)" : "Potions",
    "(26-35)" : "Rings",
    "(36-45)" : "Rods",
    "(46-55)" : "Scrolls",
    "(56-75)" : "Staffs",
    "(76-80)" : "Wands",
    "(81-100)" : "Wondrous items"
}



def roll_minor_item(num_items):
    print("rolling minor")
    result = MapList()
    for _ in range(num_items):
        item_type = roll_table(MINOR_ITEMS)
        if type(item_type) == str:
            print(item_type)
        else:
            item_type(result)

    return result

def roll_medium_item(num_items):
    print("rolling medium")
    result = MapList()
    for _ in range(num_items):
        item_type = roll_table(MEDIUM_ITEMS)
        if type(item_type) == str:
            print(item_type)
        else:
            item_type(result)
    return result

def roll_major_item(num_items):
    print("rolling major")
    result = MapList()
    for _ in range(num_items)
        item_type = roll_table(MAJOR_ITEMS)
        if type(item_type) == str:
            print(item_type)
        else:
            item_type(result)
    return result