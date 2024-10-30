from utils.map_list import MapList
from utils.utils import roll_table


POTIONS_MINOR = {
    "(1,10)"	: {"NAME" : "Cure light wounds (potion)", "VALUE" : "5 gp"},
    "(11,13)"	: {"NAME" : "Endure elements (potion)", "VALUE" : "5 gp"},
    "(14,15)"	: {"NAME" : "Hide from animals (potion)", "VALUE" : "5 gp"},
    "(16,17)"	: {"NAME" : "Hide from undead (potion)", "VALUE" : "5 gp"},
    "(18,19)"	: {"NAME" : "Jump (potion)", "VALUE" : "5 gp"},
    "(20,22)"	: {"NAME" : "Mage armor (potion)", "VALUE" : "5 gp"},
    "(23,25)"	: {"NAME" : "Magic fang (potion)", "VALUE" : "5 gp"},
    "(26,26)"	: {"NAME" : "Magic stone (oil)", "VALUE" : "5 gp"},
    "(27,29)"	: {"NAME" : "Magic weapon (oil)", "VALUE" : "5 gp"},
    "(30,30)"	: {"NAME" : "Pass without trace (potion)", "VALUE" : "5 gp"},
    "(31,32)"	: {"NAME" : "Protection from (alignment) (potion)", "VALUE" : "5 gp"},
    "(33,34)"	: {"NAME" : "Remove fear (potion)", "VALUE" : "5 gp"},
    "(35,35)"	: {"NAME" : "Sanctuary (potion)", "VALUE" : "5 gp"},
    "(36,38)"	: {"NAME" : "Shield of faith +2 (potion)", "VALUE" : "5 gp"},
    "(39,39)"	: {"NAME" : "Shillelagh (oil)", "VALUE" : "5 gp"},
    "(40,41)"	: {"NAME" : "Bless weapon (oil)", "VALUE" : "10 gp"},
    "(42,44)"	: {"NAME" : "Enlarge person (potion)", "VALUE" : "25 gp"},
    "(45,45)"	: {"NAME" : "Reduce person (potion)", "VALUE" : "25 gp"},
    "(46,47)"	: {"NAME" : "Aid (potion)", "VALUE" : "30 gp"},
    "(48,50)"	: {"NAME" : "Barkskin +2 (potion)", "VALUE" : "30 gp"},
    "(51,53)"	: {"NAME" : "Bear’s endurance (potion)", "VALUE" : "30 gp"},
    "(54,56)"	: {"NAME" : "Blur (potion)", "VALUE" : "30 gp"},
    "(57,59)"	: {"NAME" : "Bull’s strength (potion)", "VALUE" : "30 gp"},
    "(60,62)"	: {"NAME" : "Cat’s grace (potion)", "VALUE" : "30 gp"},
    "(63,67)"	: {"NAME" : "Cure moderate wounds (potion)", "VALUE" : "30 gp"},
    "(68,68)"	: {"NAME" : "Darkness (oil)", "VALUE" : "30 gp"},
    "(69,71)"	: {"NAME" : "Darkvision (potion)", "VALUE" : "30 gp"},
    "(72,74)"	: {"NAME" : "Delay poison (potion)", "VALUE" : "30 gp"},
    "(75,76)"	: {"NAME" : "Eagle’s splendor (potion)", "VALUE" : "30 gp"},
    "(77,78)"	: {"NAME" : "Fox’s cunning (potion)", "VALUE" : "30 gp"},
    "(79,81)"	: {"NAME" : "Invisibility (potion or oil)", "VALUE" : "30 gp"},
    "(82,84)"	: {"NAME" : "Lesser restoration (potion)", "VALUE" : "30 gp"},
    "(85,86)"	: {"NAME" : "Levitate (potion or oil)", "VALUE" : "30 gp"},
    "(87,87)"	: {"NAME" : "Misdirection (potion)", "VALUE" : "30 gp"},
    "(88,89)"	: {"NAME" : "Owl’s wisdom (potion)", "VALUE" : "30 gp"},
    "(90,91)"	: {"NAME" : "Protection from arrows 10/magic (potion)", "VALUE" : "30 gp"},
    "(92,93)"	: {"NAME" : "Remove paralysis (potion)", "VALUE" : "30 gp"},
    "(94,96)"	: {"NAME" : "Resist energy (type) 10 (potion)", "VALUE" : "30 gp"},
    "(97,97)"	: {"NAME" : "Shield of faith +3 (potion)", "VALUE" : "30 gp"},
    "(98,99)"	: {"NAME" : "Spider climb (potion)", "VALUE" : "30 gp"},
    "(100,100)"	: {"NAME" : "Undetectable alignment (potion)", "VALUE" : "30 gp"}
}



