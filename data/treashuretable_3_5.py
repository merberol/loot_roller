
from data import dice 


TREASHURE_START = {
    1:{
        "COINS":{
            "(1,14)"     : "NONE",
            "(15,39)"    : "1 d6 * 100 cp",
            "(40,95)"    : "1 d8 * 10 sp",
            "(96,100)"   : "2 d8 * 1 gp"
        },
        "GOODS":{
            "(1,90)" : "NONE",
            "(91,95)" : "1 gem",
            "(96,100)" : "1 art"
        },
        "ITEMS":{
            "(1,71)" : "NONE",
            "(72,95)" : "1 mundane",
            "(96,100)" : "1 minor"
        }
    },
    2:{
        "COINS":{
            "(1, 13)"     : "NONE",
            "(14, 23)"    : "1 d10 * 100 cp",
            "(24, 43)"    : "2 d10 * 10 sp",
            "(44, 95)"    : "2 d10 * 1 gp",
            "(96, 100)"   : "4 d10 * 1 gp"
        },
        "GOODS":{
            "(1,81)" : "NONE",
            "(82,95)" : "1 d3 gems",
            "(96,100)" : "1 d3 art"
        },
        "ITEMS":{
            "(1,49)" : "NONE",
            "(50,85)" : "1 mundane",
            "(86,100)" : "1 minor"
        }
    },
    3:{
        "COINS":{
            "(1, 11)"     : "NONE",
            "(12, 21)"    : "3 d10 * 100 cp",
            "(22, 41)"    : "4 d12 * 100 sp",
            "(42, 95)"    : "1 d6 * 10 gp",
            "(96, 100)"   : "1 d2 * 1 pp"
        },
        "GOODS":{
            "(1,77)" : "NONE",
            "(78,95)" : "1 d3 gems",
            "(96,100)" : "1 d3 art"
        },
        "ITEMS":{
            "(1,49)" : "NONE",
            "(50,79)" : "1 d3 mundane",
            "(80,100)" : "1 minor"
        }
    },
    4:{
        "COINS":{
            "(1, 11)"     : "NONE",
            "(12, 21)"    : "3 d10 * 100 cp",
            "(22, 41)"    : "4 d12 * 100 sp",
            "(42, 95)"    : "1 d6 * 10 gp",
            "(96, 100)"   : "1 d2 * 1 pp"
        },
        "GOODS":{
            "(1,70)" : "NONE",
            "(71,95)" : "1 d4 gems",
            "(96,100)" : "1 d3 art"
        },
        "ITEMS":{
            "(1,42)" : "NONE",
            "(43,62)" : "1 d4 mundane",
            "(63,100)" : "1 minor"
        }
    },
    5:{
        "COINS":{
            "(1, 10)"   : "NONE",
            "(11, 19)"   : "1 d4 * 1000 cp",
            "(20, 38)"   : "1 d6 * 100 sp",
            "(39, 95)"   : "1 d8 * 10 gp",
            "(96, 100)"   : "1 d2 * 1 pp"
        },
        "GOODS":{
            "(1,60)" : "NONE",
            "(61,95)" : "1 d4 gems",
            "(96,100)" : "1 d4 art"
        },
        "ITEMS":{
            "(1,57)" : "NONE",
            "(58,67)" : "1 d4 mundane",
            "(68,100)" : "1 d3 minor"
        }
    },
    6:{
        "COINS":{
            "(1, 10)"   : "NONE",
            "(11, 18)"   : "1 d6 * 1000 cp",
            "(19, 37)"   : "1 d6 * 100 sp",
            "(38, 95)"   : "1 d10 * 10 gp",
            "(96, 100)"   : "1 d12 * 1 pp"
        },
        "GOODS":{
            "(1,56)" : "NONE",
            "(57,92)" : "1 d4 gems",
            "(93,100)" : "1 d4 art"
        },
        "ITEMS":{
            "(1,54)"  : "NONE",
            "(55,59)" : "1 d4 mundane",
            "(60,99)" : "1 d3 minor",
            "(100,100)"   : "1 medium"
        }
    },
    7:{
        "COINS":{
            "(1, 11)"     : "NONE",
            "(12, 18)"    : "1 d10 * 1000 cp",
            "(19, 35)"    : "1 d12 * 100 sp",
            "(36, 93)"    : "2 d6 * 10 gp",
            "(94, 100)"   : "3 d4 * 1 pp"
        },
        "GOODS":{
            "(1,48)"      : "None",
            "(49,88)"     : "1 d4 gems",
            "(89,100)"    : "1 d4 art"
        },
        "ITEMS":{
            "(1,51)"      : "NONE",
            "(52,97)"     : "1 d3 minor",
            "(98,100)"    : "1 d3 medium"
        }
    },
    8:{
        "COINS":{
            "(1, 10)"   : "NONE",
            "(11, 15)"   : "1 d12 * 1000 cp",
            "(16, 29)"   : "2 d6 * 100 sp",
            "(30, 87)"   : "2 d8 * 10 gp",
            "(88, 100)"   : "3 d6 * 1 pp"
        },
        "GOODS":{
            "(1,45)"      : "None",
            "(46,85)"     : "1 d6 gems",
            "(86,100)"    : "1 d4 art"
        },
        "ITEMS":{
            "(1,51)"      : "NONE",
            "(52,97)"     : "1 d3 minor",
            "(98,100)"    : "1 d3 medium"
        }
    },
    9:{
        "COINS":{
            "(1, 10)"   : "NONE",
            "(11, 15)"   : "2 d6 * 1000 cp",
            "(16, 29)"   : "2 d8 * 100 sp",
            "(30, 85)"   : "5 d4 * 10 gp",
            "(86, 100)"   : "2 d12 * 1 pp"
        },
        "GOODS":{
            "(1,40)" : "NONE",
            "(41,80)" : "1 d8 gems",
            "(81,100)" : "1 d4 art"
        },
        "ITEMS":{
            "(1,43)" : "NONE",
            "(44,91)" : "1 d4 minor",
            "(92,100 )" : "1 medium"
        }
    },
    10:{
        "COINS":{
            "(1, 10)"   : "NONE",
            "(11, 24)"   : "2 d10 * 100 sp",
            "(25, 79)"   : "6 d8 * 10 gp",
            "(80, 100)"   : "5 d6 * 1 pp"
        },
        "GOODS":{
            "(1,35)" : "NONE",
            "(36,79)" : "1 d8 gems",
            "(81,100)" : "1 d4 art"
        },
        "ITEMS":{
            "(1,43)" : "NONE",
            "(44,91)" : "1 d4 minor",
            "(92,100)" : "1 medium"
        }
    },
    11:{
        "COINS":{
            "(1, 8)"  : "NONE",
            "(9, 14)"  : "3 d10 * 100 sp",
            "(15, 75)"   : "4 d8 * 10 gp",
            "(76, 100)"   : "4 d10 * 1 pp"
        },
        "GOODS":{
            "(1,24)" : "NONE",
            "(25,74)" : "1 d10 gems",
            "(75,100)" : "1 d6 art"
        },
        "ITEMS":{
            "(1,31)" : "NONE",
            "(32,84)" : "1 d4 minor",
            "(85,98)" : "1 medium",
            "(99,100)" : "1 major"
        }
    },
    12:{
        "COINS":{
            "(1, 8)"  : "NONE",
            "(9, 14)"  : "3 d12 * 100 sp",
            "(15, 75)"   : "1 d4 * 100 gp",
            "(76, 100)"   : "1 d4 * 10 pp"
        },
        "GOODS":{
            "(1,17)" : "NONE",
            "(18,70)" : "1 d10 gems",
            "(71,100)" : "1 d8 art"
        },
        "ITEMS":{
            "(1,27)" : "NONE",
            "(28,82)" : "1 d6 minor",
            "(83,97)" : "1 medium",
            "(98,100)" : "1 major"
        }
    },
    13:{
        "COINS":{
            "(1, 8)"     : "NONE",
            "(9, 75)"    : "1 d4 * 100 gp",
            "(76, 100)"  : "1 d10 * 10 pp"
        },
        "GOODS":{
            "(1,17)" : "NONE",
            "(18,70)" : "1 d10 gems",
            "(71,100)" : "1 d8 art"
        },
        "ITEMS":{
            "(1,19)" : "NONE",
            "(20,73)" : "1 d6 minor",
            "(74,95)" : "1 medium",
            "(96,100)" : "1 major"
        }
    },
    14:{
        "COINS":{
            "(1, 8)"     : "NONE",
            "(9, 75)"    : "1 d6 * 100 gp",
            "(76, 100)"  : "1 d12 * 10 pp"
        },
        "GOODS":{
            "(1,11)" : "NONE",
            "(12,66)" : "2 d8 gems",
            "(67,100)" : "2 d6 art"
        },
        "ITEMS":{
            "(1,19)" : "NONE",
            "(20,58)" : "1 d6 minor",
            "(59,92)" : "1 medium",
            "(93,100)" : "1 major"
        }
    },
    15:{
        "COINS":{
            "(1, 3)"     : "NONE",
            "(4, 74)"    : "1 d8 * 100 gp",
            "(75, 100)"  : "3 d4 * 10 pp"
        },
        "GOODS":{
            "(1,9)" : "NONE",
            "(10,65)" : "2 d10 gems",
            "(66,100)" : "2 d8 art"
        },
        "ITEMS":{
            "(1,11)" : "NONE",
            "(12,46)" : "1 d6 minor",
            "(47,90)" : "1 medium",
            "(91,100)" : "1 major"
        }
    },
    16:{
        "COINS":{
            "(1, 3)"     : "NONE",
            "(4, 74)"    : "1 d12 * 100 gp",
            "(75, 100)"  : "3 d4 * 10 pp"
        },
        "GOODS":{
            "(1,7)" : "NONE",
            "(8,64)" : "4 d6 gems",
            "(65,100)" : "2 d10 art"
        },
        "ITEMS":{
            "(1,40)" : "NONE",
            "(41,46)" : "1 d10 minor",
            "(47,90)" : "1 d3 medium",
            "(91,100)" : "1 major"
        }
    },
    17:{
        "COINS":{
            "(1, 3)"     : "NONE",
            "(4, 68)"    : "3 d4 * 100 gp",
            "(69, 100)"  : "2 d10 * 10 pp"
        },
        "GOODS":{
            "(1,4)" : "NONE",
            "(5,63)" : "4 d8 gems",
            "(64,100)" : "3 d8 art"
        },
        "ITEMS":{
            "(1,33)" : "NONE",
            "(34,83)" : "1 d3 medium",
            "(84,100)" : "1 major"
        }
    },
    18:{
        "COINS":{
            "(1, 2)"     : "NONE",
            "(3, 65)"    : "3 d6 * 100 gp",
            "(66, 100)"  : "5 d4 * 10 pp"
        },
        "GOODS":{
            "(1,4)" : "NONE",
            "(5,54)" : "3 d12 gems",
            "(55,100)" : "3 d10 art"
        },
        "ITEMS":{
            "(1,24)" : "NONE",
            "(25,80)" : "1 d4 medium",
            "(81,100)" : "1 major"
        }
    },
    19:{
        "COINS":{
            "(1, 2)"     : "NONE",
            "(3, 65)"    : "3 d8 * 100 gp",
            "(66, 100)"  : "3 d10 * 10 pp"
        },
        "GOODS":{
            "(1,3)" : "NONE",
            "(4,50)" : "6 d6 gems",
            "(51,100)" : "6 d6 art"
        },
        "ITEMS":{
            "(1,4)" : "NONE",
            "(5,70)" : "1 d4 medium",
            "(71,100)" : "1 major"
        }
    },
    20:{
        "COINS":{
            "(1, 2)"     : "NONE",
            "(3, 65)"    : "4 d8 * 100 gp",
            "(66, 100)"  : "4 d10 * 10 pp"
        },
        "GOODS":{
            "(1,2)" : "NONE",
            "(3,38)" : "4 d10 gems",
            "(39,100)" : "7 d6 art"
        },
        "ITEMS":{
            "(1,25)" : "NONE",
            "(26,65)" : "1 d4 medium",
            "(66,100)" : "1 d3 major"
        }
    },
}


