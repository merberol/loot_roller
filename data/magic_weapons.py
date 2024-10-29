from data.mundane_weapons import *
from utils.map_list import MapList
from utils.utils import roll_table, add_coins, add_spec_abilities, special_ability_and_roll_again

WEAPON_COSTS_BY_BONUS = {
    "+1" : "200 gp",
    "+2" : "800 gp",
    "+3" : "1800 gp",
    "+4" : "3200 gp",
    "+5" : "5000 gp",
    "+6" : "7200 gp",
    "+7" : "9800 gp",
    "+8" : "12800 gp",
    "+9" : "16200 gp",
    "+10" : "20000 gp"
}

DESIGNATED_FOE_TABLE = {
    "(1,5)"	: "Aberrations",
    "(6,9)"	: "Animals",
    "(10,16)"	: "Constructs",
    "(17,22)"	: "Dragons",
    "(23,27)"	: "Elementals",
    "(28,32)"	: "Fey",
    "(33,39)"	: "Giants",
    "(40,40)"	: "Humanoids, aquatic",
    "(41,42)"	: "Humanoids, dwarf",
    "(43,44)"	: "Humanoids, elf",
    "(45,45)"	: "Humanoids, gnoll",
    "(46,46)"	: "Humanoids, gnome",
    "(47,49)"	: "Humanoids, goblinoid",
    "(50,50)"	: "Humanoids, halfling",
    "(51,54)"	: "Humanoids, human",
    "(55,57)"	: "Humanoids, reptilian",
    "(58,60)"	: "Humanoids, orc",
    "(61,65)"	: "Magical beasts",
    "(66,70)"	: "Monstrous humanoids",
    "(71,72)"	: "Oozes",
    "(73,73)"	: "Outsiders, air",
    "(74,76)"	: "Outsiders, chaotic",
    "(77,73)"	: "Outsiders, earth",
    "(78,80)"	: "Outsiders, evil",
    "(81,81)"	: "Outsiders, fire",
    "(82,84)"	: "Outsiders, good",
    "(85,87)"	: "Outsiders, lawful",
    "(88,88)"	: "Outsiders, water",
    "(89,90)"	: "Plants",
    "(91,98)"	: "Undead",
    "(99,100)"	: "Vermin"
}

MELEE_WEAPON_SPECIAL_ABILITIES_MINOR = {
    "(1,10)" : {"NAME" : "Bane", "VALUE" : "+1 bonus"},
    "(11,17)" : {"NAME" : "Defending", "VALUE" : "+1 bonus"},
    "(18,27)" : {"NAME" : "Flaming", "VALUE" : "+1 bonus"},
    "(28,37)" : {"NAME" : "Frost", "VALUE" : "+1 bonus"},
    "(38,47)" : {"NAME" : "Shock", "VALUE" : "+1 bonus"},
    "(48,56)" : {"NAME" : "Ghost touch", "VALUE" : "+1 bonus"},
    "(57,67)" : {"NAME" : "Keen", "VALUE" : "+1 bonus"},
    "(68,71)" : {"NAME" : "Ki Focus", "VALUE" : "+1 bonus"},
    "(72,75)" : {"NAME" : "Merciful", "VALUE" : "+1 bonus"},
    "(76,82)" : {"NAME" : "Mighty cleaving", "VALUE" : "+1 bonus"},
    "(83,87)" : {"NAME" : "Spell storing", "VALUE" : "+1 bonus"},
    "(88,91)" : {"NAME" : "Throwing", "VALUE" : "+1 bonus"},
    "(92,95)" : {"NAME" : "Thundering", "VALUE" : "+1 bonus"},
    "(96,99)" : {"NAME" : "Vicious", "VALUE" : "+1 bonus"},
    "(100,100)" : {"NAME" : "Roll again twice"}
}

