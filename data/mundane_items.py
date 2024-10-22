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
    "(36,40)"       : {"name":"Manacles, masterwork", "val": "5 gp"},,
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

TABLE = {
    "(1,17)"        : ALCHEMICAL_ITEM,
    "(18,50)"       : ARMOR,
    "(51,83)"       : WEAPONS,
    "(84,100)"      : TOOLS_AND_GEAR
}