ALCHEMICAL_ITEM = {
    "(1,12)"         : {"name":"Alchemist's fire", "val":"1 d4 2 gp"},
    "(13,24)"        : {"name": "Acid", "val": "2 d4 1 gp"},
    "(25,36)"        : {"name": "Smokestiks", "val" : "1 d4 2 gp"},
    "(37,48)"        : {"name": "Holy water", "val" : "1 d4 25 sp"}, 
    "(49,62)"        : {"name": "Antitoxin", "val" : "1 d4 5 gp"}, 
    "(63,74)"        : {"name": "Everburning Torch", "val" : ""}, 
    "(75,88)"        : {"name": "Tanglefoot bags", "val" : "1 d4 5 gp"}, 
    "(89,100)"       : {"name": "Thunderstones", "val" : "1 d4 3 gp"}
}

MASTER_WORK_SHIELDS = {
    "(1,17)"         : {"name": "Buckler", "val": "205 sp"},
    "(18,40)"        : {"name": "Light wooden shield", "val" : "153 sp"},
    "(41,60)"        : {"name": "Light steel shield", "val" : "159 sp"},
    "(61,83)"        : {"name": "Heavy wooden shield", "val" : "157 sp"},
    "(84,100)"       : {"name": "Heavy steel shield", "val" : "170 sp"}
}

