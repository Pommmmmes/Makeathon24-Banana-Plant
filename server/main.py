from flask import Flask, render_template, jsonify, request, send_file
from PIL import Image
import sqlite_utils
import uuid


def calculate_ripeness_percentage(r, g, b):

	rgb_color = (r, g, b)
	unripe_color = (0, 255, 0)
	ripe_color = (255, 255, 0)

	total_distance = sum((unripe_color[i] - ripe_color[i]) ** 2 for i in range(3))
	ripe_distance = sum((rgb_color[i] - ripe_color[i]) ** 2 for i in range(3))

	if (total_distance == 0):
		return 100

	ripeness_percentage = (1 - (ripe_distance / total_distance)) * 100
	return ripeness_percentage

app = Flask(__name__)

@app.route('/', methods=["GET"])
def display():
    return (render_template('hello.html'))

@app.route('/images/banana.svg')
def display_svg():
    with open('./templates/images/banana.svg', 'r') as f:
        svg_content = f.read()

    return svg_content, 200, {'Content-Type': 'image/svg+xml'}

# @app.route('/humidity_data')
# def display_humidity():
#     humidity_data = sqlite_utils.get_array_from_db()
#     graph = create_plot.plot_soil_moisture(humidity_data)




@app.route('/recieve', methods=["POST"])
def process_data():
    if request.is_json:
        json_data = request.json
        try:
            sqlite_utils.add_row(str(uuid.uuid4()), json_data["id"], json_data["timestamp"],
                    json_data["temperature"], json_data["humidity"], json_data["red"],
                    json_data["green"], json_data["blue"])
            return "Success"
        except:
            return "Wrong data json file"
    else:
        return jsonify({"error": "No JSON data received"}), 400

def main():
    sqlite_utils.initialize_db()
    app.run(host='0.0.0.0', port=8080, debug=True)

main()

# {
#   "uuid": "banana",
#   "id": "1",
#   "timestamp": "2024-02-28T12:34:56",
#   "humidity": "40",
#   "red": "150",
#   "green": 255,
#   "blue": 0
# }
# def initialize_db(
# def initialize_db():
# add_row(uuid: str, id: str, timestamp: int , temp: int,
            # humidity: int, red: int, green: int, blue: int):
# def delete_row(row_uuid):

# add_row(uuid: str, id: str, timestamp: int , temp: int,
            # humidity: int, red: int, green: int, blue: int):
# def delete_row(row_uuid):