MELEE_WEAPON_SPECIAL_ABILITIES_MEDIUM = {
    "(1-6)" : {"NAME" : "Bane", "VALUE" : "+1 bonus"},
    "(7-12)" : {"NAME" : "Defending", "VALUE" : "+1 bonus"},
    "(13-19)" : {"NAME" : "Flaming", "VALUE" : "+1 bonus"},
    "(20-26)" : {"NAME" : "Frost", "VALUE" : "+1 bonus"},
    "(27-33)" : {"NAME" : "Shock", "VALUE" : "+1 bonus"},
    "(34-38)" : {"NAME" : "Ghost touch", "VALUE" : "+1 bonus"},
    "(39-44)" : {"NAME" : "Keen", "VALUE" : "+1 bonus"},
    "(45-48)" : {"NAME" : "Ki Focus", "VALUE": "+1 bonus"},
    "(49-50)" : {"NAME" : "Merciful", "VALUE" : "+1 bonus"},
    "(51-54)" : {"NAME" : "Mighty cleaving", "VALUE" : "+1 bonus"},
    "(55-59)" : {"NAME" : "Spell storing", "VALUE" : "+1 bonus"},
    "(60-63)" : {"NAME" : "Throwing",  "VALUE" : "+1 bonus"},
    "(64-65)" : {"NAME" : "Thundering",  "VALUE" : "+1 bonus"},
    "(66-69)" : {"NAME" : "Vicious", "VALUE" : "+1 bonus"},
    "(70-72)" : {"NAME" : "Anarchic", "VALUE" : "+2 bonus"},
    "(73-75)" : {"NAME" : "Axiomatic", "VALUE" : "+2 bonus"},
    "(76-78)" : {"NAME" : "Disruption", "VALUE" : "+2 bonus"},
    "(79-81)" : {"NAME" : "Flaming burst", "VALUE" : "+2 bonus"},
    "(82-84)" : {"NAME" : "Icy burst", "VALUE" : "+2 bonus"},
    "(85-87)" : {"NAME" : "Holy", "VALUE" : "+2 bonus"},
    "(88-90)" : {"NAME" : "Shocking burst", "VALUE" : "+2 bonus"},
    "(91-93)" : {"NAME" : "Unholy", "VALUE" : "+2 bonus"},
    "(94-95)" : {"NAME" : "Wounding", "VALUE" : "+2 bonus"},
    "(96-100)" : {"NAME" : "Roll again twice"}
}

MELEE_WEAPON_SPECIAL_ABILITIES_MAJOR = {
    "(1,3)" : {"NAME" : "Bane", "VALUE" : "+1 bonus"},
    "(4,6)" : {"NAME" : "Flaming", "VALUE" : "+1 bonus"},
    "(7,9)" : {"NAME" : "Frost", "VALUE" : "+1 bonus"},
    "(10,12)" : {"NAME" : "Shock", "VALUE" : "+1 bonus"},
    "(13,15)" : {"NAME" : "Ghost touch", "VALUE" : "+1 bonus"},
    "(16,19)" : {"NAME" : "Ki Focus", "VALUE" : "+1 bonus"},
    "(20,21)" : {"NAME" : "Mighty cleaving", "VALUE" : "+1 bonus"},
    "(22,24)" : {"NAME" : "Spell storing", "VALUE" : "+1 bonus"},
    "(25,28)" : {"NAME": "Throwing", "VALUE" : "+1 bonus"},
    "(29,32)" : {"NAME": "Thundering", "VALUE" : "+1 bonus"},
    "(33,36)" : {"NAME": "Vicious", "VALUE" : "+1 bonus"},
    "(37,41)" : {"NAME": "Anarchic", "VALUE" : "+2 bonus"},
    "(42,46)" : {"NAME": "Axiomatic", "VALUE" : "+2 bonus"},
    "(47,49)" : {"NAME": "Disruption", "VALUE" : "+2 bonus"},
    "(50,54)" : {"NAME" : "Flaming burst", "VALUE" : "+2 bonus"},
    "(55,59)" : {"NAME" : "Icy burst", "VALUE" : "+2 bonus"},
    "(60,64)" : {"NAME" : "Holy", "VALUE" : "+2 bonus"},
    "(65,69)" : {"NAME" : "Shocking burst", "VALUE" : "+2 bonus"},
    "(70,74)" : {"NAME" : "Unholy", "VALUE" : "+2 bonus"},
    "(75,78)" : {"NAME" : "Wounding", "VALUE" : "+2 bonus"},
    "(79,83)" : {"NAME" : "Speed", "VALUE" : "+3 bonus"},
    "(84,86)" : {"NAME" : "Brilliant energy", "VALUE" : "+4 bonus"},
    "(87,88)" : {"NAME" : "Dancing", "VALUE" : "+4 bonus"},
    "(89,90)" : {"NAME" : "Vorpal4", "VALUE" : "+5 bonus"},
    "(91,100)" : {"NAME" : "Roll again twice"}
}

