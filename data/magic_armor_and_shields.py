
from utils.utils import roll_table, add_coins, add_spec_abilities, special_ability_and_roll_again
from utils.map_list import MapList

ARMOR_COSTS_BY_BONUS = {
"+1" : "100 gp",
"+2" : "400 gp",
"+3" : "900 gp",
"+4" : "1600 gp",
"+5" : "2500 gp",
"+6" : "3600 gp",
"+7" : "4900 gp",
"+8" : "6400 gp",
"+9" : "8100 gp",
"+10" : "10000 gp"
}

SPECIFIC_ARMOR_MINOR = {
    "(1,50)"  : {"NAME" : "Mithral shirt",    "VALUE" : "110 gp"},
    "(51,80)"  : {"NAME" : "Dragonhide plate", "VALUE" : "330 gp"},
    "(81,100)" : {"NAME" : "Elven chain",      "VALUE" : "415 gp"}
}

SPECIFIC_SHIELD_MINOR = {
    "(01,30)" :  { "NAME" : "Darkwood buckler",     "VALUE" : "205 sp"},
    "(31,80)" :  { "NAME" : "Darkwood shield",      "VALUE" : "257 sp"},
    "(81,95)" :  { "NAME" : "Mithral heavy shield", "VALUE" : "102 gp"},
    "(96,100)" : { "NAME" : "Caster’s shield",      "VALUE" : "3153 sp"}
}

SPECIFIC_ARMOR_MEDIUM = {
    "(1,25)"   : {"NAME" : "Mithral shirt",          "VALUE" : "110 gp"},
    "(26,45)"  : {"NAME" : "Dragonhide plate",       "VALUE" : "330 gp"},
    "(46,57)"  : {"NAME" : "Elven chain",            "VALUE" : "415 gp"},
    "(58,67)"  : {"NAME" : "Rhino hide",             "VALUE" : "5165 sp"},
    "(68,82)"  : {"NAME" : "Adamantine breastplate", "VALUE" : "1020 gp"},
    "(83,97)"  : {"NAME" : "Dwarven plate",          "VALUE" : "1650 gp"},
    "(98,100)" : {"NAME" : "Banded mail of luck",    "VALUE" : "1890 gp"}
}

SPECIFIC_SHIELD_MEDIUM = {
    "(01-20)"  : {"NAME" : "Darkwood buckler",      "VALUE" : "205 sp"},
    "(21-45)"  : {"NAME" : "Darkwood shield",       "VALUE" : "257 sp"},
    "(46-70)"  : {"NAME" : "Mithral heavy shield",  "VALUE" : "102 gp"},
    "(71-85)"  : {"NAME" : "Caster’s shield",       "VALUE" : "3153 sp"},
    "(86-90)"  : {"NAME" : "Spined shield",         "VALUE" : "558 gp"},
    "(91-95)"  : {"NAME" : "Lion’s shield",         "VALUE" : "917 gp"},
    "(96-100)" : {"NAME" : "Winged shield",         "VALUE" : "17257 sp"}
}

ARMOR_AND_SHIELD_MEDIUM = {
    "(1,5)"    : {"NAME" : "+1 shield", "VALUE" :  "100 gp"},
    "(6,10)"   : {"NAME" : "+1 armor ", "VALUE" :  "100 gp"},
    "(11,20)"  : {"NAME" : "+2 shield", "VALUE" :  "400 gp"},
    "(21,30)"  : {"NAME" : "+2 armor ", "VALUE" :  "400 gp"},
    "(31,40)"  : {"NAME" : "+3 shield", "VALUE" :  "900 gp"},
    "(41,50)"  : {"NAME" : "+3 armor ", "VALUE" :  "900 gp"},
    "(51,55)"  : {"NAME" : "+4 shield", "VALUE" :  "1600 gp"},
    "(56,57)"  : {"NAME" : "+4 armor ", "VALUE" :  "1600 gp"},
    "(58,60)"  : {"NAME" : "Specific armor"},
    "(61,63)"  : {"NAME" : "Specific shield"},
    "(64,100)" : {"NAME" : "Special ability and roll again"}
}

SPECIFIC_ARMOR_MAJOR = {
    "(1,10)"	 : {"NAME" : "Adamantine breastplate", "VALUE" : "1020 gp"},
    "(11,20)"	 : {"NAME" : "Dwarven plate", "VALUE" : "1650 gp"},
    "(21,32)"	 : {"NAME" : "Banded mail of luck", "VALUE" : "1890 gp"},
    "(33,50)"	 : {"NAME" : "Celestial armor", "VALUE" : "2240 gp"},
    "(51,60)"	 : {"NAME" : "Plate armor of the deep", "VALUE" : "2465 gp"},
    "(61,75)"	 : {"NAME" : "Breastplate of command", "VALUE" : "2540 gp"},
    "(76,90)"	 : {"NAME" : "Mithral full plate of speed", "VALUE" : "2650 gp"},
    "(91,100)"	 : {"NAME" : "Demon armor", "VALUE" : "5226 gp"}
}

