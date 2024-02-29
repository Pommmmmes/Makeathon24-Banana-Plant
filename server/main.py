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

# def calculate_ripeness_percentage(r, g, b):

# 	rgb_color = (r, g, b)
# 	unripe_color = (0, 255, 0)
# 	ripe_color = (255, 255, 0)

# 	total_distance = sum((unripe_color[i] - ripe_color[i]) ** 2 for i in range(3))
# 	ripe_distance = sum((rgb_color[i] - ripe_color[i]) ** 2 for i in range(3))

# 	if (total_distance == 0):
# 		return 100

# 	ripeness_percentage = (1 - (ripe_distance / total_distance)) * 100
# 	return ripeness_percentage


# def initialize_db(
# def initialize_db():
# add_row(uuid: str, id: str, timestamp: int , temp: int,
            # humidity: int, red: int, green: int, blue: int):
# def delete_row(row_uuid):

# add_row(uuid: str, id: str, timestamp: int , temp: int,
            # humidity: int, red: int, green: int, blue: int):
# def delete_row(row_uuid):
