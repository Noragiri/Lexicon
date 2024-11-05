from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for tasks
tasks = []
task_counter = 1


# GET endpoint to retrieve all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks), 200


# POST endpoint to add a new task
@app.route("/tasks", methods=["POST"])
def add_task():
    global task_counter
    task_data = request.get_json()
    if "title" not in task_data:
        return jsonify({"error": "Task must have a title"}), 400

    task = {
        "id": task_counter,
        "title": task_data["title"],
        "completed": task_data.get("completed", False),
    }
    tasks.append(task)
    task_counter += 1
    return jsonify(task), 201


# DELETE endpoint to remove a task by ID
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]
    return jsonify({"message": "Task deleted"}), 200


if __name__ == "__main__":
    app.run(debug=True)
