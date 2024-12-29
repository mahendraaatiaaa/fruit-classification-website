from flask import Flask, request, render_template, send_from_directory, jsonify
import os
from PIL import Image
import numpy as np
import onnxruntime as ort

# Flask app setup
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load ONNX model (global for efficiency)
MODEL_PATH = 'onnx_final2_with_softmax.onnx'
model = ort.InferenceSession(MODEL_PATH)

# Softmax function with temperature scaling
def softmax_with_temperature(x, temperature=0.1):  # Lower temperature for sharper results
    x = np.array(x, dtype=np.float32)  # Ensure float32
    shifted_x = x - np.max(x)  # Stabilize for numerical stability
    exp_x = np.exp(shifted_x / temperature)
    return exp_x / np.sum(exp_x, axis=-1, keepdims=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    # Check if an image file is provided
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No image selected"}), 400

    # Save image
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Process image
    try:
        # Preprocess image
        image = Image.open(filepath)
        image = image.resize((177, 177))
        image_data = np.array(image).astype(np.float32)
        image_data = np.transpose(image_data, (2, 0, 1))
        image_data = image_data / 255.0

        mean = np.array([0.485, 0.456, 0.406], dtype=np.float32)
        std = np.array([0.229, 0.224, 0.225], dtype=np.float32)
        image_data = (image_data - mean[:, None, None]) / std[:, None, None]
        image_data = image_data[np.newaxis, ...]

        # Run inference
        inputs = {model.get_inputs()[0].name: image_data.astype(np.float32)}
        output = model.run(None, inputs)

        # Process output
        probabilities = softmax_with_temperature(output[0][0])  # No multiplication
        max_index = np.argmax(probabilities)

        # Return response with image URL and output probabilities
        return jsonify({
            "image_url": f"/{UPLOAD_FOLDER}/{file.filename}",
            "probabilities": probabilities.tolist(),
            "predicted_class": int(max_index)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route(f'/{UPLOAD_FOLDER}/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)