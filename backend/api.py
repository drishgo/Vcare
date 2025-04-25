from flask import Flask, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 
@app.route('/api/usage')
def get_usage():
    try:
        with open("usage_data.json" , "r") as f:
            usage_data = json.load(f)
        return jsonify(usage_data)
    except exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)

