from flask import ( Flask, request, render_template,
                    send_from_directory, flash, 
                    redirect, url_for )
import os
import secrets

app = Flask(__name__)

#secret key generated
secret_key = secrets.token_hex(16)
app.config['SECRET_KEY'] = secret_key

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/", methods=['GET', 'POST'])
def index():
    # saves list of images in 'uploads' to variable
    uploaded_images = os.listdir('uploads')
    # if an image is uplated will used the upload route
    if request.method == 'POST':
        return upload(uploaded_images)
    return render_template('upload.html', uploaded_images=uploaded_images)

@app.route('/upload', methods=['POST'])
def upload(uploaded_images):
    # checks for file
    if 'file' not in request.files:
        flash('No file.')
        return redirect(url_for('index'))

    file = request.files['file']
    # checks for filename
    if file.filename == '':
        flash('No file selected.')
        return redirect(url_for('index'))

    # creates path
    filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    # saves file to the specified path UPLOAD_FOLDER
    file.save(filename)
    flash('File uploaded successfully')

    return redirect(url_for('index'))

@app.route('/uploads/<filename>')
#returns file to user upon specific url request
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0"
    )
