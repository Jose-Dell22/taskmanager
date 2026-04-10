import time
import mysql.connector


class DatabaseConnection:

    def connect(self):
        for i in range(10):
            try:
                connection = mysql.connector.connect(
                    host="db",          # nombre del servicio docker
                    user="root",
                    password="root",
                    database="taskdb"
                )
                print("✔ Conectado a MySQL")
                return connection

            except mysql.connector.Error as err:
                print(f"MySQL no listo (intento {i+1})... reintentando")
                time.sleep(3)

        raise Exception("❌ No se pudo conectar a MySQL después de varios intentos")