POTIONS_MEDIUM = {
    "(1,2)" : {"NAME" : "Bless weapon (oil)", "VALUE" : "10 gp"},
    "(3,4)" : {"NAME" : "Enlarge person (potion)", "VALUE" : "25 gp"},
    "(5,5)" : {"NAME" : "Reduce person (potion)", "VALUE" : "25 gp"},
    "(6,6)" : {"NAME" : "Aid (potion)", "VALUE" : "30 gp"},
    "(7,7)" : {"NAME" : "Barkskin +2 (potion)", "VALUE" : "30 gp"},
    "(8,10)" : {"NAME" : "Bear’s endurance (potion)", "VALUE" : "30 gp"},
    "(11,13)" : {"NAME" : "Blur (potion)", "VALUE" : "30 gp"},
    "(14,16)" : {"NAME" : "Bull’s strength (potion)", "VALUE" : "30 gp"},
    "(17,19)" : {"NAME" : "Cat’s grace (potion)", "VALUE" : "30 gp"},
    "(20,27)" : {"NAME" : "Cure moderate wounds (potion)", "VALUE" : "30 gp"},
    "(28,28)" : {"NAME" : "Darkness (oil)", "VALUE" : "30 gp"},
    "(29,30)" : {"NAME" : "Darkvision (potion)", "VALUE" : "30 gp"},
    "(31,31)" : {"NAME" : "Delay poison (potion)", "VALUE" : "30 gp"},
    "(32,33)" : {"NAME" : "Eagle’s splendor (potion)", "VALUE" : "30 gp"},
    "(34,35)" : {"NAME" : "Fox’s cunning (potion)", "VALUE" : "30 gp"},
    "(36,37)" : {"NAME" : "Invisibility (potion or oil)", "VALUE" : "30 gp"},
    "(38,38)" : {"NAME" : "Lesser restoration (potion)", "VALUE" : "30 gp"},
    "(39,39)" : {"NAME" : "Levitate (potion or oil)", "VALUE" : "30 gp"},
    "(40,40)" : {"NAME" : "Misdirection (potion)", "VALUE" : "30 gp"},
    "(41,42)" : {"NAME" : "Owl’s wisdom (potion)", "VALUE" : "30 gp"},
    "(43,43)" : {"NAME" : "Protection from arrows 10/magic (potion)", "VALUE" : "30 gp"},
    "(44,44)" : {"NAME" : "Remove paralysis (potion)", "VALUE" : "30 gp"},
    "(45,46)" : {"NAME" : "Resist energy (type) 10 (potion)", "VALUE" : "30 gp"},
    "(47,48)" : {"NAME" : "Shield of faith +3 (potion)", "VALUE" : "30 gp"},
    "(49,49)" : {"NAME" : "Spider climb (potion)", "VALUE" : "30 gp"},
    "(50,50)" : {"NAME" : "Undetectable alignment (potion)", "VALUE" : "30 gp"},
    "(51,51)" : {"NAME" : "Barkskin +3 (potion)", "VALUE" : "60 gp"},
    "(52,52)" : {"NAME" : "Shield of faith +4 (potion)", "VALUE" : "60 gp"},
    "(53,55)" : {"NAME" : "Resist energy (type) 20 (potion)", "VALUE" : "70 gp"},
    "(56,60)" : {"NAME" : "Cure serious wounds (potion)", "VALUE" : "75 gp"},
    "(61,61)" : {"NAME" : "Daylight (oil)", "VALUE" : "75 gp"},
    "(62,64)" : {"NAME" : "Displacement (potion)", "VALUE" : "75 gp"},
    "(65,65)" : {"NAME" : "Flame arrow (oil)", "VALUE" : "75 gp"},
    "(66,68)" : {"NAME" : "Fly (potion)", "VALUE" : "75 gp"},
    "(69,69)" : {"NAME" : "Gaseous form (potion)", "VALUE" : "75 gp"},
    "(70,71)" : {"NAME" : "Greater magic fang +1 (potion)", "VALUE" : "75 gp"},
    "(72,73)" : {"NAME" : "Greater magic weapon +1 (oil)", "VALUE" : "75 gp"},
    "(74,75)" : {"NAME" : "Haste (potion)", "VALUE" : "75 gp"},
    "(76,78)" : {"NAME" : "Heroism (potion)", "VALUE" : "75 gp"},
    "(79,80)" : {"NAME" : "Keen edge (oil)", "VALUE" : "75 gp"},
    "(81,81)" : {"NAME" : "Magic circle against (alignment) (potion)", "VALUE" : "75 gp"},
    "(82,83)" : {"NAME" : "Magic vestment +1 (oil)", "VALUE" : "75 gp"},
    "(84,86)" : {"NAME" : "Neutralize poison (potion)", "VALUE" : "75 gp"},
    "(87,88)" : {"NAME" : "Nondetection (potion)", "VALUE" : "75 gp"},
    "(89,91)" : {"NAME" : "Protection from energy (type) (potion)", "VALUE" : "75 gp"},
    "(92,93)" : {"NAME" : "Rage (potion)", "VALUE" : "75 gp"},
    "(94,94)" : {"NAME" : "Remove blindness/deafness (potion)", "VALUE" : "75 gp"},
    "(95,95)" : {"NAME" : "Remove curse (potion)", "VALUE" : "75 gp"},
    "(96,96)" : {"NAME" : "Remove disease (potion)", "VALUE" : "75 gp"},
    "(97,97)" : {"NAME" : "Tongues (potion)", "VALUE" : "75 gp"},
    "(98,99)" : {"NAME" : "Water breathing (potion)", "VALUE" : "75 gp"},
    "(100,100)" : {"NAME" : "Water walk (potion)", "VALUE" : "75 gp"}
}



