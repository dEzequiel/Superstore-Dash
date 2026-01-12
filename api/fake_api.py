from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

def load_targets():
    targets_path = os.path.join(os.path.dirname(__file__), 'targets.json')
    with open(targets_path, 'r') as f:
        return json.load(f)

@app.route('/api/targets', methods=['GET'])
def get_all_targets():
    data = load_targets()
    return jsonify(data)

@app.route('/api/targets/<region>', methods=['GET'])
def get_targets_by_region(region):
    data = load_targets()
    filtered = [t for t in data['sales_targets'] if t['region_code'] == region.upper()]
    return jsonify({
        'sales_targets': filtered,
        'metadata': data['metadata']
    })

@app.route('/api/targets/year/<int:year>', methods=['GET'])
def get_targets_by_year(year):
    data = load_targets()
    filtered = [t for t in data['sales_targets'] if t['fiscal_year'] == year]
    return jsonify({
        'sales_targets': filtered,
        'metadata': data['metadata']
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok', 'service': 'targets-api'})

if __name__ == '__main__':
    print("Starting Targets API on http://localhost:5000")
    print("Endpoints:")
    print("  GET /api/targets - All targets")
    print("  GET /api/targets/<region> - Targets by region (US, APAC, EU, etc.)")
    print("  GET /api/targets/year/<year> - Targets by year (2011-2014)")
    print("  GET /api/health - Health check")
    app.run(debug=True, port=5000)

