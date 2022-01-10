import os
import random
import unicodedata


def clear(): #También la podemos llamar cls (depende a lo que estemos acostumbrados)
        os.system ("cls")

def drawHangMan(tried):

    if tried == 1:
        print("""
         _____
             |
             |
             |
             |
        _____|_____     
               
    """)
    if tried == 2:
        print("""
         _____
         O   |
             |
             |
             |
        _____|_____
        
    """)
    if tried == 3:
        print("""
         _____
         O   |
         |   |
             |
             |
        _____|_____
        
    """)
    if tried == 4:
        print("""
         _____
         O   |
         |__ |
             |
             |
        _____|_____
        
    """)
    if tried == 5:
        print("""
         _____
         O   |
       __|__ |
             |
             |
        _____|_____
        
    """)
    
    if tried == 6:
        print("""
         _____
         O   |
       __|__ |
         |   |
             |
        _____|_____
        
    """)
    if tried == 7:
        print("""
         _____
         O   |
       __|__ |
         |   |
        /    |
        _____|_____
        
    """)
    if tried == 8:
        print("""
         _____
         O   |
       __|__ |
         |   |
        / \  |
        _____|_____
        
    """)

def listOfSpacing(word):
    resolving = []
    for l in word:
        resolving.append("_ ")
    resolving.pop()
    return resolving

def listOfWord(word):
        word  = ''.join(c for c in unicodedata.normalize('NFD', word)
            if unicodedata.category(c) != 'Mn')
        listWords = [l for l in word]
        listWords.pop()
        return listWords

def read_data():
    data = []
    with open("C:/Users/57320/Desktop/platzi/python/ahorcados/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u")
            data.append(line)
    word = random.choice(data)
    return word
    
    

def run():
    word = read_data()
    word_final = word.strip()
    listWord = listOfWord(word)
    listSpacing = listOfSpacing(word)
    tried = 1
    resolve = False
    
    bienvenida = """"
     ▄▄▄▄    ██▓▓█████  ███▄    █ ██▒   █▓▓█████  ███▄    █  ██▓▓█████▄  ▒█████  
▓█████▄ ▓██▒▓█   ▀  ██ ▀█   █▓██░   █▒▓█   ▀  ██ ▀█   █ ▓██▒▒██▀ ██▌▒██▒  ██▒
▒██▒ ▄██▒██▒▒███   ▓██  ▀█ ██▒▓██  █▒░▒███   ▓██  ▀█ ██▒▒██▒░██   █▌▒██░  ██▒
▒██░█▀  ░██░▒▓█  ▄ ▓██▒  ▐▌██▒ ▒██ █░░▒▓█  ▄ ▓██▒  ▐▌██▒░██░░▓█▄   ▌▒██   ██░
░▓█  ▀█▓░██░░▒████▒▒██░   ▓██░  ▒▀█░  ░▒████▒▒██░   ▓██░░██░░▒████▓ ░ ████▓▒░
░▒▓███▀▒░▓  ░░ ▒░ ░░ ▒░   ▒ ▒   ░ ▐░  ░░ ▒░ ░░ ▒░   ▒ ▒ ░▓   ▒▒▓  ▒ ░ ▒░▒░▒░ 
▒░▒   ░  ▒ ░ ░ ░  ░░ ░░   ░ ▒░  ░ ░░   ░ ░  ░░ ░░   ░ ▒░ ▒ ░ ░ ▒  ▒   ░ ▒ ▒░ 
 ░    ░  ▒ ░   ░      ░   ░ ░     ░░     ░      ░   ░ ░  ▒ ░ ░ ░  ░ ░ ░ ░ ▒  
 ░       ░     ░  ░         ░      ░     ░  ░         ░  ░     ░        ░ ░  
      ░                           ░                          ░               
    
    
    *Welcome to Ahorcados GAME*
    By lucho fit    
    
    """
    print(bienvenida)
    print(""" 
        Bienvenido/a al juego del ahorcado 
        la palabra que debes adivinar es """  +"_ "*len(word_final)
        +"Tienes " +str(len(word_final))+" intentos")
    
    while resolve == False:
        if listWord != listSpacing:
                if tried != 6:
                    drawHangMan(tried)
        try:
            choice = input(str("Elige una letra: "))
            if len(choice) < 1 or len(choice) > 1:
                raise ValueError("Debes ingresar una letra")
            if choice.isnumeric():
                raise ValueError("No puedes ingresar números")
            if choice in listWord:
                indices = [i for i in range(len(listWord)) if listWord[i] == choice]
                for i in indices:
                    listSpacing[i] = choice
                print(listSpacing)
            if listSpacing == listWord:
                print("haz adivinado la palabra")
                break
            else:
                tried += 1
                if tried > 8:
                    print("Haz pérdido")
                    break
        except ValueError as ve:
            print(ve)
            return ve

        
    
def again():
        
        print("""
        1 - Jugar de nuevo
        2 - Salirme del juego
        """) 

        try:
            revenge = input("¿Te gustaría jugar de nuevo? ")
            yes = 1
            if revenge.isalpha():
                raise ValueError("debes escribir un número")
            revenge = int(revenge)
            if revenge > 2:
                raise ValueError("Debes ingresar una opción valida")
            if revenge == yes:
                run()
            else:
                print("Nos vemos una próxima ocasión")
                
            
        except ValueError as va:
            print(va)
            return va

    

if __name__ == "__main__":
    clear()
    run()
    again()
    