POTIONS_MAJOR = {
    "(1,2)" : {"NAME" : "Blur (potion)", "VALUE" : "30 gp"},
    "(3,7)" : {"NAME" : "Cure moderate wounds (potion)", "VALUE" : "30 gp"},
    "(8,9)" : {"NAME" : "Darkvision (potion)", "VALUE" : "30 gp"},
    "(10,11)" : {"NAME" : "Invisibility (potion or oil)", "VALUE" : "30 gp"},
    "(12,12)" : {"NAME" : "Lesser restoration (potion)", "VALUE" : "30 gp"},
    "(13,13)" : {"NAME" : "Remove paralysis (potion)", "VALUE" : "30 gp"},
    "(14,14)" : {"NAME" : "Shield of faith +3 (potion)", "VALUE" : "30 gp"},
    "(15,15)" : {"NAME" : "Undetectable alignment (potion)", "VALUE" : "30 gp"},
    "(16,16)" : {"NAME" : "Barkskin +3 (potion)", "VALUE" : "60 gp"},
    "(17,18)" : {"NAME" : "Shield of faith +4 (potion)", "VALUE" : "60 gp"},
    "(19,20)" : {"NAME" : "Resist energy (type) 20 (potion)", "VALUE" : "70 gp"},
    "(21,28)" : {"NAME" : "Cure serious wounds (potion)", "VALUE" : "75 gp"},
    "(29,29)" : {"NAME" : "Daylight (oil)", "VALUE" : "75 gp"},
    "(30,32)" : {"NAME" : "Displacement (potion)", "VALUE" : "75 gp"},
    "(33,33)" : {"NAME" : "Flame arrow (oil)", "VALUE" : "75 gp"},
    "(34,38)" : {"NAME" : "Fly (potion)", "VALUE" : "75 gp"},
    "(39,39)" : {"NAME" : "Gaseous form (potion)", "VALUE" : "75 gp"},
    "(40,41)" : {"NAME" : "Haste (potion)", "VALUE" : "75 gp"},
    "(42,44)" : {"NAME" : "Heroism (potion)", "VALUE" : "75 gp"},
    "(45,46)" : {"NAME" : "Keen edge (oil)", "VALUE" : "75 gp"},
    "(47,47)" : {"NAME" : "Magic circle against (alignment) (potion)", "VALUE" : "75 gp"},
    "(48,50)" : {"NAME" : "Neutralize poison (potion)", "VALUE" : "75 gp"},
    "(51,52)" : {"NAME" : "Nondetection (potion)", "VALUE" : "75 gp"},
    "(53,54)" : {"NAME" : "Protection from energy (type) (potion)", "VALUE" : "75 gp"},
    "(55,55)" : {"NAME" : "Rage (potion)", "VALUE" : "75 gp"},
    "(56,56)" : {"NAME" : "Remove blindness/deafness (potion)", "VALUE" : "75 gp"},
    "(57,57)" : {"NAME" : "Remove curse (potion)", "VALUE" : "75 gp"},
    "(58,58)" : {"NAME" : "Remove disease (potion)", "VALUE" : "75 gp"},
    "(59,59)" : {"NAME" : "Tongues (potion)", "VALUE" : "75 gp"},
    "(60,60)" : {"NAME" : "Water breathing (potion)", "VALUE" : "75 gp"},
    "(61,61)" : {"NAME" : "Water walk (potion)", "VALUE" : "75 gp"},
    "(62,63)" : {"NAME" : "Barkskin +4 (potion)", "VALUE" : "90 gp"},
    "(64,64)" : {"NAME" : "Shield of faith +5 (potion)", "VALUE" : "90 gp"},
    "(65,65)" : {"NAME" : "Good hope (potion)", "VALUE" : "105 gp"},
    "(66,68)" : {"NAME" : "Resist energy (type) 30 (potion)", "VALUE" : "110 gp"},
    "(69,69)" : {"NAME" : "Barkskin +5 (potion)", "VALUE" : "120 gp"},
    "(70,73)" : {"NAME" : "Greater magic fang +2 (potion)", "VALUE" : "120 gp"},
    "(74,77)" : {"NAME" : "Greater magic weapon +2 (oil)", "VALUE" : "120 gp"},
    "(78,81)" : {"NAME" : "Magic vestment +2 (oil)", "VALUE" : "120 gp"},
    "(82,82)" : {"NAME" : "Protection from arrows 15/magic (potion)", "VALUE" : "150 gp"},
    "(83,85)" : {"NAME" : "Greater magic fang +3 (potion)", "VALUE" : "180 gp"},
    "(86,88)" : {"NAME" : "Greater magic weapon +3 (oil)", "VALUE" : "180 gp"},
    "(89,91)" : {"NAME" : "Magic vestment +3 (oil)", "VALUE" : "180 gp"},
    "(92,93)" : {"NAME" : "Greater magic fang +4 (potion)", "VALUE" : "240 gp"},
    "(94,95)" : {"NAME" : "Greater magic weapon +4 (oil)", "VALUE" : "240 gp"},
    "(96,97)" : {"NAME" : "Magic vestment +4 (oil)", "VALUE" : "240 gp"},
    "(98,98)" : {"NAME" : "Greater magic fang +5 (potion)", "VALUE" : "300 gp"},
    "(99,99)" : {"NAME" : "Greater magic weapon +5 (oil)", "VALUE" : "300 gp"},
    "(100,100)" : {"NAME" : "Magic vestment +5 (oil)", "VALUE" : "300 gp"}
}

def roll_potion(result : MapList, ring_table):
    item_data = roll_table(ring_table)
    result.add(item_data["NAME"], item_data["VALUE"])


def roll_minor_potion(result : MapList):
    roll_potion(result, POTIONS_MINOR)


def roll_medium_potion(result : MapList):
    roll_potion(result, POTIONS_MEDIUM)


def roll_major_potion(result : MapList):
    roll_potion(result, POTIONS_MAJOR)
