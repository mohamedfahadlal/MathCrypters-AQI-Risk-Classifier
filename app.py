from flask import Flask, jsonify, send_from_directory
import json

app = Flask(__name__, static_folder=".")

@app.route("/")
def home():
    return send_from_directory(".", "mv.html")

@app.route("/map")
def map_page():
    return send_from_directory(".", "map.html")

@app.route("/api/prediction")
def get_prediction():
    with open("predicted_aqi.json") as f:
        data = json.load(f)
    return jsonify(data)

@app.route("/api/clusters")
def get_clusters():
    with open("city_clusters.json") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
