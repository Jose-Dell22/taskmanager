from database.connection import DatabaseConnection


class TaskController:

    def __init__(self):
        self.db = DatabaseConnection()

    # =========================
    # CREATE TASK
    # =========================
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

            status = task.status if task.status else "pending"

            cursor.execute(query, (
                task.title,
                task.description,
                status
            ))

            connection.commit()
            print("✔ Task created")

        except Exception as e:
            print("❌ Error creating task:", e)

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    # =========================
    # GET ALL TASKS
    # =========================
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
            return cursor.fetchall()

        except Exception as e:
            print("❌ Error fetching tasks:", e)
            return []

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    # =========================
    # GET TASK BY ID
    # =========================
    def get_task_by_id(self, task_id):

        connection = self.db.connect()
        cursor = connection.cursor()

        query = "SELECT id, title, description, status FROM tasks WHERE id=%s"

        cursor.execute(query, (task_id,))
        task = cursor.fetchone()

        cursor.close()
        connection.close()

        return task

    # =========================
    # DELETE TASK
    # =========================
    def delete_task(self, task_id):

        connection = None
        cursor = None

        try:
            connection = self.db.connect()
            cursor = connection.cursor()

            cursor.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
            connection.commit()

            print("✔ Task deleted")

        except Exception as e:
            print("❌ Error deleting task:", e)

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    # =========================
    # UPDATE STATUS
    # =========================
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

            cursor.execute(query, (new_status, task_id))
            connection.commit()

            print("✔ Status updated")

        except Exception as e:
            print("❌ Error updating status:", e)

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

    # =========================
    # EDIT TASK (TITLE + DESCRIPTION)
    # =========================
    def edit_task(self, task_id, title, description, status):

        connection = None
        cursor = None

        try:
            connection = self.db.connect()
            cursor = connection.cursor()

            query = """
            UPDATE tasks
            SET title=%s,
                description=%s,
                status=%s
            WHERE id=%s
            """

            cursor.execute(query, (
                title,
                description,
                status,
                task_id
            ))

            connection.commit()

            print("✔ Task updated")

        except Exception as e:
            print("❌ Error updating task:", e)

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()