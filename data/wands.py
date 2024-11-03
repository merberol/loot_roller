from utils.map_list import MapList
from utils.utils import roll_table, round_coins, convert_coins_to_cp
from random import randint



WANDS_MINOR = {
    "(1,2)" : 	{"NAME" : "Detect magic", "VALUE" : "375 sp"},
    "(3,4)" : 	{"NAME" : "Light", "VALUE" : "375 sp"},
    "(5,7)" : 	{"NAME" : "Burning hands", "VALUE" : "750 sp"},
    "(8,10)" : 	{"NAME" : "Charm animal", "VALUE" : "750 sp"},
    "(11,13)" : 	{"NAME" : "Charm person", "VALUE" : "750 sp"},
    "(14,16)" : 	{"NAME" : "Color spray", "VALUE" : "750 sp"},
    "(17,19)" : 	{"NAME" : "Cure light wounds", "VALUE" : "750 sp"},
    "(20,22)" : 	{"NAME" : "Detect secret doors", "VALUE" : "750 sp"},
    "(23,25)" : 	{"NAME" : "Enlarge person", "VALUE" : "750 sp"},
    "(26,28)" : 	{"NAME" : "Magic missile (1st)", "VALUE" : "750 sp"},
    "(29,31)" : 	{"NAME" : "Shocking grasp", "VALUE" : "750 sp"},
    "(32,34)" : 	{"NAME" : "Summon monster I", "VALUE" : "750 sp"},
    "(35,36)" : 	{"NAME" : "Magic missile (3rd)", "VALUE" : "2250 sp"},
    "(37,37)" : 	{"NAME" : "Magic missile (5th)", "VALUE" : "3750 sp"},
    "(38,40)" : 	{"NAME" : "Bear’s endurance", "VALUE" : "4500 sp"},
    "(41,43)" : 	{"NAME" : "Bull’s strength", "VALUE" : "4500 sp"},
    "(44,46)" : 	{"NAME" : "Cat’s grace", "VALUE" : "4500 sp"},
    "(47,49)" : 	{"NAME" : "Cure moderate wounds", "VALUE" : "4500 sp"},
    "(50,51)" : 	{"NAME" : "Darkness", "VALUE" : "4500 sp"},
    "(52,54)" : 	{"NAME" : "Daze Monster", "VALUE" : "4500 sp"},
    "(55,57)" : 	{"NAME" : "Delay poison", "VALUE" : "4500 sp"},
    "(58,60)" : 	{"NAME" : "Eagle’s splendor", "VALUE" : "4500 sp"},
    "(61,63)" : 	{"NAME" : "False life", "VALUE" : "4500 sp"},
    "(64,66)" : 	{"NAME" : "Fox’s cunning", "VALUE" : "4500 sp"},
    "(67,68)" : 	{"NAME" : "Ghoul touch", "VALUE" : "4500 sp"},
    "(69,71)" : 	{"NAME" : "Hold person", "VALUE" : "4500 sp"},
    "(72,74)" : 	{"NAME" : "Invisibility", "VALUE" : "4500 sp"},
    "(75,77)" : 	{"NAME" : "Knock", "VALUE" : "4500 sp"},
    "(78,80)" : 	{"NAME" : "Levitate", "VALUE" : "4500 sp"},
    "(81,83)" : 	{"NAME" : "Acid arrow", "VALUE" : "4500 sp"},
    "(84,86)" : 	{"NAME" : "Mirror image", "VALUE" : "4500 sp"},
    "(87,89)" : 	{"NAME" : "Owl’s wisdom", "VALUE" : "4500 sp"},
    "(90,91)" : 	{"NAME" : "Shatter", "VALUE" : "4500 sp"},
    "(92,94)" : 	{"NAME" : "Silence", "VALUE" : "4500 sp"},
    "(95,97)" : 	{"NAME" : "Summon monster II", "VALUE" : "4500 sp"},
    "(98,100)" : 	{"NAME" : "Web", "VALUE" : "4500 sp"}
}


