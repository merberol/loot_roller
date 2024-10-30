from data.scrolls import *
from utils.map_list import MapList


def test_roll_minor_scroll():
    print("testing roll minor scroll")
    res = MapList()
    roll_minor_scroll(res)
    print(res)


def test_roll_medium_scroll():
    print("testing roll medium scroll")
    res = MapList()
    roll_medium_scroll(res)
    print(res)


def test_roll_major_scroll():
    print("testing roll major scroll")
    res = MapList()
    roll_major_scroll(res)
    print(res)
