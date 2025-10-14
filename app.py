from flask import Flask, render_template, jsonify, send_from_directory
from pathlib import Path
import json

app = Flask(__name__)


@app.route("/")
def index():
    #TODO: import wyników z folteru results

    return render_template("index.html")




if __name__ == "__main__":

    app.run(debug=True)