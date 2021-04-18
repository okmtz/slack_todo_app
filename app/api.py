from flask import Flask, request, jsonify;
from app.database import init_db;
from app.database import db;
from models.models import Task;


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    init_db(app)

    return app

app = create_app()

@app.route('/tasks', methods=["GET", "POST"])
def tasks():
    task = None
    if request.form:
        try:
            task = Task(title=request.form.get("title"))
            db.session.add(task)
            db.session.commit()
        except Exception as e:
            print("Failed to add task")
            print(e)

    tasks = Task.query.all()
    return jsonify(tasks=[(i.serialize()) for i in tasks])