RANGED_WEAPON_SPECIAL_ABILITIES_MINOR = {
    "(1,12)" : {"NAME" : "Bane", "VALUE" : "+1 bonus"},
    "(13,25)" : {"NAME" : "Distance", "VALUE" : "+1 bonus"},
    "(26,40)" : {"NAME" : "Flaming", "VALUE" : "+1 bonus"},
    "(41,55)" : {"NAME" : "Frost", "VALUE" : "+1 bonus"},
    "(56,60)" : {"NAME" : "Merciful", "VALUE" : "+1 bonus"},
    "(61,68)" : {"NAME" : "Returning", "VALUE" : "+1 bonus"},
    "(69,83)" : {"NAME" : "Shock", "VALUE" : "+1 bonus"},
    "(84,93)" : {"NAME" : "Seeking", "VALUE" : "+1 bonus"},
    "(94,99)" : {"NAME" : "Thundering", "VALUE" : "+1 bonus"},
    "(100,100)" : {"NAME" : "Roll again twice"}
}

RANGED_WEAPON_SPECIAL_ABILITIES_MEDIUM = {
    "(1,8)" : {"NAME" : "Bane", "VALUE" : "+1 bonus"},
    "(9,16)" : {"NAME" : "Distance", "VALUE" : "+1 bonus"},
    "(17,28)" : {"NAME" : "Flaming", "VALUE" : "+1 bonus"},
    "(29,40)" : {"NAME" : "Frost", "VALUE" : "+1 bonus"},
    "(41,42)" : {"NAME" : "Merciful", "VALUE" : "+1 bonus"},
    "(43,47)" : {"NAME" : "Returning", "VALUE" : "+1 bonus"},
    "(48,59)" : {"NAME" : "Shock", "VALUE" : "+1 bonus"},
    "(60,64)" : {"NAME" : "Seeking", "VALUE" : "+1 bonus"},
    "(65,68)" : {"NAME" : "Thundering", "VALUE" : "+1 bonus"},
    "(69,71)" : {"NAME" : "Anarchic", "VALUE" : "+2 bonus"},
    "(72,74)" : {"NAME" : "Axiomatic", "VALUE" : "+2 bonus"},
    "(75,79)" : {"NAME" : "Flaming burst", "VALUE" : "+2 bonus"},
    "(80,82)" : {"NAME" : "Holy", "VALUE" : "+2 bonus"},
    "(83,87)" : {"NAME" : "Icy burst", "VALUE" : "+2 bonus"},
    "(88,92)" : {"NAME" : "Shocking burst", "VALUE" : "+2 bonus"},
    "(93,95)" : {"NAME" : "Unholy", "VALUE" : "+2 bonus"},
    "(96,100)" : {"NAME" : "Roll again twice"}
}

RANGED_WEAPON_SPECIAL_ABILITIES_MAJOR = {
    "(01,04)" : {"NAME" : "Bane", "VALUE" : "+1 bonus"},
    "(05,08)" : {"NAME" : "Distance", "VALUE" : "+1 bonus"},
    "(09,12)" : {"NAME" : "Flaming", "VALUE" : "+1 bonus"},
    "(13,16)" : {"NAME" : "Frost", "VALUE" : "+1 bonus"},
    "(17,21)" : {"NAME" : "Returning", "VALUE" : "+1 bonus"},
    "(22,25)" : {"NAME" : "Shock", "VALUE" : "+1 bonus"},
    "(26,27)" : {"NAME" : "Seeking", "VALUE" : "+1 bonus"},
    "(28,29)" : {"NAME" : "Thundering", "VALUE" : "+1 bonus"},
    "(30,34)" : {"NAME" : "Anarchic", "VALUE" : "+2 bonus"},
    "(35,39)" : {"NAME" : "Axiomatic", "VALUE" : "+2 bonus"},
    "(40,49)" : {"NAME" : "Flaming burst", "VALUE" : "+2 bonus"},
    "(50,54)" : {"NAME" : "Holy", "VALUE" : "+2 bonus"},
    "(55,64)" : {"NAME" : "Icy burst", "VALUE" : "+2 bonus"},
    "(65,74)" : {"NAME" : "Shocking burst", "VALUE" : "+2 bonus"},
    "(75,79)" : {"NAME" : "Unholy", "VALUE" : "+2 bonus"},
    "(80,84)" : {"NAME" : "Speed", "VALUE" : "+3 bonus"},
    "(85,90)" : {"NAME" : "Brilliant energy", "VALUE" : "+4 bonus"},
    "(91,100)" : {"NAME" : "Roll again twice"}
}

SPECIFIC_WEAPONS_MINOR = {
"(01,15)" : {"NAME" : "Sleep arrow", "VALUE" : "132 sp"},
"(16,25)" : {"NAME" : "Screaming bolt", "VALUE" : "267 sp"},
"(26,45)" : {"NAME" : "Silver dagger, masterwork", "VALUE" : "322 sp"},
"(46,65)" : {"NAME" : "Cold iron longsword, masterwork", "VALUE" : "330 sp"},
"(66,75)" : {"NAME" : "Javelin of lightning", "VALUE" : "1500 sp"},
"(76,80)" : {"NAME" : "Slaying arrow", "VALUE" : "2282 sp"},
"(81,90)" : {"NAME" : "Adamantine dagger", "VALUE" : "3002 sp"},
"(91,100)" : {"NAME" : "Adamantine battleaxe", "VALUE" : "3010 sp"}
}

