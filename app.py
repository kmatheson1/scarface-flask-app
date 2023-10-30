from flask import Flask, request, render_template, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def index():
    render_template('upload.html')


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0"
    )
