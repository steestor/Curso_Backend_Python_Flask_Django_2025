from zona_fit_db.conexion import Conexion
from cliente import Cliente


class ClienteDAO:
    SELECCIONAR =  "select * from cliente order by id"
    INSERTAR = "insert into cliente values (nombre, apellido, membresia) values (%s, %s, %s)"
    ACTUALIZAR = "update cliente set nombre=%s, apellido=%s, membresia=%s where id=%s"
    ELIMINAR = "delete from cliente where id=%s"

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion= Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()

            # Mapeo de clase-tabla cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes

        except Exception as e:
            print(f"Ocurrio un error al seleccionar los clientes: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == "__main__":
    # Seleccionar los clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)