ARMOR = {
    "(1,12)"        : {"name":"Chain shirt", "val" : "10 gp"},
    "(13,18)"       : {"name": "mwk studded leather", "val" : "175 sp"}, 
    "(19,26)"       : {"name": "Breastplate", "val" : "20 gp"}, 
    "(27,34)"       : {"name": "banded mail", "val" : "25 gp"}, 
    "(35,54)"       : {"name": "half plate", "val" : "60 gp"}, 
    "(55,80)"       : {"name": "full plate", "val" : "150 gp"}, 
    "(81,85)"       : {"name": "darkwood buckler", "val" : "205 sp"}, 
    "(86,90)"       : {"name": "darkwood shield", "val" : "257 sp"}, 
    "(91,100)"      : {"name": "Masterwork Shield", "val" : MASTER_WORK_SHIELDS}, 
}

WEAPONS = {
    "(1,50)"        : {"name": "Masterwork common melee weapons", "val" : ""}, 
    "(51,70)"       : {"name": "Masterwork uncommon melee weapons", "val" : ""}, 
    "(71,100)"      : {"name": "Masterwork common ranged weapons", "val" : ""}, 
}

TOOLS_AND_GEAR = {
    "(1,3)"         : {"name":"Backpack, empty", "val": "2 sp"},
    "(4,6)"         : {"name":"Crowbar", "val": "2 sp"},
    "(7,11)"        : {"name":"Lantern, Bullseye", "val": "12 sp"},
    "(12,16)"       : {"name":"Lock, Simple", "val": "2 gp"},
    "(17,21)"       : {"name":"Lock, Average", "val": "4 gp"},
    "(22,28)"       : {"name":"Lock, Good", "val": "8 gp"},
    "(29,35)"       : {"name":"Lock, Superior", "val": "15 gp"},
    "(36,40)"       : {"name":"Manacles, masterwork", "val": "5 gp"},
    "(41,43)"       : {"name":"Mirror, small steel", "val": " 1 gp"},
    "(44,46)"       : {"name":"Rope, silk (50 ft)", "val": "1 gp"},
    "(47,53)"       : {"name":"Spyglass", "val": "100 gp"},
    "(54,58)"       : {"name":"Artisan's tools, masterwork", "val": "55 sp"},
    "(59,63)"       : {"name":"Climber's kit", "val": "8 gp"},
    "(64,68)"       : {"name":"Disguise kit", "val": "5 sp"},
    "(69,73)"       : {"name":"Healer's kit", "val": "5 gp"},
    "(74,77)"       : {"name":"Holy symbol, silver", "val": "25 sp"},
    "(78,81)"       : {"name":"Hourglass", "val": "25 sp"},
    "(82,88)"       : {"name":"Magnifying glass", "val": "10 gp"},
    "(89,95)"       : {"name":"Muical instrument, masterwork", "val": "10 gp"},
    "(96,100)"      : {"name":"Theives' tools, masterwork", "val": "5 gp"}
}

