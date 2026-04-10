from flask import Flask, render_template, request, redirect
from controllers.task_controller import TaskController
from models.task import Task

app = Flask(__name__)

controller = TaskController()


# =========================
# HOME
# =========================
@app.route("/")
def index():

    tasks = controller.get_tasks()

    return render_template(
        "index.html",
        tasks=tasks
    )


# =========================
# CREATE TASK
# =========================
@app.route("/create", methods=["POST"])
def create():

    title = request.form.get("title")
    description = request.form.get("description")
    status = request.form.get("status")

    task = Task(title, description, status)

    controller.create_task(task)

    return redirect("/")


# =========================
# DELETE TASK
# =========================
@app.route("/delete/<int:task_id>")
def delete(task_id):

    controller.delete_task(task_id)

    return redirect("/")


# =========================
# UPDATE STATUS (ya lo tienes)
# =========================
@app.route("/update_status/<int:task_id>", methods=["POST"])
def update_status(task_id):

    new_status = request.form.get("status")

    controller.update_status(task_id, new_status)

    return redirect("/")


# =========================
# ✏️ EDIT TASK (NUEVO)
# =========================

# Mostrar formulario con datos
@app.route("/edit/<int:task_id>")
def edit_form(task_id):

    task = controller.get_task_by_id(task_id)
    tasks = controller.get_tasks()

    return render_template(
        "index.html",
        tasks=tasks,
        task_to_edit=task
    )


# Guardar cambios
@app.route("/edit/<int:task_id>", methods=["POST"])
def edit(task_id):

    title = request.form.get("title")
    description = request.form.get("description")
    status = request.form.get("status")

    controller.edit_task(
        task_id,
        title,
        description,
        status
    )

    return redirect("/")


# =========================
# RUN
# =========================
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )