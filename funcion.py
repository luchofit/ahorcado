import os
import random


def clear(): #También la podemos llamar cls (depende a lo que estemos acostumbrados)
        os.system ("cls")

def read_data():
    data = []
    with open("./ahorcados/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            data.append(line)

def run():
    pass



if __name__ == "__main__":
    clear()
    read_data() 
    run()