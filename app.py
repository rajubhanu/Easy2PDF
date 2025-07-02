
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "EasyPDF Backend Running with 10 Tools"

@app.route('/pdf-to-word', methods=['POST'])
def pdf_to_word():
    return jsonify({"message": "PDF to Word tool working"})

@app.route('/word-to-pdf', methods=['POST'])
def word_to_pdf():
    return jsonify({"message": "Word to PDF tool working"})

@app.route('/merge-pdf', methods=['POST'])
def merge_pdf():
    return jsonify({"message": "Merge PDF tool working"})

@app.route('/split-pdf', methods=['POST'])
def split_pdf():
    return jsonify({"message": "Split PDF tool working"})

@app.route('/compress-pdf', methods=['POST'])
def compress_pdf():
    return jsonify({"message": "Compress PDF tool working"})

@app.route('/pdf-to-image', methods=['POST'])
def pdf_to_image():
    return jsonify({"message": "PDF to Image tool working"})

@app.route('/image-to-pdf', methods=['POST'])
def image_to_pdf():
    return jsonify({"message": "Image to PDF tool working"})

@app.route('/rotate-pdf', methods=['POST'])
def rotate_pdf():
    return jsonify({"message": "Rotate PDF tool working"})

@app.route('/unlock-pdf', methods=['POST'])
def unlock_pdf():
    return jsonify({"message": "Unlock PDF tool working"})

@app.route('/protect-pdf', methods=['POST'])
def protect_pdf():
    return jsonify({"message": "Protect PDF tool working"})