SPECIFIC_WEAPONS_MEDIUM = {
"(01,09)" : {"NAME" : "Javelin of lightning", "VALUE" : "1500 sp"},
"(10,15)" : {"NAME" : "Slaying arrow", "VALUE" : "2282 sp"},
"(16,24)" : {"NAME" : "Adamantine dagger", "VALUE" : "3002 sp"},
"(25,33)" : {"NAME" : "Adamantine battleaxe", "VALUE" : "3010 sp"},
"(34,37)" : {"NAME" : "Slaying arrow (greater)", "VALUE" : "4057 sp"},
"(38,40)" : {"NAME" : "Shatterspike", "VALUE" : "4315 sp"},
"(41,46)" : {"NAME" : "Dagger of venom", "VALUE" : "8302 sp"},
"(47,51)" : {"NAME" : "Trident of warning", "VALUE" : "10115 sp"},
"(52,57)" : {"NAME" : "Assassin’s dagger", "VALUE" : "10302 sp"},
"(58,62)" : {"NAME" : "Shifter’s sorrow", "VALUE" : "12780 sp"},
"(63,66)" : {"NAME" : "Trident of fish command", "VALUE" : "18650 sp"},
"(67,74)" : {"NAME" : "Flame tongue", "VALUE" : "20715 sp"},
"(75,79)" : {"NAME" : "Luck blade (0 wishes)", "VALUE" : "22060 sp"},
"(80,86)" : {"NAME" : "Sword of subtlety", "VALUE" : "22310 sp"},
"(87,91)" : {"NAME" : "Sword of the planes", "VALUE" : "22315 sp"},
"(92,95)" : {"NAME" : "Nine lives stealer", "VALUE" : "23057 sp"},
"(96,98)" : {"NAME" : "Sword of life stealing", "VALUE" : "25715 sp"},
"(99,100)" : {"NAME" : "Oathbow", "VALUE" : "25600 sp"}
}

SPECIFIC_WEAPONS_MAJOR = {
    "(01,04)" : {"NAME" : "Assassin’s dagger", "VALUE" : "10302 sp"},
    "(05,07)" : {"NAME" : "Shifter’s sorrow", "VALUE" : "12780 sp"},
    "(08,09)" : {"NAME" : "Trident of fish command", "VALUE" : "18650 sp"},
    "(10,13)" : {"NAME" : "Flame tongue", "VALUE" : "20715 sp"},
    "(14,17)" : {"NAME" : "Luck blade (0 wishes)", "VALUE" : "22060 sp"},
    "(18,24)" : {"NAME" : "Sword of subtlety", "VALUE" : "22310 sp"},
    "(25,31)" : {"NAME" : "Sword of the planes", "VALUE" : "22315 sp"},
    "(32,37)" : {"NAME" : "Nine lives stealer", "VALUE" : "23057 sp"},
    "(38,42)" : {"NAME" : "Sword of life stealing", "VALUE" : "25715 sp"},
    "(43,46)" : {"NAME" : "Oathbow", "VALUE" : "25600 sp"},
    "(47,51)" : {"NAME" : "Mace of terror", "VALUE" : "38552 sp"},
    "(52,57)" : {"NAME" : "Life-drinker", "VALUE" : "40320 sp"},
    "(58,62)" : {"NAME" : "Sylvan scimitar", "VALUE" : "47315 sp"},
    "(63,67)" : {"NAME" : "Rapier of puncturing", "VALUE" : "50320 sp"},
    "(68,73)" : {"NAME" : "Sun blade", "VALUE" : "50335 sp"},
    "(74,79)" : {"NAME" : "Frost brand", "VALUE" : "54475 sp"},
    "(80,84)" : {"NAME" : "Dwarven thrower", "VALUE" : "60312 sp"},
    "(85,91)" : {"NAME" : "Luck blade (1 wish)", "VALUE" : "62360 sp"},
    "(92,95)" : {"NAME" : "Mace of smiting", "VALUE" : "75312 sp"},
    "(96,97)" : {"NAME" : "Luck blade (2 wishes)", "VALUE" : "102660 sp"},
    "(98,99)" : {"NAME" : "Holy avenger", "VALUE" : "120630 sp"},
    "(100,100)" : {"NAME" : "Luck blade (3 wishes)", "VALUE" : "142960 sp"}
}

