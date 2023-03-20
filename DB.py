import sqlite3
from sqlite3 import Error


connection = sqlite3.connect("bycicle.db")


def velo(message,table):
    connection = sqlite3.connect("bycicle.db")
    cursor=connection.cursor()
    slovar=message.text
    words = [word.strip() for word in slovar.split(",")]  # Split the text into words and remove any leading/trailing whitespace
    quoted_words = [f'"{word}"' for word in words]  # Add quotes around each word

    result = ", ".join(quoted_words)

    electro="INSERT INTO VELO(name, frame, fork, fwheels, bwheels, Fbrake, Bbrake, fsw, bsw, weight, price, vid) " \
        "VALUES ("+str(result)+",'"+table+"');"
    print(slovar)
    print (electro)
    # Сохраняем изменения
    cursor.execute(electro)
    connection.commit()

    cursor.close()
    connection.close()

def search(table):
    connection = sqlite3.connect("bycicle.db")
    cursor=connection.cursor()
    
    otvet=cursor.execute("SELECT * FROM VELO WHERE vid=?",[table]).fetchall()
    print(otvet[0])
    
    
    connection.commit()
    cursor.close()
    connection.close()
    return otvet