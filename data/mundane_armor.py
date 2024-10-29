from utils.utils import roll_table
from utils.map_list import MapList


MASTER_WORK_SHIELDS = {
    "(1,17)"         : {"NAME": "Buckler", "VALUE": "205 sp"},
    "(18,40)"        : {"NAME": "Light wooden shield", "VALUE" : "153 sp"},
    "(41,60)"        : {"NAME": "Light steel shield", "VALUE" : "159 sp"},
    "(61,83)"        : {"NAME": "Heavy wooden shield", "VALUE" : "157 sp"},
    "(84,100)"       : {"NAME": "Heavy steel shield", "VALUE" : "170 sp"}
}

MUNDANE_ARMOR = {
    "(1,12)"        : {"NAME": "Chain shirt", "VALUE" : "10 gp"},
    "(13,18)"       : {"NAME": "mwk studded leather", "VALUE" : "175 sp"}, 
    "(19,26)"       : {"NAME": "Breastplate", "VALUE" : "20 gp"}, 
    "(27,34)"       : {"NAME": "banded mail", "VALUE" : "25 gp"}, 
    "(35,54)"       : {"NAME": "half plate", "VALUE" : "60 gp"}, 
    "(55,80)"       : {"NAME": "full plate", "VALUE" : "150 gp"}, 
    "(81,85)"       : {"NAME": "darkwood buckler", "VALUE" : "205 sp"}, 
    "(86,90)"       : {"NAME": "darkwood shield", "VALUE" : "257 sp"}, 
    "(91,100)"      : {"NAME": "Masterwork Shield", "VALUE" : MASTER_WORK_SHIELDS}, 
}





def roll_mundane_armor(result : MapList):
    item_data = roll_table(MUNDANE_ARMOR)
    if type(item_data["VALUE"]) == dict:
        print("Rolling for masterwork shield")
        item_data = roll_table(item_data["VALUE"])
    result.add(
        item_data.get("NAME"),
        item_data.get("VALUE")
    )