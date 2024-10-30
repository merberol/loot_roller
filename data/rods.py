from utils.map_list import MapList
from utils.utils import roll_table
from utils.utils import convert_coins_to_cp, round_coins

RODS_MEDIUM = {
    "(1,7)" : 	{"NAME" : "Metamagic, Enlarge, lesser", "VALUE" : "300 gp"},
    "(8,14)" : 	{"NAME" : "Metamagic, Extend, lesser", "VALUE" : "300 gp"},
    "(15,21)" : 	{"NAME" : "Metamagic, Silent, lesser", "VALUE" : "300 gp"},
    "(22,28)" : 	{"NAME" : "Immovable", "VALUE" : "500 gp"},
    "(29,35)" : 	{"NAME" : "Metamagic, Empower, lesser", "VALUE" : "900 gp"},
    "(36,42)" : 	{"NAME" : "Metal and mineral detection	", "VALUE" : "050 gp"},
    "(43,53)" : 	{"NAME" : "Cancellation	", "VALUE" : "100 gp"},
    "(54,57)" : 	{"NAME" : "Metamagic, Enlarge	", "VALUE" : "100 gp"},
    "(58,61)" : 	{"NAME" : "Metamagic, Extend	", "VALUE" : "100 gp"},
    "(62,65)" : 	{"NAME" : "Metamagic, Silent	", "VALUE" : "100 gp"},
    "(66,71)" : 	{"NAME" : "Wonder	", "VALUE" : "200 gp"},
    "(72,79)" : 	{"NAME" : "Python	", "VALUE" : "300 gp"},
    "(80,83)" : 	{"NAME" : "Metamagic, Maximize, lesser	", "VALUE" : "400 gp"},
    "(84,89)" : 	{"NAME" : "Flame extinguishing	", "VALUE" : "500 gp"},
    "(90,97)" : 	{"NAME" : "Viper	", "VALUE" : "900 gp"},
    "(98,99)" : 	{"NAME" : "Metamagic, Empower	", "VALUE" : "250 gp"},
    "(100,100)" : 	{"NAME" : "Metamagic, Quicken, lesser	", "VALUE" : "500 gp"}
}

RODS_MAJOR = {
    "(1,4)" : 	{"NAME" : "Cancellation", "VALUE" : "1100 gp"},
    "(5,6)" : 	{"NAME" : "Metamagic, Enlarge", "VALUE" : "1100 gp"},
    "(7,8)" : 	{"NAME" : "Metamagic, Extend", "VALUE" : "1100 gp"},
    "(9,10)" : 	{"NAME" : "Metamagic, Silent", "VALUE" : "1100 gp"},
    "(11,14)" : 	{"NAME" : "Wonder", "VALUE" : "1200 gp"},
    "(15,18)" : 	{"NAME" : "Python", "VALUE" : "1300 gp"},
    "(19,21)" : 	{"NAME" : "Flame extinguishing", "VALUE" : "1500 gp"},
    "(22,25)" : 	{"NAME" : "Viper", "VALUE" : "1900 gp"},
    "(26,30)" : 	{"NAME" : "Enemy detection", "VALUE" : "2350 gp"},
    "(31,36)" : 	{"NAME" : "Metamagic, Enlarge, greater", "VALUE" : "2450 gp"},
    "(37,42)" : 	{"NAME" : "Metamagic, Extend, greater", "VALUE" : "2450 gp"},
    "(43,48)" : 	{"NAME" : "Metamagic, Silent, greater", "VALUE" : "2450 gp"},
    "(49,53)" : 	{"NAME" : "Splendor", "VALUE" : "2500 gp"},
    "(54,58)" : 	{"NAME" : "Withering", "VALUE" : "2500 gp"},
    "(59,64)" : 	{"NAME" : "Metamagic, Empower", "VALUE" : "3250 gp"},
    "(65,69)" : 	{"NAME" : "Thunder and lightning", "VALUE" : "3300 gp"},
    "(70,73)" : 	{"NAME" : "Metamagic, Quicken, lesser", "VALUE" : "3500 gp"},
    "(74,77)" : 	{"NAME" : "Negation", "VALUE" : "3700 gp"},
    "(78,80)" : 	{"NAME" : "Absorption", "VALUE" : "5000 gp"},
    "(81,84)" : 	{"NAME" : "Flailing", "VALUE" : "5000 gp"},
    "(85,86)" : 	{"NAME" : "Metamagic, Maximize", "VALUE" : "5400 gp"},
    "(87,88)" : 	{"NAME" : "Rulership", "VALUE" : "6000 gp"},
    "(89,90)" : 	{"NAME" : "Security", "VALUE" : "6100 gp"},
    "(91,92)" : 	{"NAME" : "Lordly might", "VALUE" : "7000 gp"},
    "(93,94)" : 	{"NAME" : "Metamagic, Empower, greater", "VALUE" : "7300 gp"},
    "(95,96)" : 	{"NAME" : "Metamagic, Quicken", "VALUE" : "7550 gp"},
    "(97,98)" : 	{"NAME" : "Alertness", "VALUE" : "8500 gp"},
    "(99,99)" : 	{"NAME" : "Metamagic, Maximize, greater", "VALUE" : "12150 gp"},
    "(100,100)" : 	{"NAME" : "Metamagic, Quicken, greater", "VALUE" : "17000 gp"}
}


def roll_rod(result : MapList, table : dict) -> None:
    item_data = roll_table(table)
    item_data["VALUE"] = round_coins(
        convert_coins_to_cp(
            item_data["VALUE"]
        )
    )
    result.add(item_data["NAME"], item_data["VALUE"])

def roll_medium_rod(result : MapList):
    roll_rod(result, RODS_MEDIUM)


def roll_major_rod(result : MapList):
    roll_rod(result, RODS_MAJOR)