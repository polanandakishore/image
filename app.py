from flask import Flask, render_template, send_from_directory
import os

app = Flask(_name_)

# Define the path for images
IMAGE_FOLDER = os.path.join('static', 'images')
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER

# Route to serve the homepage with the image gallery
@app.route('/')
def index():
    # Get all image file names in the static/images folder
    image_files = os.listdir(app.config['IMAGE_FOLDER'])
    image_files = [f for f in image_files if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    return render_template('index.html', images=image_files)

# Route to serve an image from the static folder
@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory(app.config['IMAGE_FOLDER'], filename)

if _name_ == '_main_':
    app.run(debug=True)