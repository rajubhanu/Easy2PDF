
from flask import Flask, request, send_file
from flask_cors import CORS
import os
import tempfile

from tools import (
    pdf_to_word, word_to_pdf, merge_pdf, split_pdf, compress_pdf,
    pdf_to_image, image_to_pdf, rotate_pdf, unlock_pdf, protect_pdf
)

app = Flask(__name__)
CORS(app)

TOOL_MAP = {
    "pdf-to-word": pdf_to_word.convert,
    "word-to-pdf": word_to_pdf.convert,
    "merge-pdf": merge_pdf.convert,
    "split-pdf": split_pdf.convert,
    "compress-pdf": compress_pdf.convert,
    "pdf-to-image": pdf_to_image.convert,
    "image-to-pdf": image_to_pdf.convert,
    "rotate-pdf": rotate_pdf.convert,
    "unlock-pdf": unlock_pdf.convert,
    "protect-pdf": protect_pdf.convert
}

@app.route("/<tool>", methods=["POST"])
def convert_tool(tool):
    if tool not in TOOL_MAP:
        return {"error": "Invalid tool"}, 400

    if "file" not in request.files:
        return {"error": "No file uploaded"}, 400

    uploaded_file = request.files["file"]
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        uploaded_file.save(temp.name)
        output_path = TOOL_MAP[tool](temp.name)

    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
