#intalar con pip "pip install mysql-connector-python"
import mysql.connector 
from mysql.connector import Error

try: 
    conexion = mysql.connector.connect(
        host='localhost', 
        port='3306',
        user='root',
        password='aa9797',
        db='nom_texto'
        )
    
    if conexion.is_connected():
        print("Conexion establecida")
        cursor = conexion.cursor()
        nombre=input("Ingresa el nombre: ") 
        #cursor.execute("INSERT INTO nom_texto (nombre) VALUES ('')")
        sentencia = "INSERT INTO entrada (nombre) VALUES ('{0}')".format(nombre)
        cursor.execute(sentencia)
        conexion.commit()
        print("Insercion exitosa")  
        
        
     

except Error as ex:
    print("Error en conexion")
finally:
    if conexion.is_connected():
        file = open("{0}.txt".format(nombre), "w")
        file.write(nombre)
        conexion.close()
        print("conexion finalizada") 