SPECIFIC_SHIELD_MAJOR = {
    "(1,20)" :  {"NAME": "Caster’s shield",  "VALUE" : "3153 sp"},
    "(21,40)" :  {"NAME": "Spined shield",  "VALUE" : "558 gp"},
    "(41,60)" :  {"NAME": "Lion’s shield",  "VALUE" : "917 gp"},
    "(61,90)" :  {"NAME": "Winged shield",  "VALUE" : "17257 sp"},
    "(91,100)" : {"NAME": "Absorbing shield",  "VALUE" : "5017 gp"}
}
ARMOR_AND_SHIELD_MAJOR = {
    "(1,8)"    : {"NAME" : "+3 shield", "VALUE" : "900 gp"},
    "(9,16)"   : {"NAME" : "+3 armor",  "VALUE" : "900 gp"},
    "(17,27)"  : {"NAME" : "+4 shield", "VALUE" : "1600 gp"},
    "(28,38)"  : {"NAME" : "+4 armor",  "VALUE" : "1600 gp"},
    "(39,49)"  : {"NAME" : "+5 shield", "VALUE" : "2500 gp"},
    "(50,57)"  : {"NAME" : "+5 armor",  "VALUE" : "2500 gp"},
    "(58,60)"  : {"NAME" : "Specific armor"},
    "(61,63)"  : {"NAME" : "Specific shield"},
    "(64,100)" : {"NAME" : "Special ability and roll again"}
}

RANDOM_ARMOR_TYPE = {
    "(1,1)"    : {"NAME" : "Padded",          "VALUE" : "155 sp"},
    "(2,2)"    : {"NAME" : "Leather",         "VALUE" : "16 gp "},
    "(3,17)"   : {"NAME" : "Studded leather", "VALUE" : "175 sp"},
    "(18,32)"  : {"NAME" : "Chain shirt",     "VALUE" : "25 gp "},
    "(33,42)"  : {"NAME" : "Hide",            "VALUE" : "165 sp"},
    "(43,43)"  : {"NAME" : "Scale mail",      "VALUE" : "20 gp "},
    "(44,44)"  : {"NAME" : "Chainmail",       "VALUE" : "30 gp "},
    "(45,57)"  : {"NAME" : "Breastplate",     "VALUE" : "35 gp "},
    "(58,58)"  : {"NAME" : "Splint mail",     "VALUE" : "35 gp "},
    "(59,59)"  : {"NAME" : "Banded mail",     "VALUE" : "40 gp "},
    "(60,60)"  : {"NAME" : "Half-plate",      "VALUE" : "75 gp "},
    "(61,100)" : {"NAME" : "Full plate",      "VALUE" : "165 gp"}
}

RANDOM_SHIELD_TYPE = {
    "(1,10)"   : {"NAME": "Buckler              ", "VALUE" : "165 gp"},
    "(11,15)"  : {"NAME": "Shield, light, wooden", "VALUE" : "153 gp"},
    "(16,20)"  : {"NAME": "Shield, light, steel ", "VALUE" : "159 gp"},
    "(21,30)"  : {"NAME": "Shield, heavy, wooden", "VALUE" : "157 gp"},
    "(31,95)"  : {"NAME": "Shield, heavy, steel ", "VALUE" : "170 gp"},
    "(96,100)" : {"NAME": "Shield, tower        ", "VALUE" : "180 gp"}
}

