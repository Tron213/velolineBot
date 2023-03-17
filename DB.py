import sqlite3
from sqlite3 import Error
import time

connection = sqlite3.connect("bycicle.db")


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
        connection.close
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def BDelectro(slovar,path):
    connection = sqlite3.connect(path)
    cursor=connection.cursor()
    time.sleep(10)
    
    "INSERT INTO Electro(name, frame, fork, fwheels, bwheels, Fbrake, Bbrake, fsw, bsw, weight, price) " \
        "VALUES ("+slovar+")"
    
    # Сохраняем изменения
    connection.commit()
    cursor.close()
    connection.close()
    

#cursor=connection.cursor()

#cursor.execute(f"""  INSERT INTO Electro(name, frame, fork, fwheels, bwheels, Fbrake, Bbrake, fsw, bsw, weight, price) VALUES("ds","ds","df","gff","hg","yt","nh","xc","kk","qw","dc") """)

#connection.commit()
#cursor.close()
#connection.close()