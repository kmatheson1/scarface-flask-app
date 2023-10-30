from flask import Flask, request, render_template, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def index():
    render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    #checks for file
    if 'file' not in request.files:
        return 'No file.'
    file = request.files['file']
    #checks for filename
    if file.filename == '':
        return 'No file slected.'
    if file:
        #creates pathe
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        #saves file to specified path UPLOAD_FOLDER
        file.save(filename)
        return 'File uploaded successfully'

@app.route('/uploads/<filename>')
#returns file to user upon specific url request
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0"
    )
