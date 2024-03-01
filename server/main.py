from flask import Flask, render_template, jsonify, request, send_file
from PIL import Image
import sqlite_utils
import uuid
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import datetime

app = Flask(__name__,  static_url_path='/static')

@app.route('/', methods=["GET"])
def display():
    return (render_template('./html/bubble.html'))

@app.route('/images/marker-icon-2x-red.png', methods=["GET"])
def display_png_red():
    return send_file('./templates/images/marker-icon-2x-red.png', mimetype='image/png')

@app.route('/images/marker-icon-blue.png', methods=["GET"])
def display_png_blue():
    return send_file('./templates/images/marker-icon-blue.png', mimetype='image/png')

@app.route('/id=<id>')
def display_plant_data(id):
    data = sqlite_utils.get_id_data(id)
    temperature = data[-1][2]
    humidity = data[-1][3]
    ripeness = sqlite_utils.calculate_ripeness_percentage(data[-1][5], data[-1][6], data[-1][7])
    return render_template('./html/banana_bush.html', temperature=temperature, humidity=humidity, ripeness=ripeness)

@app.route('/images/banana.svg')
def display_svg():
    with open('./templates/images/banana.svg', 'r') as f:
        svg_content = f.read()

    return svg_content, 200, {'Content-Type': 'image/svg+xml'}

@app.route('/images/sky.jpg')
def display_background():
    return send_file('./templates/images/sky.jpg', mimetype='image/jpg')

@app.route('/images/new_plot.png', methods=["GET"])
def show_graph():
    return send_file('./templates/images/new_plot.png', mimetype='image/png')

@app.route('/images/bn_button.png', methods=["GET"])
def display_banana_button():
    return send_file('./templates/images/bn_button.png', mimetype='image/png')

@app.route('/images/bananaplantation.jpeg', methods=["GET"])
def display_banana_plantation():
    return send_file('./templates/images/bananaplantation.jpeg', mimetype='image/jpeg')

@app.route('/map', methods=["GET"])
def show_map():
    return send_file('./templates/html/map.html')

@app.route('/data=<id>', methods=["GET"])
def display_details(id):
    humidity_data = sqlite_utils.get_array_from_db("humidity", id)
    temperature_data = sqlite_utils.get_array_from_db("temperature", id)
    growth_data = sqlite_utils.get_percentage_arr(id)
    today = datetime.date.today()
    dates = [str(today - datetime.timedelta(days=i)) for i in range(6, -1, -1)]

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 10))

   # Plot humidity data
    ax1.plot(dates, humidity_data[-7:], marker='o', linestyle='-')
    ax1.set_title('Humidity')
    ax1.set_ylabel('Moisture (%)')
    ax1.set_xticklabels(dates, rotation=45)
    ax1.set_ylim(0, 100)
    ax1.grid(True)

    # Plot temperature data
    ax2.plot(dates, temperature_data[-7:], marker='o', linestyle='-')
    ax2.set_title('Temperature')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Temperature (°C)')
    ax2.set_xticklabels(dates, rotation=45)
    ax2.grid(True)

    # Plot growth data
    ax3.plot(dates, growth_data[-7:], marker='o', linestyle='-')
    ax3.set_title('Growth')
    ax3.set_ylabel('Ripeness (%)')
    ax3.set_xticklabels(dates, rotation=45)
    ax3.set_ylim(0, 100)
    ax3.grid(True)

    plt.tight_layout()
    plt.savefig('./templates/images/new_plot.png')
    return render_template('./html/details.html')

@app.route('/recieve', methods=["POST"])
def process_data():
    if request.is_json:
        json_data = request.json
        try:
            sqlite_utils.add_row(str(uuid.uuid4()), json_data["id"], (datetime.datetime.now()).strftime("%Y-%m-%dT%H:%M:%S"),
                    json_data["temperature"], json_data["humidity"], json_data["red"],
                    json_data["green"], json_data["blue"], json_data["ripe"])
            return "Success", 201
        except KeyError:
            return "Wrong data json file", 406
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
