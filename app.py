from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Aapka Token securely yahan add kar diya hai
OPEN_CELL_ID_KEY = "pk.00538f0bc13fda302d8b0338c8d65382"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trace', methods=['GET'])
def trace():
    mcc = request.args.get('mcc')
    mnc = request.args.get('mnc')
    lac = request.args.get('lac')
    cellid = request.args.get('cellid')
    
    url = f"https://opencellid.org/cell/get?key={OPEN_CELL_ID_KEY}&mcc={mcc}&mnc={mnc}&lac={lac}&cellid={cellid}&format=json"
    
    try:
        response = requests.get(url).json()
        return jsonify(response)
    except:
        return jsonify({"status": "error", "message": "Failed to connect to tower database"})

if __name__ == '__main__':
    app.run()
