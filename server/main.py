from flask import Flask, render_template, jsonify, request
import sqlite_utils

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello():
    return render_template('hello.html')

@app.route('/recieve', methods=["POST"])
def process_data():
    if request.is_json:
        json_data = request.json
        try:
            return json_data["time"]
        except KeyError:
            return "Wrong data json file"
    else:
        return jsonify({"error": "No JSON data received"}), 400



def main():
    sqlite_utils.initialize_db()
    app.run(host='0.0.0.0', port=8080, debug=True)

main()

# def initialize_db(
# def initialize_db():
# add_row(uuid: str, id: str, timestamp: int , temp: int,
            # humidity: int, red: int, green: int, blue: int):
# def delete_row(row_uuid):

# add_row(uuid: str, id: str, timestamp: int , temp: int,
            # humidity: int, red: int, green: int, blue: int):
# def delete_row(row_uuid):
