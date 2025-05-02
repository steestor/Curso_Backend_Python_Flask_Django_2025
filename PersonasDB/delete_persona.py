import mysql.connector

personas_db = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    passwd="admin",
    database="personas_db"
)

# Ejecutar sentencia delete
cursor = personas_db.cursor()
sentencia_sql = "DELETE FROM personas WHERE id=%s"
cursor.execute(sentencia_sql,(7,))

print("Se ha eliminado el registro")
personas_db.commit()
