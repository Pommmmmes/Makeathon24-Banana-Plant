from flask import Flask, render_template, jsonify, request, send_file
from PIL import Image
import sqlite_utils
import uuid
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import datetime

app = Flask(__name__)

@app.route('/', methods=["GET"])
def display():
    return (render_template('./html/hello.html'))

@app.route('/images/banana.svg')
def display_svg():
    with open('./templates/images/banana.svg', 'r') as f:
        svg_content = f.read()

    return svg_content, 200, {'Content-Type': 'image/svg+xml'}

@app.route('/images/new_plot.png', methods=["GET"])
def show_graph():
    return send_file('./templates/images/new_plot.png', mimetype='image/png')

@app.route('/humidity_data', methods=["GET"])
def display_humidity():
    humidity_data = sqlite_utils.get_array_from_db()
    today = datetime.date.today()
    dates = [str(today - datetime.timedelta(days=i)) for i in range(6, -1, -1)]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, humidity_data[-7:], marker='o', linestyle='-')
    plt.title('Daily Soil Moisture of Last 7 Days')
    plt.xlabel('Date')
    plt.ylabel('Moisture (%)')
    plt.xticks(rotation=45)
    plt.ylim(0, 100)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('./templates/images/new_plot.png')
    return render_template('./html/humidity.html')

@app.route('/recieve', methods=["POST"])
def process_data():
    if request.is_json:
        json_data = request.json
        try:
            sqlite_utils.add_row(str(uuid.uuid4()), json_data["id"], (datetime.datetime.now()).strftime("%Y-%m-%dT%H:%M:%S"),
                    json_data["temperature"], json_data["humidity"], json_data["red"],
                    json_data["green"], json_data["blue"])
            return "Success", 201
        except:
            return "Wrong data json file"
    else:
        return jsonify({"error": "No JSON data received"}), 400

@app.route('/coordinates', methods=["GET"])
def get_coordinates():
    return send_file("./templates/json/coordinates.json", mimetype='application/json')

@app.route('/percentages', methods=["GET"])
def get_percentages():
    return sqlite_utils.get_percentage_arr()

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
