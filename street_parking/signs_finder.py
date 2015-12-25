import os

import psycopg2

from urllib.parse import urlparse

url = urlparse(os.environ["DATABASE_URL"])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

def get_signs(lat, lng, radius):
    cursor = conn.cursor()
    
    query = 'SELECT latitude, longtitude, signdesc1, from_time, to_time, days from signs WHERE earth_box(ll_to_earth(%s, %s), %s) @> ll_to_earth(latitude, longtitude);'

    cursor.execute(query, (lat, lng, radius))
    columns = ['latitude', 'longtitude', 'signdesc1', 'from_time', 'to_time', 'days']
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    
    print(results[0])
    return results


