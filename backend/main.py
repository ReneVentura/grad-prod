from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import json  # Importar el módulo json para parsear la cadena JSON
import ai_svc

app = Flask(__name__)


# Configura la carpeta donde se guardarán las imágenes cargadas
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Función para comprobar que el archivo es una imagen
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    # Comprobar si la petición tiene el archivo
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']

    # Si el usuario no selecciona archivo, el navegador envía una parte sin nombre de archivo
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Intentar obtener datos adicionales como JSON desde el formulario
    data = {}
    if 'data' in request.form:
        try:
            data = json.loads(request.form['data'])
        except json.JSONDecodeError:
            return jsonify({'error': 'Invalid JSON data'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        

        
        try:

            phrase = ai_svc.create_fragment_from_image(data, file_path)
            os.remove(file_path)
        
            return jsonify({'message': phrase}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500


    return jsonify({'error': 'Invalid file type'}), 400



CORS(app)