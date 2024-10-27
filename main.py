#! /usr/bin/python3
from data import treashuretable_3_5 as t3_5
import sys



def main(level = 1):

    random_result = t3_5.roll_random_treasure(level)
    print(random_result)
    
    

if __name__ == "__main__":
    level = int(sys.argv[1])
    # print(level)
    main(level)