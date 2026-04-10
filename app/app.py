from flask import Flask, render_template

from controllers.task_controller import TaskController

app = Flask(__name__)

controller = TaskController()


@app.route("/")
def index():

    tasks = controller.get_tasks()

    return render_template(
        "index.html",
        tasks=tasks
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )