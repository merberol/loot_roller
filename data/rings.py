from utils.map_list import MapList
from utils.utils import roll_table

RINGS_MINOR = {
    "(1,18)" : {"NAME" : "Protection +1", "VALUE" : "200 gp"},
    "(19,28)" : {"NAME" : "Feather falling", "VALUE" : "200 gp"},
    "(29,36)" : {"NAME" : "Sustenance", "VALUE" : "250 gp"},
    "(37,44)" : {"NAME" : "Climbing", "VALUE" : "250 gp"},
    "(45,52)" : {"NAME" : "Jumping", "VALUE" : "250 gp"},
    "(53,60)" : {"NAME" : "Swimming", "VALUE" : "250 gp"},
    "(61,70)" : {"NAME" : "Counterspells", "VALUE" : "400 gp"},
    "(71,75)" : {"NAME" : "Mind shielding", "VALUE" : "800 gp"},
    "(76,80)" : {"NAME" : "Protection +2", "VALUE" : "800 gp"},
    "(81,85)" : {"NAME" : "Force shield", "VALUE" : "850 gp"},
    "(86,90)" : {"NAME" : "Ram", "VALUE" : "860 gp"},
    "(91,93)" : {"NAME" : "Animal friendship", "VALUE" : "1080 gp"},
    "(94,96)" : {"NAME" : "Energy resistance, minor", "VALUE" : "1200 gp"},
    "(97,98)" : {"NAME" : "Chameleon power", "VALUE" : "1270 gp"},
    "(99,100)" : {"NAME" : "Water walking", "VALUE" : "1500 gp"}
}

RINGS_MEDIUM = {
    "(1,5)" : {"NAME" : "Counterspells", "VALUE" : "400 gp"},
    "(6,8)" : {"NAME" : "Mind shielding", "VALUE" : "800 gp"},
    "(9,18)" : {"NAME" : "Protection +2", "VALUE" : "800 gp"},
    "(19,23)" : {"NAME" : "Force shield", "VALUE" : "850 gp"},
    "(24,28)" : {"NAME" : "Ram", "VALUE" : "860 gp"},
    "(29,34)" : {"NAME" : "Climbing, improved", "VALUE" : "1000 gp"},
    "(35,40)" : {"NAME" : "Jumping, improved", "VALUE" : "1000 gp"},
    "(41,46)" : {"NAME" : "Swimming, improved", "VALUE" : "1000 gp"},
    "(47,51)" : {"NAME" : "Animal friendship", "VALUE" : "1080 gp"},
    "(52,56)" : {"NAME" : "Energy resistance, minor", "VALUE" : "1200 gp"},
    "(57,61)" : {"NAME" : "Chameleon power", "VALUE" : "1270 gp"},
    "(62,66)" : {"NAME" : "Water walking", "VALUE" : "1500 gp"},
    "(67,71)" : {"NAME" : "Protection +3", "VALUE" : "1800 gp"},
    "(72,76)" : {"NAME" : "Spell storing, minor", "VALUE" : "1800 gp"},
    "(77,81)" : {"NAME" : "Invisibility", "VALUE" : "2000 gp"},
    "(82,85)" : {"NAME" : "Wizardry (I)", "VALUE" : "2000 gp"},
    "(86,89)" : {"NAME" : "Evasion", "VALUE" : "2500 gp"},
    "(90,92)" : {"NAME" : "X-ray vision", "VALUE" : "2500 gp"},
    "(93,95)" : {"NAME" : "Blinking", "VALUE" : "2700 gp"},
    "(96,98)" : {"NAME" : "Meld into Stone", "VALUE" : "2700 gp"},
    "(99,100)" : {"NAME" : "Energy resistance, major", "VALUE" : "2800 gp"}
}

RINGS_MAJOR = {
    "(1,2)" : {"NAME" : "Energy resistance, minor", "VALUE" : "1200 gp"},
    "(3,7)" : {"NAME" : "Protection +3", "VALUE" : "1800 gp"},
    "(8,10)" : {"NAME" : "Spell storing, minor", "VALUE" : "1800 gp"},
    "(11,15)" : {"NAME" : "Invisibility", "VALUE" : "2000 gp"},
    "(16,19)" : {"NAME" : "Wizardry (I)", "VALUE" : "2000 gp"},
    "(20,25)" : {"NAME" : "Evasion", "VALUE" : "2500 gp"},
    "(26,28)" : {"NAME" : "X-ray vision", "VALUE" : "2500 gp"},
    "(29,32)" : {"NAME" : "Blinking", "VALUE" : "2700 gp"},
    "(33,36)" : {"NAME" : "Meld into Stone", "VALUE" : "2700 gp"},
    "(37,43)" : {"NAME" : "Energy resistance, major", "VALUE" : "2800 gp"},
    "(44,50)" : {"NAME" : "Protection +4", "VALUE" : "3200 gp"},
    "(51,55)" : {"NAME" : "Wizardry (II)", "VALUE" : "4000 gp"},
    "(56,60)" : {"NAME" : "Freedom of movement", "VALUE" : "4000 gp"},
    "(61,63)" : {"NAME" : "Energy resistance, greater", "VALUE" : "4400 gp"},
    "(64,65)" : {"NAME" : "Friend shield (pair)", "VALUE" : "5000 gp"},
    "(66,70)" : {"NAME" : "Protection +5", "VALUE" : "5000 gp"},
    "(71,74)" : {"NAME" : "Shooting stars", "VALUE" : "5000 gp"},
    "(75,79)" : {"NAME" : "Spell storing", "VALUE" : "5000 gp"},
    "(80,83)" : {"NAME" : "Wizardry (III)", "VALUE" : "7000 gp"},
    "(84,86)" : {"NAME" : "Telekinesis", "VALUE" : "7500 gp"},
    "(87,88)" : {"NAME" : "Regeneration", "VALUE" : "9000 gp"},
    "(89,89)" : {"NAME" : "Three wishes", "VALUE" : "9795 gp"},
    "(90,92)" : {"NAME" : "Spell turning", "VALUE" : "9828 gp"},
    "(93,94)" : {"NAME" : "Wizardry (IV)", "VALUE" : "10000 gp"},
    "(95,95)" : {"NAME" : "Djinni calling", "VALUE" : "12500 gp"},
    "(96,96)" : {"NAME" : "Elemental command (air)", "VALUE" : "20000 gp"},
    "(97,97)" : {"NAME" : "Elemental command (earth)", "VALUE" : "20000 gp"},
    "(98,98)" : {"NAME" : "Elemental command (fire)", "VALUE" : "20000 gp"},
    "(99,99)" : {"NAME" : "Elemental command (water)", "VALUE" : "20000 gp"},
    "(100,100)" : {"NAME" : "Spell storing, major", "VALUE" : "20000 gp"}
}


def roll_ring(result : MapList, ring_table):
    item_data = roll_table(ring_table)
    result.add(item_data["NAME"], item_data["VALUE"])


def roll_minor_ring(result : MapList):
    roll_ring(result, RINGS_MINOR)


def roll_medium_ring(result : MapList):
    roll_ring(result, RINGS_MEDIUM)


def roll_major_ring(result : MapList):
    roll_ring(result, RINGS_MAJOR)
