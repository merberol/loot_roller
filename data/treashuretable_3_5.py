
from utils.dice import roll_dice
from utils.utils import roll_table, handle_coins
from random import choice
from utils.map_list import MapList
from data.mundane_items import roll_mundane_item, roll_minor_item, roll_medium_item, roll_major_item


TREASHURE_START = {
    1:{
        "COINS":{"(1,14)": "NONE", "(15,39)" : "1 d6 * 100 cp", "(40,95)" : "1 d8 * 10 sp", "(96,100)"   : "2 d8 * 1 gp"},
        "GOODS":{"(1,90)": "NONE", "(91,95)" : "1 gem", "(96,100)" : "1 art"},
        "ITEMS":{"(1,71)": "NONE", "(72,95)" : "1 mundane", "(96,100)" : "1 minor"}
    },
    2:{
        "COINS":{ "(1,13)": "NONE", "(14,23)": "1 d10 * 100 cp", "(24,43)": "2 d10 * 10 sp", "(44, 95)": "2 d10 * 1 gp", "(96, 100)": "4 d10 * 1 gp"},
        "GOODS":{ "(1,81)": "NONE", "(82,95)" : "1 d3 gems", "(96,100)" : "1 d3 art"},
        "ITEMS":{ "(1,49)": "NONE", "(50,85)" : "1 mundane", "(86,100)" : "1 minor"}
    },
    3:{
        "COINS":{ "(1,11)": "NONE", "(12, 21)": "3 d10 * 100 cp", "(22, 41)": "4 d12 * 100 sp", "(42, 95)": "1 d6 * 10 gp", "(96, 100)": "1 d2 * 1 pp"},
        "GOODS":{ "(1,77)": "NONE", "(78,95)" : "1 d3 gems", "(96,100)" : "1 d3 art"},
        "ITEMS":{ "(1,49)": "NONE", "(50,79)" : "1 d3 mundane", "(80,100)" : "1 minor"}
    },
    4:{
        "COINS":{ "(1,11)": "NONE", "(12, 21)"    : "3 d10 * 100 cp", "(22, 41)"    : "4 d12 * 100 sp", "(42, 95)"    : "1 d6 * 10 gp", "(96, 100)"   : "1 d2 * 1 pp"},
        "GOODS":{ "(1,70)": "NONE", "(71,95)" : "1 d4 gems", "(96,100)" : "1 d3 art"},
        "ITEMS":{ "(1,42)": "NONE", "(43,62)" : "1 d4 mundane", "(63,100)" : "1 minor"}
    },
    5:{
        "COINS":{"(1,10)": "NONE","(11, 19)"   : "1 d4 * 1000 cp","(20, 38)"   : "1 d6 * 100 sp","(39, 95)"   : "1 d8 * 10 gp","(96, 100)"   : "1 d2 * 1 pp"},
        "GOODS":{"(1,60)": "NONE","(61,95)": "1 d4 gems","(96,100)" : "1 d4 art"},
        "ITEMS":{"(1,57)": "NONE","(58,67)": "1 d4 mundane","(68,100)" : "1 d3 minor"}
    },
    6:{
        "COINS":{"(1,10)": "NONE","(11, 18)": "1 d6 * 1000 cp","(19, 37)"   : "1 d6 * 100 sp","(38, 95)"   : "1 d10 * 10 gp","(96, 100)"   : "1 d12 * 1 pp"},
        "GOODS":{"(1,56)": "NONE","(57,92)": "1 d4 gems","(93,100)" : "1 d4 art"},
        "ITEMS":{"(1,54)": "NONE","(55,59)": "1 d4 mundane","(60,99)" : "1 d3 minor","(100,100)"   : "1 medium"}
    },
    7:{
        "COINS":{"(1,11)": "NONE","(12, 18)"    : "1 d10 * 1000 cp","(19, 35)"    : "1 d12 * 100 sp","(36, 93)"    : "2 d6 * 10 gp","(94, 100)"   : "3 d4 * 1 pp"},
        "GOODS":{"(1,48)": "NONE","(49,88)"     : "1 d4 gems","(89,100)"    : "1 d4 art"},
        "ITEMS":{"(1,51)": "NONE","(52,97)"     : "1 d3 minor","(98,100)"    : "1 d3 medium"}
    },
    8:{
        "COINS":{"(1, 10)": "NONE","(11, 15)"   : "1 d12 * 1000 cp","(16, 29)"   : "2 d6 * 100 sp","(30, 87)"   : "2 d8 * 10 gp","(88, 100)"   : "3 d6 * 1 pp"},
        "GOODS":{"(1,45)": "NONE","(46,85)"     : "1 d6 gems","(86,100)"    : "1 d4 art"},
        "ITEMS":{"(1,51)": "NONE","(52,97)"     : "1 d3 minor","(98,100)"    : "1 d3 medium"}
    },
    9:{
        "COINS":{"(1,10)": "NONE","(11, 15)"   : "2 d6 * 1000 cp","(16, 29)"   : "2 d8 * 100 sp","(30, 85)"   : "5 d4 * 10 gp","(86, 100)"   : "2 d12 * 1 pp"},
        "GOODS":{"(1,40)": "NONE","(41,80)" : "1 d8 gems","(81,100)" : "1 d4 art"},
        "ITEMS":{"(1,43)": "NONE","(44,91)" : "1 d4 minor","(92,100 )" : "1 medium"}
    },
    10:{
        "COINS":{"(1,10)": "NONE","(11, 24)"   : "2 d10 * 100 sp","(25, 79)"   : "6 d8 * 10 gp","(80, 100)"   : "5 d6 * 1 pp"},
        "GOODS":{"(1,35)": "NONE","(36,79)" : "1 d8 gems","(81,100)" : "1 d4 art"},
        "ITEMS":{"(1,43)": "NONE","(44,91)" : "1 d4 minor","(92,100)" : "1 medium"}
    },
    11:{
        "COINS":{"(1,8)": "NONE","(9, 14)"  : "3 d10 * 100 sp","(15, 75)"   : "4 d8 * 10 gp","(76, 100)"   : "4 d10 * 1 pp"},
        "GOODS":{"(1,24)": "NONE","(25,74)" : "1 d10 gems","(75,100)" : "1 d6 art"},
        "ITEMS":{"(1,31)": "NONE","(32,84)" : "1 d4 minor","(85,98)" : "1 medium","(99,100)" : "1 major"}
    },
    12:{
        "COINS":{"(1,8)": "NONE","(9, 14)"  : "3 d12 * 100 sp","(15, 75)"   : "1 d4 * 100 gp","(76, 100)"   : "1 d4 * 10 pp"},
        "GOODS":{"(1,17)": "NONE","(18,70)" : "1 d10 gems","(71,100)" : "1 d8 art"},
        "ITEMS":{"(1,27)": "NONE","(28,82)" : "1 d6 minor","(83,97)" : "1 medium","(98,100)" : "1 major"}
    },
    13:{
        "COINS":{"(1, 8)": "NONE","(9, 75)"    : "1 d4 * 100 gp","(76, 100)"  : "1 d10 * 10 pp"},
        "GOODS":{"(1,17)": "NONE","(18,70)" : "1 d10 gems","(71,100)" : "1 d8 art"},
        "ITEMS":{"(1,19)": "NONE","(20,73)" : "1 d6 minor","(74,95)" : "1 medium","(96,100)" : "1 major"}
    },
    14:{
        "COINS":{"(1,8)": "NONE","(9,75)"    : "1 d6 * 100 gp","(76,100)"  : "1 d12 * 10 pp"},
        "GOODS":{"(1,11)": "NONE","(12,66)" : "2 d8 gems","(67,100)" : "2 d6 art"},
        "ITEMS":{"(1,19)": "NONE","(20,58)" : "1 d6 minor","(59,92)" : "1 medium","(93,100)" : "1 major"}
    },
    15:{
        "COINS":{"(1,3)"     : "NONE","(4,74)"    : "1 d8 * 100 gp","(75,100)"  : "3 d4 * 10 pp"},
        "GOODS":{"(1,9)" : "NONE","(10,65)" : "2 d10 gems","(66,100)" : "2 d8 art"},
        "ITEMS":{"(1,11)" : "NONE","(12,46)" : "1 d6 minor","(47,90)" : "1 medium","(91,100)" : "1 major"}
    },
    16:{
        "COINS":{"(1, 3)"     : "NONE","(4, 74)"    : "1 d12 * 100 gp","(75, 100)"  : "3 d4 * 10 pp"},
        "GOODS":{"(1,7)" : "NONE","(8,64)" : "4 d6 gems","(65,100)" : "2 d10 art"},
        "ITEMS":{"(1,40)" : "NONE","(41,46)" : "1 d10 minor","(47,90)" : "1 d3 medium","(91,100)" : "1 major"}
    },
    17:{
        "COINS":{"(1, 3)"     : "NONE","(4, 68)"    : "3 d4 * 100 gp","(69, 100)"  : "2 d10 * 10 pp"},
        "GOODS":{"(1,4)" : "NONE","(5,63)" : "4 d8 gems","(64,100)" : "3 d8 art"},
        "ITEMS":{"(1,33)" : "NONE","(34,83)" : "1 d3 medium","(84,100)" : "1 major"}
    },
    18:{
        "COINS":{"(1, 2)"     : "NONE","(3, 65)"    : "3 d6 * 100 gp","(66, 100)"  : "5 d4 * 10 pp"},
        "GOODS":{"(1,4)" : "NONE","(5,54)" : "3 d12 gems","(55,100)" : "3 d10 art"},
        "ITEMS":{"(1,24)" : "NONE","(25,80)" : "1 d4 medium","(81,100)" : "1 major"}
    },
    19:{
        "COINS":{"(1, 2)"     : "NONE","(3, 65)"    : "3 d8 * 100 gp","(66, 100)"  : "3 d10 * 10 pp"},
        "GOODS":{"(1,3)" : "NONE","(4,50)" : "6 d6 gems","(51,100)" : "6 d6 art"},
        "ITEMS":{"(1,4)" : "NONE","(5,70)" : "1 d4 medium","(71,100)" : "1 major"}
    },
    20:{
        "COINS":{"(1, 2)"     : "NONE","(3, 65)"    : "4 d8 * 100 gp","(66, 100)"  : "4 d10 * 10 pp"},
        "GOODS":{"(1,2)" : "NONE","(3,38)" : "4 d10 gems","(39,100)" : "7 d6 art"},
        "ITEMS":{"(1,25)" : "NONE","(26,65)" : "1 d4 medium","(66,100)" : "1 d3 major"}
    },
}





