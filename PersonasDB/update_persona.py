import mysql.connector

personas_db = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    passwd="admin",
    database="personas_db"
)

# Ejecutar sentencia update
cursor = personas_db.cursor()
sentencia_sql = "UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id=%s"
valores = ("carlota", "test", 31, 7)

cursor.execute(sentencia_sql, valores)
print("Se ha actualizado el registro.")

personas_db.commit()

personas_db.close()
cursor.close()