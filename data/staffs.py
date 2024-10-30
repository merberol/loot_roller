from utils.map_list import MapList
from utils.utils import convert_coins_to_cp, round_coins, roll_table


STAFFS_MEDIUM = {
    "(1,15)" : 	{"NAME" : "Charming", "VALUE" : "1650 gp"},
    "(16,30)" : 	{"NAME" : "Fire", "VALUE" : "2850 gp"},
    "(31,40)" : 	{"NAME" : "Swarming insects", "VALUE" : "2475 gp"},
    "(41,60)" : 	{"NAME" : "Healing", "VALUE" : "2775 gp"},
    "(61,75)" : 	{"NAME" : "Size alteration", "VALUE" : "2900 gp"},
    "(76,90)" : 	{"NAME" : "Illumination", "VALUE" : "4825 gp"},
    "(91,95)" : 	{"NAME" : "Frost", "VALUE" : "5625 gp"},
    "(96,100)" : 	{"NAME" : "Defense", "VALUE" : "5825 gp"}
}


STAFFS_MAJOR = {
    "(1,3)" : 	{"NAME" : "Charming", "VALUE" : "1650 gp"},
    "(4,9)" : 	{"NAME" : "Fire", "VALUE" : "2850 gp"},
    "(10,11)" : 	{"NAME" : "Swarming insects", "VALUE" : "2475 gp"},
    "(12,17)" : 	{"NAME" : "Healing", "VALUE" : "2775 gp"},
    "(18,19)" : 	{"NAME" : "Size alteration", "VALUE" : "2900 gp"},
    "(20,24)" : 	{"NAME" : "Illumination", "VALUE" : "4825 gp"},
    "(25,31)" : 	{"NAME" : "Frost", "VALUE" : "5625 gp"},
    "(32,38)" : 	{"NAME" : "Defense", "VALUE" : "5825 gp"},
    "(39,43)" : 	{"NAME" : "Abjuration", "VALUE" : "6500 gp"},
    "(44,48)" : 	{"NAME" : "Conjuration", "VALUE" : "6500 gp"},
    "(49,53)" : 	{"NAME" : "Enchantment", "VALUE" : "6500 gp"},
    "(54,58)" : 	{"NAME" : "Evocation", "VALUE" : "6500 gp"},
    "(59,63)" : 	{"NAME" : "Illusion", "VALUE" : "6500 gp"},
    "(64,68)" : 	{"NAME" : "Necromancy", "VALUE" : "6500 gp"},
    "(69,73)" : 	{"NAME" : "Transmutation", "VALUE" : "6500 gp"},
    "(74,77)" : 	{"NAME" : "Divination", "VALUE" : "7350 gp"},
    "(78,82)" : 	{"NAME" : "Earth and stone", "VALUE" : "8050 gp"},
    "(83,87)" : 	{"NAME" : "Woodlands", "VALUE" : "10125 gp"},
    "(88,92)" : 	{"NAME" : "Life", "VALUE" : "15575 gp"},
    "(93,97)" : 	{"NAME" : "Passage", "VALUE" : "17050 gp"},
    "(98,100)" : 	{"NAME" : "Power", "VALUE" : "21100 gp"}
}



def roll_staff(result : MapList, table):
    item_data = roll_table(table)
    item_data["VALUE"] = round_coins(
        convert_coins_to_cp(
            item_data["VALUE"]
        )
    )
    result.add(item_data["NAME"], item_data["VALUE"])



def roll_medium_staff(result : MapList):
    roll_staff(result, STAFFS_MEDIUM)


def roll_major_staff(result : MapList):
    roll_staff(result , STAFFS_MAJOR)