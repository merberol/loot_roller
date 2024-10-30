from data.magic_armor_and_shields import *
from data.magic_weapons import *
from data.rings import roll_minor_ring, roll_medium_ring, roll_major_ring
from data.potions import roll_minor_potion, roll_medium_potion, roll_major_potion
from data.scrolls import roll_minor_scroll, roll_medium_scroll, roll_major_scroll
from data.wands import roll_minor_wand, roll_medium_wand, roll_major_wand
from data.rods import roll_medium_rod, roll_major_rod
from data.wonderous_items import roll_minor_wonderous_item, roll_medium_wonderous_item, roll_major_wonderous_item
from data.staffs import roll_medium_staff, roll_major_staff


MINOR_ITEMS = {
    "(1,14)"  : roll_armor_and_shield_minor,
    "(5,9)"  : roll_weapon_minor,
    "(10,44)"  : roll_minor_potion,
    "(45,46)"  : roll_minor_ring,
    "(47,81)"  : roll_minor_scroll,
    "(82,91)"  : roll_minor_wand,
    "(92,100)" : roll_minor_wonderous_item
}

MEDIUM_ITEMS = {
    "(1,10)" : roll_armor_and_shield_medium,
    "(11,20)" : roll_weapon_medium,
    "(21,30)" : roll_medium_potion,
    "(31,40)" : roll_medium_ring,
    "(41,50)" : roll_medium_rod,
    "(51,65)" : roll_medium_scroll,
    "(66,68)" : roll_medium_staff,
    "(69,83)" : roll_medium_wand,
    "(84,100)" : roll_medium_wonderous_item
}

MAJOR_ITEMS = {
    "(1,10)" : roll_armor_and_shield_major,
    "(11,20)" : roll_weapon_major,
    "(21,25)" : roll_major_potion,
    "(26,35)" : roll_major_ring,
    "(36,45)" : roll_major_rod,
    "(46,55)" : roll_major_scroll,
    "(56,75)" : roll_major_staff,
    "(76,80)" : roll_major_wand,
    "(81,100)" : roll_major_wonderous_item
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
    for _ in range(num_items):
        item_type = roll_table(MAJOR_ITEMS)
        if type(item_type) == str:
            print(item_type)
        else:
            item_type(result)
    return result