WANDS_MEDIUM = {
    "(1,3)" : 	{"NAME" : "Magic missile (5th)", "VALUE" : "3750 sp"},
    "(4,7)" : 	{"NAME" : "Bear’s endurance", "VALUE" : "4500 sp"},
    "(8,11)" : 	{"NAME" : "Bull’s strength", "VALUE" : "4500 sp"},
    "(12,15)" : 	{"NAME" : "Cat’s grace", "VALUE" : "4500 sp"},
    "(16,20)" : 	{"NAME" : "Cure moderate wounds", "VALUE" : "4500 sp"},
    "(21,22)" : 	{"NAME" : "Darkness", "VALUE" : "4500 sp"},
    "(23,24)" : 	{"NAME" : "Daze Monster", "VALUE" : "4500 sp"},
    "(25,27)" : 	{"NAME" : "Delay poison", "VALUE" : "4500 sp"},
    "(28,31)" : 	{"NAME" : "Eagle’s splendor", "VALUE" : "4500 sp"},
    "(32,33)" : 	{"NAME" : "False life", "VALUE" : "4500 sp"},
    "(34,37)" : 	{"NAME" : "Fox’s cunning", "VALUE" : "4500 sp"},
    "(38,38)" : 	{"NAME" : "Ghoul touch", "VALUE" : "4500 sp"},
    "(39,39)" : 	{"NAME" : "Hold person", "VALUE" : "4500 sp"},
    "(40,42)" : 	{"NAME" : "Invisibility", "VALUE" : "4500 sp"},
    "(43,44)" : 	{"NAME" : "Knock", "VALUE" : "4500 sp"},
    "(45,45)" : 	{"NAME" : "Levitate", "VALUE" : "4500 sp"},
    "(46,47)" : 	{"NAME" : "Acid arrow", "VALUE" : "4500 sp"},
    "(48,49)" : 	{"NAME" : "Mirror image", "VALUE" : "4500 sp"},
    "(50,53)" : 	{"NAME" : "Owl’s wisdom", "VALUE" : "4500 sp"},
    "(54,54)" : 	{"NAME" : "Shatter", "VALUE" : "4500 sp"},
    "(55,56)" : 	{"NAME" : "Silence", "VALUE" : "4500 sp"},
    "(57,57)" : 	{"NAME" : "Summon monster II", "VALUE" : "4500 sp"},
    "(58,59)" : 	{"NAME" : "Web", "VALUE" : "4500 sp"},
    "(60,62)" : 	{"NAME" : "Magic missile (7th)", "VALUE" : "5250 sp"},
    "(63,64)" : 	{"NAME" : "Magic missile (9th)", "VALUE" : "6750 sp"},
    "(65,67)" : 	{"NAME" : "Call lightning (5th)", "VALUE" : "11250 sp"},
    "(68,00)" : 	{"NAME" : "Charm person, heightened (3rd-level spell)", "VALUE" : "11250 sp"},
    "(69,70)" : 	{"NAME" : "Contagion", "VALUE" : "11250 sp"},
    "(71,74)" : 	{"NAME" : "Cure serious wounds", "VALUE" : "11250 sp"},
    "(75,77)" : 	{"NAME" : "Dispel magic", "VALUE" : "11250 sp"},
    "(78,81)" : 	{"NAME" : "Fireball (5th)", "VALUE" : "11250 sp"},
    "(82,83)" : 	{"NAME" : "Keen edge", "VALUE" : "11250 sp"},
    "(84,87)" : 	{"NAME" : "Lightning bolt (5th)", "VALUE" : "11250 sp"},
    "(88,89)" : 	{"NAME" : "Major image", "VALUE" : "11250 sp"},
    "(90,91)" : 	{"NAME" : "Slow", "VALUE" : "11250 sp"},
    "(92,94)" : 	{"NAME" : "Suggestion", "VALUE" : "11250 sp"},
    "(95,97)" : 	{"NAME" : "Summon monster III", "VALUE" : "11250 sp"},
    "(98,98)" : 	{"NAME" : "Fireball (6th)", "VALUE" : "13500 sp"},
    "(99,99)" : 	{"NAME" : "Lightning bolt (6th)", "VALUE" : "13500 sp"},
    "(100,100)" : 	{"NAME" : "Searing light (6th)", "VALUE" : "13500 sp"}
}




