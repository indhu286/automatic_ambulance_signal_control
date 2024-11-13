from flask import Flask, request, jsonify
import your_model_file  # Replace with the actual file name containing detect_ambulance

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'})

    # Save the file temporarily
    file_path = "temporary_path/" + file.filename
    file.save(file_path)
    
    # Run the model inference
    result = your_model_file.detect_ambulance(file_path)  # Should return "Yes" or "No"

    # Send the detection result back to the frontend
    return jsonify({'detected': result})

if __name__ == '__main__':
    app.run(debug=True)
