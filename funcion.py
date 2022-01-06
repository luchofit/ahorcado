import os
def clear(): #También la podemos llamar cls (depende a lo que estemos acostumbrados)
    if os.name == "posix":
        os.system ("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system ("cls")


def run():
    pass

if __name__ == "__main__":
    run()