MUNDANE_ITEMS = {
    "(1,17)"        : ALCHEMICAL_ITEM,
    "(18,50)"       : ARMOR,
    "(51,83)"       : WEAPONS,
    "(84,100)"      : TOOLS_AND_GEAR
}


ART_OBJECTS = {
    "(1,10)"        : {
        "VALUE": "1 d1 * 1 gp", 
        "EXAMPLES": ["Silver ewer", "Carved Bone or ivory statuette", "Finely wrought small gold bracelet"]
    },

}


GEMS = {
    "(1,25)" : {
        "VALUE" : "4 d4 * 1 sp", 
        "EXAMPLES" : ["Banded eye or moss agate", "azurite", "blue quartz", "hematite", "lapis lazuli", "malachite", "obsidian", "rhodochrosite", "tiger eye", "turquoise", "freshwater (irregular) pearl"]
    },
    "(26,50)" : {
        "VALUE" : "2 d4 * 1 gp", 
        "EXAMPLES" :  ["Bloodstone" , "carnelian", "chalcedony", "chrysoprase", "citrine", "iolite jasper", "moonstone", "onyx", "peridot", "rock crystal (clear quartz)", "sard", "sardonyx", "rose or smoky or star rose ; quartz", "zircon"]
    },
    "(51,70)" : {
        "VALUE": "4 d4 * 1 gp", 
        "EXAMPLES" : ["Amber", "amethyst", "chrysoberyl", "coral", "red or brown-green ; garnet", "jade", "jet", "white or golden or pink or silver ; pearl", "red or red-brown or deep green ; spinel", "tourmaline"]
    },
    "(71,90)" : {
        "VALUE": "2 d4 * 10 gp  ",
        "EXAMPLES" :  ["Alexandrite", "aquamarine", "violet garnet", "black pearl", "deep blue spinel", "golden yellow topaz"]
    },
    "(91,99)" : {
        "VALUE": "4 d4 * 10 gp",
        "EXAMPLES" :  ["Emerald", "white or black or fire ; opal", "blue sapphire", "fiery yellow or rich purple ; corundum", "blue or black ; star sapphire", "star ruby"]
    },
    "(100,100)" : {
        "VALUE": "2 d4 * 100 gp",
        "EXAMPLES" :  ["Clearest bright green emerald", "blue-white or canary or pink or brown or blue ; diamond", "jacinth"]
    }
}