ARMOR_SPECIAL_ABILITY_MEDIUM = {
    "(1,5)" : {"NAME" :   "Glamered",                 "VALUE" : "270 gp"},
    "(6,8)" : {"NAME" :   "Fortification: light",     "VALUE" : "+1 bonus"},
    "(9,11)" : {"NAME" :  "Slick ",                   "VALUE" : "375 gp"},
    "(12,14)" : {"NAME" : "Shadow",                   "VALUE" : "375 gp"},
    "(15,17)" : {"NAME" : "Silent moves",             "VALUE" : "375 gp"},
    "(18,19)" : {"NAME" : "Spell resistance (13)",    "VALUE" : "+2 bonus"},
    "(20,29)" : {"NAME" : "Slick, improved",          "VALUE" : "1500 gp"},
    "(30,39)" : {"NAME" : "Shadow, improved",         "VALUE" : "1500 gp"},
    "(40,49)" : {"NAME" : "Silent moves, improved",   "VALUE" : "1500 gp"},
    "(50,54)" : {"NAME" : "Acid resistance",          "VALUE" : "1800 gp"},
    "(55,59)" : {"NAME" : "Cold resistance",          "VALUE" : "1800 gp"},
    "(60,64)" : {"NAME" : "Electricity resistance",   "VALUE" : "1800 gp"},
    "(65,69)" : {"NAME" : "Fire resistance",          "VALUE" : "1800 gp"},
    "(70,74)" : {"NAME" : "Sonic resistance",         "VALUE" : "1800 gp"},
    "(75,79)" : {"NAME" : "Ghost touch",              "VALUE" : "+3 bonus"},
    "(80,84)" : {"NAME" : "Invulnerability",          "VALUE" : "+3 bonus"},
    "(85,89)" : {"NAME" : "Fortification, moderate",  "VALUE" : "+3 bonus"},
    "(90,94)" : {"NAME" : "Spell resistance (15)",    "VALUE" : "+3 bonus"},
    "(95,99)" : {"NAME" : "Wild",                     "VALUE" : "+3 bonus"},
    "(100,100)" : {"NAME" : "Roll twice again"}
}

ARMOR_SPECIAL_ABILITY_MAJOR = {
    "(1,3)"     : {"NAME" : "Glamered",                         "VALUE" : "270 gp"},
    "(4,4)"     : {"NAME" : "Fortification: light",             "VALUE" : "+1 bonus"},
    "(5,7)"     : {"NAME" : "Slick: improved",                  "VALUE" : "1500 gp"},
    "(8,10)"    : {"NAME" : "Shadow, improved",                 "VALUE" : "1500 gp"},
    "(11,13)"   : {"NAME" : "Silent moves, improved",           "VALUE" : "1500 gp"},
    "(14,16)"   : {"NAME" : "Acid resistance",                  "VALUE" : "1800 gp"},
    "(17,19)"   : {"NAME" : "Cold resistance",                  "VALUE" : "1800 gp"},
    "(20,22)"   : {"NAME" : "Electricity resistance",           "VALUE" : "1800 gp"},
    "(23,25)"   : {"NAME" : "Fire resistance",                  "VALUE" : "1800 gp"},
    "(26,28)"   : {"NAME" : "Sonic resistance",                 "VALUE" : "1800 gp"},
    "(29,33)"   : {"NAME" : "Ghost touch",                      "VALUE" : "+3 bonus"},
    "(34,35)"   : {"NAME" : "Invulnerability",                  "VALUE" : "+3 bonus"},
    "(36,40)"   : {"NAME" : "Fortification, moderate",          "VALUE" : "+3 bonus"},
    "(41,42)"   : {"NAME" : "Spell resistance (15)",            "VALUE" : "+3 bonus"},
    "(43,43)"   : {"NAME" : "Wild",                             "VALUE" : "+3 bonus"},
    "(44,48)"   : {"NAME" : "Slick, greater",                   "VALUE" : "3375 gp"},
    "(49,53)"   : {"NAME" : "Shadow, greater",                  "VALUE" : "3375 gp"},
    "(54,58)"   : {"NAME" : "Silent moves, greater",            "VALUE" : "3375 gp"},
    "(59,63)"   : {"NAME" : "Acid resistance, improved",        "VALUE" : "4200 gp"},
    "(64,68)"   : {"NAME" : "Cold resistance, improved",        "VALUE" : "4200 gp"},
    "(69,73)"   : {"NAME" : "Electricity resistance, improved", "VALUE" : "4200 gp"},
    "(74,78)"   : {"NAME" : "Fire resistance, improved",        "VALUE" : "4200 gp"},
    "(79,83)"   : {"NAME" : "Sonic resistance, improved",       "VALUE" : "4200 gp"},
    "(84,88)"   : {"NAME" : "Spell resistance (17)",            "VALUE" : "+4 bonus"},
    "(89,89)"   : {"NAME" : "Etherealness",                     "VALUE" : "4900 gp"},
    "(90,90)"   : {"NAME" : "Undead controlling",               "VALUE" : "4900 gp"},
    "(91,92)"   : {"NAME" : "Fortification, heavy",             "VALUE" : "+5 bonus"},
    "(93,94)"   : {"NAME" : "Spell resistance (19)",            "VALUE" : "+5 bonus"},
    "(95,95)"   : {"NAME" : "Acid resistance, greater",         "VALUE" : "6600 gp"},
    "(96,96)"   : {"NAME" : "Cold resistance, greater",         "VALUE" : "6600 gp"},
    "(97,97)"   : {"NAME" : "Electricity resistance, greater",  "VALUE" : "6600 gp"},
    "(98,98)"   : {"NAME" : "Fire resistance, greater",         "VALUE" : "6600 gp"},
    "(99,99)"   : {"NAME" : "Sonic resistance, greater",        "VALUE" : "6600 gp"},
    "(100,100)" : {"NAME" : "Roll twice again"}
}

