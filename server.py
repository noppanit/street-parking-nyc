import os
from flask import Flask, request
import psycopg2
import json

app = Flask(__name__)

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL)

@app.route('/find')
def find():
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    radius = request.args.get('radius')
    cursor = conn.cursor()
    
    query = 'SELECT * from signs WHERE earth_box(ll_to_earth(%s, %s), %s) @> ll_to_earth(latitude, longtitude);'

    cursor.execute(query, (lat, lng, radius))
    columns = ['longtitude', 'latitude', 'object_id', 'sg_key_bor', 'sg_order_n', 'sg_seqno_n', 'sg_mutcd_c', 'sr_dist', 'sg_sign_fc', 'sg_arrow_d', 'x', 'y', 'signdesc']
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))

    return json.dumps({'results':results})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