WANDS_MAJOR = {
    "(1,2)" : 	{"NAME" : "Magic missile (7th)", "VALUE" : "5250 sp"},
    "(3,5)" : 	{"NAME" : "Magic missile (9th)", "VALUE" : "6750 sp"},
    "(6,7)" : 	{"NAME" : "Call lightning (5th)", "VALUE" : "11250 sp"},
    "(8,8)" : 	{"NAME" : "Charm person, heightened (3rd-level spell)", "VALUE" : "11250 sp"},
    "(9,10)" : 	{"NAME" : "Contagion", "VALUE" : "11250 sp"},
    "(11,13)" : 	{"NAME" : "Cure serious wounds", "VALUE" : "11250 sp"},
    "(14,15)" : 	{"NAME" : "Dispel magic", "VALUE" : "11250 sp"},
    "(16,17)" : 	{"NAME" : "Fireball (5th)", "VALUE" : "11250 sp"},
    "(18,19)" : 	{"NAME" : "Keen edge", "VALUE" : "11250 sp"},
    "(20,21)" : 	{"NAME" : "Lightning bolt (5th)", "VALUE" : "11250 sp"},
    "(22,23)" : 	{"NAME" : "Major image", "VALUE" : "11250 sp"},
    "(24,25)" : 	{"NAME" : "Slow", "VALUE" : "11250 sp"},
    "(26,27)" : 	{"NAME" : "Suggestion", "VALUE" : "11250 sp"},
    "(28,29)" : 	{"NAME" : "Summon monster III", "VALUE" : "11250 sp"},
    "(30,31)" : 	{"NAME" : "Fireball (6th)", "VALUE" : "13500 sp"},
    "(32,33)" : 	{"NAME" : "Lightning bolt (6th)", "VALUE" : "13500 sp"},
    "(34,35)" : 	{"NAME" : "Searing light (6th)", "VALUE" : "13500 sp"},
    "(36,37)" : 	{"NAME" : "Call lightning (8th)", "VALUE" : "18000 sp"},
    "(38,39)" : 	{"NAME" : "Fireball (8th)", "VALUE" : "18000 sp"},
    "(40,41)" : 	{"NAME" : "Lightning bolt (8th)", "VALUE" : "18000 sp"},
    "(42,45)" : 	{"NAME" : "Charm monster", "VALUE" : "21000 sp"},
    "(46,50)" : 	{"NAME" : "Cure critical wounds", "VALUE" : "21000 sp"},
    "(51,52)" : 	{"NAME" : "Dimensional anchor", "VALUE" : "21000 sp"},
    "(53,55)" : 	{"NAME" : "Fear", "VALUE" : "21000 sp"},
    "(56,59)" : 	{"NAME" : "Greater invisibility", "VALUE" : "21000 sp"},
    "(60,60)" : 	{"NAME" : "Hold person, heightened (4th level)", "VALUE" : "21000 sp"},
    "(61,65)" : 	{"NAME" : "Ice storm", "VALUE" : "21000 sp"},
    "(66,68)" : 	{"NAME" : "Inflict critical wounds", "VALUE" : "21000 sp"},
    "(69,72)" : 	{"NAME" : "Neutralize poison", "VALUE" : "21000 sp"},
    "(73,74)" : 	{"NAME" : "Poison", "VALUE" : "21000 sp"},
    "(75,77)" : 	{"NAME" : "Polymorph", "VALUE" : "21000 sp"},
    "(78,78)" : 	{"NAME" : "Ray of enfeeblement, heightened (4th level)", "VALUE" : "21000 sp"},
    "(79,79)" : 	{"NAME" : "Suggestion, heightened (4th level)", "VALUE" : "21000 sp"},
    "(80,82)" : 	{"NAME" : "Summon monster IV", "VALUE" : "21000 sp"},
    "(83,86)" : 	{"NAME" : "Wall of fire", "VALUE" : "21000 sp"},
    "(87,90)" : 	{"NAME" : "Wall of ice", "VALUE" : "21000 sp"},
    "(91,91)" : 	{"NAME" : "Dispel magic (10th)", "VALUE" : "22500 sp"},
    "(92,92)" : 	{"NAME" : "Fireball (10th)", "VALUE" : "22500 sp"},
    "(93,93)" : 	{"NAME" : "Lightning bolt (10th)", "VALUE" : "22500 sp"},
    "(94,94)" : 	{"NAME" : "Chaos hammer (8th)", "VALUE" : "24000 sp"},
    "(95,95)" : 	{"NAME" : "Holy smite (8th)", "VALUE" : "24000 sp"},
    "(96,96)" : 	{"NAME" : "Order’s wrath (8th)", "VALUE" : "24000 sp"},
    "(97,97)" : 	{"NAME" : "Unholy blight (8th)", "VALUE" : "24000 sp"},
    "(98,99)" : 	{"NAME" : "Restoration", "VALUE" : "26000 sp"},
    "(100,100)" : 	{"NAME" : "Stoneskin", "VALUE" : "33500 sp"}
}


def _calc_wand_value(start_value, num_charges):
    coins_as_cp = convert_coins_to_cp(start_value)
    one_charge_val = coins_as_cp / 50
    new_val = one_charge_val * num_charges
    return round_coins(new_val)


def roll_wand(result : MapList, table):
    item_data = roll_table(table)
    # calculate number of charges
    num_charges = randint(1,50)
    item_data["NAME"] = "Want of " + item_data["NAME"] + f" with {num_charges} charges"
    start_value = item_data["VALUE"]
    new_value = _calc_wand_value(start_value, num_charges)
    item_data["VALUE"] = new_value
    result.add(item_data["NAME"], item_data["VALUE"])


def roll_minor_wand(result : MapList):
    roll_wand(result, WANDS_MINOR)


def roll_medium_wand(result : MapList):
    roll_wand(result, WANDS_MEDIUM)


def roll_major_wand(result : MapList):
    roll_wand(result, WANDS_MAJOR)
