from flask import Flask, render_template, jsonify, send_from_directory
from pathlib import Path
import json

app = Flask(__name__)

RESULTS_PATH = Path('results')
@app.route("/")
def index():
    #TODO: import wyników z folteru results

    return render_template("index.html")

@app.route("/frequency_table")
def frequency_table_page():
    return render_template("frequency_table.html")

@app.route("/common_nouns")
def common_nouns_view():
    return render_template("common_nouns.html")




@app.route("/api/frequency_table")
def frequency_table():
    return jsonify(json.loads((RESULTS_PATH / "frequency_table.json").read_text()))


@app.route("/api/common_nouns")
def common_nouns():
    return jsonify(json.loads((RESULTS_PATH / "common_nouns.json").read_text()))


if __name__ == "__main__":
    app.run(debug=True)