WEAPONS_MINOR = {
    "(1,70)"  : {"NAME" : "+1",  "VALUE" : "200 gp"},
    "(71,85)"  : {"NAME" : "+2", "VALUE" : "800 gp"},
    "(86,90)"  : {"NAME" : "Specific weapon", "VALUE" : SPECIFIC_WEAPONS_MINOR},
    "(91,100)" : {"NAME" : "Special ability and roll again"}
}

WEAPONS_MEDIUM = {
    "(1,10)"   : {"NAME" : "+1", "VALUE" : "200 gp"},
    "(11,29)"  : {"NAME" : "+2", "VALUE" : "800 gp"},
    "(30,58)"  : {"NAME" : "+3", "VALUE" : "1800 gp"},
    "(59,62)"  : {"NAME" : "+4", "VALUE" : "3200 gp"},
    "(63,68)"  : {"NAME" : "Specific weapon", "VALUE" : SPECIFIC_WEAPONS_MEDIUM},
    "(69-100)" : {"NAME" : "Special ability and roll again"}
}

WEAPONS_MAJOR = {
    "(01-20)" :  {"NAME" : "+3", "VALUE" : "1800 gp"},
    "(21-38)" :  {"NAME" : "+4", "VALUE" : "3200 gp"},
    "(39-49)" :  {"NAME" : "+5", "VALUE" : "5000 gp"},
    "(50-63)" :  {"NAME" : "Specific weapon", "VALUE" : SPECIFIC_WEAPONS_MAJOR},
    "(64-100)" : {"NAME" : "Special ability and roll again"}
}


def roll_weapon(result : MapList, specific_item_data, weapons_table, spec_ability_table):
    item_data = roll_table(weapons_table)
    spec_abilities = []
    if item_data["NAME"] == "Special ability and roll again":
        data = special_ability_and_roll_again(spec_ability_table, weapons_table)
        spec_abilities = data[0]
        item_data = data[1]

    if type(item_data["VALUE"]) == dict:
        print("Rolling for spcific item")
        item_data = roll_table(item_data["VALUE"])
        if spec_abilities:
           item_data =  add_spec_abilities(item_data, spec_abilities)
        result.add(item_data["NAME"], item_data["VALUE"])
        return

    item_name = item_data["NAME"]
    item_value = item_data["VALUE"]
    bonus = item_name.split()[0]

    print(f"{specific_item_data=}")
    specific_item_data["NAME"] = bonus + " " + specific_item_data["NAME"]
    specific_item_data["VALUE"] = add_coins(item_value, specific_item_data["VALUE"])

    print(specific_item_data)
    item_data =  add_spec_abilities(specific_item_data, spec_abilities)
    result.add(item_data["NAME"], item_data["VALUE"])


def roll_weapon_minor(result : MapList):
    mundane_weapon_type = roll_table(MUNDANE_WEAPONS)
    spec_item_table = None
    
    if "melee" in mundane_weapon_type["NAME"]:
        spec_item_table = MELEE_WEAPON_SPECIAL_ABILITIES_MINOR
    else:
        spec_item_table = RANGED_WEAPON_SPECIAL_ABILITIES_MINOR
    
    mundane_weapon_type = roll_table(mundane_weapon_type["VALUE"])
    roll_weapon(result, mundane_weapon_type, WEAPONS_MINOR, spec_item_table)


def roll_weapon_medium(result : MapList):
    mundane_weapon_type = roll_table(MUNDANE_WEAPONS)
    spec_item_table = None
    if "melee" in mundane_weapon_type["NAME"]:
        spec_item_table = MELEE_WEAPON_SPECIAL_ABILITIES_MEDIUM
    else:
        spec_item_table = RANGED_WEAPON_SPECIAL_ABILITIES_MEDIUM
    
    mundane_weapon_type = roll_table(mundane_weapon_type["VALUE"])
    roll_weapon(result, mundane_weapon_type, WEAPONS_MINOR, spec_item_table)


def roll_weapon_major(result : MapList):
    mundane_weapon_type = roll_table(MUNDANE_WEAPONS)
    spec_item_table = None
    if "melee" in mundane_weapon_type["NAME"]:
        spec_item_table = MELEE_WEAPON_SPECIAL_ABILITIES_MAJOR
    else:
        spec_item_table = RANGED_WEAPON_SPECIAL_ABILITIES_MAJOR
    
    mundane_weapon_type = roll_table(mundane_weapon_type["VALUE"])
    roll_weapon(result, mundane_weapon_type, WEAPONS_MINOR, spec_item_table)