ARMOR_SPECIAL_ABILITY_MINOR = {
    "(1,25)"   : {"NAME" : "Glamered",                "VALUE" : "270 gp"},
    "(26,32)"   : {"NAME" : "Fortification: light",    "VALUE" : "+1 bonus"},
    "(33,52)"   : {"NAME" : "Slick",                   "VALUE" : "375 gp"},
    "(53,72)"   : {"NAME" : "Shadow",                  "VALUE" : "375 gp"},
    "(73,92)"   : {"NAME" : "Silent moves",            "VALUE" : "375 gp"},
    "(93,96)"   : {"NAME" : "Spell resistance: (13)",  "VALUE" : "+2 bonus"},
    "(97,97)"   : {"NAME" : "Slick: improved",         "VALUE" : "1500 gp"},
    "(98,98)"   : {"NAME" : "Shadow: improved",        "VALUE" : "1500 gp"},
    "(99,99)"   : {"NAME" : "Silent moves: improved",  "VALUE" : "1500 gp"},
    "(100,100)" : {"NAME" : "Roll twice again"}
}

ARMOR_AND_SHIELD_MINOR = {
    "(1,60)"   : {"NAME" : "+1 shield", "VALUE" : "100 gp"},
    "(61,80)"  : {"NAME" : "+1 armor ", "VALUE" : "100 gp"},
    "(81,85)"  : {"NAME" : "+2 shield", "VALUE" : "400 gp"},
    "(86,87)"  : {"NAME" : "+2 armor ", "VALUE" : "400 gp"},
    "(88,89)"  : {"NAME" : "Specific armor", "VALUE": SPECIFIC_ARMOR_MINOR},
    "(90,91)"  : {"NAME" : "Specific shield", "VALUE": SPECIFIC_SHIELD_MINOR},
    "(92,100)" : {"NAME" : "Special ability and roll again"}
}





def roll_armor_and_shield(result : MapList, spec_item_table, armor_and_shield_table) -> bool:
    item_data = roll_table(armor_and_shield_table)
    spec_abilities = []
    if item_data["NAME"] == "Special ability and roll again":
        data = special_ability_and_roll_again(spec_item_table, armor_and_shield_table)
        spec_abilities = data[0]
        item_data = data[1]

    if type(item_data["VALUE"]) == dict:
        print("Rolling for spcific item")
        item_data = roll_table(item_data["VALUE"])
        if spec_abilities:
           item_data =  add_spec_abilities(item_data, spec_abilities)
        result.add(item_data["NAME"], item_data["VALUE"])
        return

    # print(spec_abilities, item_data)

    item_name = item_data["NAME"]
    item_value = item_data["VALUE"]
    bonus = item_name.split()[0]
    item_type = item_name.split()[1]
    specific_item_data = None

    match item_type:
        case "armor":
            specific_item_data = roll_table(RANDOM_ARMOR_TYPE)
        case "shield":
            specific_item_data = roll_table(RANDOM_SHIELD_TYPE)

    if specific_item_data is not None:
        print(f"{specific_item_data=}")
        specific_item_data["NAME"] = bonus + " " + specific_item_data["NAME"]
        specific_item_data["VALUE"] = add_coins(item_value, specific_item_data["VALUE"])

        print(specific_item_data)
        res, item_data = add_spec_abilities(specific_item_data, spec_abilities , ARMOR_COSTS_BY_BONUS)
        if not res:
            return False
        print(item_data)
        result.add(item_data["NAME"], item_data["VALUE"])
        return True


def roll_armor_and_shield_minor(result : MapList):
    res = False
    while not res:
        res = roll_armor_and_shield(result, ARMOR_SPECIAL_ABILITY_MINOR, ARMOR_AND_SHIELD_MINOR)
    
def roll_armor_and_shield_medium(result : MapList):
    res = False
    while not res:
        res = roll_armor_and_shield(result, ARMOR_SPECIAL_ABILITY_MEDIUM, ARMOR_AND_SHIELD_MEDIUM)
    
def roll_armor_and_shield_major(result : MapList):
    res = False
    while not res:
        res = roll_armor_and_shield(result, ARMOR_SPECIAL_ABILITY_MAJOR, ARMOR_AND_SHIELD_MAJOR)
    



