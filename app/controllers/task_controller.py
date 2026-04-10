from database.connection import DatabaseConnection


class TaskController:

    def __init__(self):
        self.db = DatabaseConnection()

    # ✅ CREATE TASK
    def create_task(self, task):

        connection = None
        cursor = None

        try:

            connection = self.db.connect()
            cursor = connection.cursor()

            query = """
            INSERT INTO tasks (title, description, status)
            VALUES (%s, %s, %s)
            """

            # Default status if empty
            status = task.status if task.status else "pending"

            values = (
                task.title,
                task.description,
                status
            )

            cursor.execute(query, values)

            connection.commit()

            print("✔ Task created")

        except Exception as e:

            print("❌ Error creating task:")
            print(e)

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()

    # ✅ GET TASKS
    def get_tasks(self):

        connection = None
        cursor = None

        try:

            connection = self.db.connect()
            cursor = connection.cursor()

            query = """
            SELECT id, title, description, status
            FROM tasks
            ORDER BY id DESC
            """

            cursor.execute(query)

            tasks = cursor.fetchall()

            return tasks

        except Exception as e:

            print("❌ Error fetching tasks:")
            print(e)

            return []

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()

    # ✅ DELETE TASK
    def delete_task(self, task_id):

        connection = None
        cursor = None

        try:

            connection = self.db.connect()
            cursor = connection.cursor()

            query = "DELETE FROM tasks WHERE id=%s"

            cursor.execute(query, (task_id,))

            connection.commit()

            print("✔ Task deleted")

        except Exception as e:

            print("❌ Error deleting task:")
            print(e)

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()

    # ✅ UPDATE STATUS (optional but recommended)
    def update_status(self, task_id, new_status):

        connection = None
        cursor = None

        try:

            connection = self.db.connect()
            cursor = connection.cursor()

            query = """
            UPDATE tasks
            SET status=%s
            WHERE id=%s
            """

            cursor.execute(
                query,
                (new_status, task_id)
            )

            connection.commit()

            print("✔ Status updated")

        except Exception as e:

            print("❌ Error updating status:")
            print(e)

        finally:

            if cursor:
                cursor.close()

            if connection:
                connection.close()