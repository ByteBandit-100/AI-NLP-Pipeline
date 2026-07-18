from flask import Flask, request, jsonify
import sys
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")

sys.path.insert(0, SRC_DIR)

from predict import predict_attributes
app = Flask(__name__)


@app.route("/")
def home():
    return {
        "message": "Product Attribute Extraction API",
        "endpoint": "/extract"
    }
@app.route("/extract", methods=["POST"])
def extract():
    try:
        data = request.get_json(silent=True)

        if data is None:
            return jsonify({
                "error": "Invalid JSON format"
            }), 400

        if "description" not in data:
            return jsonify({
                "error": "description field is required"
            }), 400

        prediction = predict_attributes(data["description"])

        return jsonify(prediction), 200

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500
    
if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)
