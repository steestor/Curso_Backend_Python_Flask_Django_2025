from zona_fit_db.conexion import Conexion
from cliente import Cliente


class ClienteDAO:
    SELECCIONAR =  "select * from cliente order by id"
    INSERTAR = "insert into cliente(nombre, apellido, membresia) values (%s, %s, %s)"
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

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(ClienteDAO.INSERTAR, valores)
            conexion.commit()

            return cursor.rowcount

        except Exception as e:
            print(f"No se ha podido insertar el cliente {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == "__main__":
    # Insertar cliente
    cliente1 = Cliente(nombre="Alejandra", apellido="Tellez", membresia=300)
    clientes_actualizados = ClienteDAO.insertar(cliente1)
    print(f"Clientes insertados: {clientes_actualizados}")

    # Seleccionar los clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)