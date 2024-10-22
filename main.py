from data import treashuretable_3_5 as t3_5
import json


def main():
    new = {}
    for key,value in t3_5.TABLE.items():
        new_val = {}

        for key2, value2 in value.items():
            key2 = str(key2)
            new_value2 = {}
            for key3, value3 in value2.items():
                key3 = str(key3)
                new_value2[key3] = value3
            new_val[str(key2)] = new_value2
        
        new[str(key)] = new_val
                

    f = open("data/t3_5.json", "w")
    json.dump(new, f)
    f.close

if __name__ == "__main__":
    main()