def is_in(a_string : str, roll : int) -> bool:
    val = eval(a_string)
    assert isinstance(val, tuple), "val is not tuple something went wrong"
    if not val:
        return False
    res = val[0] <= roll and roll <= val[1]
    return res


def roll_table(table):
    roll = dice.roll_dice("d100")
    # print(roll)
    for cand , val in table.items():
        if is_in(cand, roll):
            return  val
    else:
        print("Something went wrong", table)
        exit()


def handle_coins(coins : str):
    print("Handlings Coins")
    if coins == "NONE":
        return coins
    data = coins.split()
    assert len(data) == 5, f"{data=} is not 5 elements"
    print(data)

    num_rolls = int(data[0])
    dice_type = data[1]
    times = int(data[3])
    coin_type = data[4]

    num_coins = dice.roll_dice(dice_type, num_rolls, times)
    return f"{num_coins} {coin_type}"


def handle_goods(goods : str):
    print(f"handling {goods=}")
    if goods == "NONE":
        return goods
    data = goods.split()
    num_dice = int(data[0])
    dice_type = data[1]
    goods_type = data[2]

    num_goods = dice.roll_dice(dice_type, num_dice)


    return goods
 

def handle_items(items : str):
    print(f"handling {items=}")
    if items == "NONE":
        return items
    
    return items




def roll_random_treasure(treasure_level):
    res = {}
    table = TREASHURE_START[treasure_level]
    for key, value in table.items():
        # print("rolling for " + key)
        res[key] = roll_table(value)
    
    coins = handle_coins(res["COINS"])
    print(f"{coins=}")
    goods = handle_goods(res["GOODS"])
    print(f"{goods=}")
    items = handle_items(res["ITEMS"])
    return f"***************************\n* {coins=}\n* {goods=}\n* {items=}\n***************************"
