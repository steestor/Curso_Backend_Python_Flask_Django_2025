import mysql.connector

personas_db = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    passwd="admin",
    database="personas_db"
)

# Ejecutar sentencia insert
cursor = personas_db.cursor()
sentencia_sql = "INSERT INTO personas(nombre, apellido, edad) VALUES (%s, %s, %s)"
valores = ("carla", "test", 37)

cursor.execute(sentencia_sql, valores)
print("Se ha insertado el registro.")

personas_db.commit()

personas_db.close()
cursor.close()