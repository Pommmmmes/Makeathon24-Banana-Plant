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
def hello():
    return render_template('hello.html')

@app.route('/banana', methods=["GET"])
def display():
    return (render_template('banana.html'))

@app.route('/images/temp.jpg')
def send_jpg():
     return (send_file('./templates/images/temp.jpg', mimetype='image/jpeg'))

@app.route('/recieve', methods=["POST"])
def process_data():
    if request.is_json:
        json_data = request.json
        try:
            sqlite_utils.add_row(str(uuid.uuid4()), json_data["id"], json_data["timestamp"],
                    json_data["temperature"], json_data["humidity"], json_data["red"],
                    json_data["green"], json_data["blue"])
            image_path = './templates/images/banana.jpg'
            img = Image.open(image_path)

            width, height = img.size
            crop_width = int(width * (round(calculate_ripeness_percentage(int(json_data["red"]), int(json_data["green"]), int(json_data["blue"])), 2) / 100))
            crop_height = height

            cropped_img = img.crop((0, 0, crop_width, crop_height))

            cropped_img_path = './templates/images/temp.jpg'
            cropped_img.save(cropped_img_path)

            return "Succesfully uploaded!"
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
