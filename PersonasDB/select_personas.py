import mysql.connector

personas_db = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    passwd="admin",
    database="personas_db"
)

# Ejecutar sentencia select
cursor = personas_db.cursor()
cursor.execute("SELECT * FROM personas")
result = cursor.fetchall()

for persona in result:
    print(persona)

# Cerramos la conexión
cursor.close()
personas_db.close()