ART_OBJECTS = {
    "(1,10)" : {
        "VALUE": "1 d10 * 1 gp", 
        "EXAMPLES": ["Silver ewer", "Carved Bone or ivory statuette", "Finely wrought small gold bracelet"]
    },
    "(11,25)" : {
        "VALUE": "3 d6  * 1 gp",
        "EXAMPLES" : ["Cloth of gold vestments", "black velvet mask with numerous citrines", "silver chalice with lapis lazuli gems"]
    },
    "(26,40)" : {
        "VALUE": "1 d6  * 10 gp",
        "EXAMPLES" : ["Large well-done wool tapestry" "brass mug with jade inlays"]
    },
    "(41,50)" : {
        "VALUE": "1 d10 * 10 gp",
        "EXAMPLES" : ["Silver comb with moonstones", "silver-plated steel longsword with jet jewel in hilt"]
    },
    "(51,60)"   : {
        "VALUE": "2 d6  * 10 gp ",
        "EXAMPLES" : ["Carved harp of exotic wood with ivory inlay and zircon gems", "solid gold idol (10 lb.)"]
    },
    "(61,70)"   : {
        "VALUE": "3 d6  * 10 gp ",
        "EXAMPLES" : ["Gold dragon comb with red garnet eye", "gold and topaz bottle stopper cork", "ceremonial electrum dagger with a star ruby in the pommel"]
    },
    "(71,80)"   : {
        "VALUE": "4 d6  * 10 gp ",
        "EXAMPLES" : ["Eyepatch with mock eye of sapphire and moonstone", "fire opal pendant on a fine gold chain", "old masterpiece painting"]
    },
    "(81,85)"   : {
        "VALUE": "5 d6  * 10 gp ",
        "EXAMPLES" : ["Embroidered silk and velvet mantle with numerous moonstones", "sapphire pendant on gold chain"]
    },
    "(86,90)"   : {
        "VALUE": "1 d4  * 100 gp",
        "EXAMPLES" : ["Embroidered and bejeweled glove", "jeweled anklet", "gold music box"]
    },
    "(91,95)"   : {
        "VALUE": "1 d6  * 100 gp",
        "EXAMPLES" : ["Golden circlet with four aquamarines", "a string of small pink pearls (necklace)"]
    },
    "(96,99)"   : {
        "VALUE": "2 d4  * 100 gp",
        "EXAMPLES" : ["Jeweled gold crown", "jeweled electrum ring"]
    },
    "(100,100)" : {
        "VALUE": "2 d6  * 100 gp",
        "EXAMPLES" : ["Gold and ruby ring", "gold cup set with emeralds"]
    }
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
        "VALUE": "2 d4 * 10 gp",
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


def handle_goods(goods : str):
    print(f"handling {goods=}")
    if goods == "NONE":
        return goods
    data = goods.split()
    if len(data) == 3:
        num_dice = int(data[0])
        dice_type = data[1]
        num_goods = roll_dice(dice_type, num_dice, 1)
        goods_type = data[2]
    elif len(data) == 2:
        num_goods = int(data[0])
        goods_type = data[1]

    table = None
    match goods_type:
        case "art":
            # print("doing art")
            table = ART_OBJECTS
                
        case "gems":
            # print("doing gems")
            table = GEMS

    goods : MapList = MapList()
    for _ in range(num_goods):
        goods_item_data = roll_table(table)
        value = handle_coins(goods_item_data.get("VALUE"))
        item = choice(goods_item_data.get('EXAMPLES'))
        print(value, item)
        goods.add(item, value)

    return goods


def handle_items(items : str):
    print(f"handling {items=}")
    if items == "NONE":
        return items
    item_as_list = items.split()

    if len(item_as_list) == 3:
        num_dice, dice_type, item_type  = item_as_list
        num_items = roll_dice(dice_type, int(num_dice), 1)
    elif len(item_as_list) == 2:
        num_items, item_type = item_as_list
    else:
        print(f"Something went wrong {item_as_list=}")
        exit()

    match item_type:
        case "mundane":
            print("rolling on mundane table")
            items = roll_mundane_item(int(num_items))

        case "minor":
            print("rolling on minor table")
            items = roll_minor_item(int(num_items))

        case "medium":
            print("rolling on medium table")
            items = roll_medium_item(int(num_items))

        case "major":
            print("rolling on major table")
            items = roll_major_item(int(num_items))

    return items


def roll_random_treasure(treasure_level):
    res = {}
    table = TREASHURE_START[treasure_level]
    for key, value in table.items():
        # print("rolling for " + key)
        res[key] = roll_table(value)

    coins = handle_coins(res["COINS"])
    # print(f"{coins=}")
    goods = handle_goods(res["GOODS"])
    # print(f"{goods=}")
    items = handle_items(res["ITEMS"])
    return {"COINS":coins, "GOODS":goods, "ITEMS":items}
