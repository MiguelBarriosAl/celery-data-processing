from flask import Flask, jsonify
from tasks import task_upload_file, task_id_state
from utils import csv_to_json

app = Flask(__name__)


@app.route("/upload/<name_file>", methods=["POST"])
def upload_file(name_file: str):
    task = task_upload_file.delay(name_file)
    return jsonify({"task_id": task.id})


@app.route("/task/<task_id>", methods=["GET"])
def processed_file(task_id):
    task_state = task_id_state.delay(task_id)
    if task_state:
        output_data = csv_to_json()
    return jsonify(output_data)


if __name__ == '__main__':
    app.run(debug=True)
