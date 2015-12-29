import os
from flask import Flask, request, Response
import json

from street_parking.signs_finder import get_signs
app = Flask(__name__)

@app.route('/find')
def find():
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    radius = request.args.get('radius')

    results = get_signs(lat, lng, radius)
    json_string = json.dumps({'results':results})

    resp = Response(response=json_string,
            status=200,
            mimetype="application/json")

    return resp

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
