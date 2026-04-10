import time
import mysql.connector


import mysql.connector


class DatabaseConnection:

    def connect(self):
        try:
            connection = mysql.connector.connect(
                host="https://mysql8-0-latest.onrender.com/",          # nombre del servicio docker
                user="user",
                password="user123",    # ← IMPORTANTE
                database="taskdb"
            )

            print("✔ Conectado a MySQL")

            return connection

        except mysql.connector.Error as err:

            print("❌ Error al conectar a MySQL:")
            print(err)

            raise Exception("No se pudo conectar a MySQL")