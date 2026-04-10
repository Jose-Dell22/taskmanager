from database.connection import DatabaseConnection


class TaskController:

    def __init__(self):
        self.db = DatabaseConnection()

    def create_task(self, task):

        connection = self.db.connect()
        cursor = connection.cursor()

        query = """
        INSERT INTO tasks (title, description, status)
        VALUES (%s, %s, %s)
        """

        values = (
            task.title,
            task.description,
            task.status
        )

        cursor.execute(query, values)

        connection.commit()

        cursor.close()
        connection.close()

    def get_tasks(self):

        connection = self.db.connect()
        cursor = connection.cursor()

        query = "SELECT * FROM tasks"

        cursor.execute(query)

        tasks = cursor.fetchall()

        cursor.close()
        connection.close()

        return tasks

    def delete_task(self, task_id):

        connection = self.db.connect()
        cursor = connection.cursor()

        query = "DELETE FROM tasks WHERE id=%s"

        cursor.execute(query, (task_id,))

        connection.commit()

        cursor.close()
        connection.close()