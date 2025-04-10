from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import os
from PIL import Image
import uuid
from colorthief import ColorThief
import json

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_color_palette(image_path, color_count=5):
    color_thief = ColorThief(image_path)
    palette = color_thief.get_palette(color_count=color_count)
    return [f'rgb({r}, {g}, {b})' for r, g, b in palette]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/layouts')
def layouts():
    return render_template('layouts.html')

@app.route('/create', methods=['GET', 'POST'])
def create_moodboard():
    if request.method == 'POST':
        # Handle image uploads
        images = []
        color_palettes = []
        for file in request.files.getlist('images'):
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                unique_filename = f"{uuid.uuid4()}_{filename}"
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
                file.save(filepath)
                images.append(unique_filename)
                
                # Generate color palette for each image
                palette = get_color_palette(filepath)
                color_palettes.append(palette)
        
        # Get moodboard title and description
        title = request.form.get('title', 'Untitled Moodboard')
        description = request.form.get('description', '')
        layout = request.form.get('layout', 'simple-work')
        
        return render_template('moodboard.html', 
                             images=images,
                             color_palettes=color_palettes,
                             title=title,
                             description=description,
                             layout=layout)
    
    return render_template('create.html')

@app.route('/moodboard/<layout>')
def moodboard(layout):
    # Get any existing images and color palettes from the session or database
    images = []
    color_palettes = []
    
    return render_template('moodboard.html',
                         images=images,
                         color_palettes=color_palettes,
                         title=f"{layout.replace('-', ' ').title()} Moodboard",
                         description="",
                         layout=layout)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/save-arrangement', methods=['POST'])
def save_arrangement():
    data = request.json
    # Here you would typically save the arrangement to a database
    return jsonify({'status': 'success'})

@app.route('/add-images', methods=['POST'])
def add_images():
    images = []
    for file in request.files.getlist('images'):
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            unique_filename = f"{uuid.uuid4()}_{filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            file.save(filepath)
            images.append(unique_filename)
    
    return jsonify({
        'success': True,
        'images': images
    })

if __name__ == '__main__':
    app.run(debug=True) 