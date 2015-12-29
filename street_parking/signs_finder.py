import os
import collections
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

def _find_signs(lat, lng, radius):
    cursor = conn.cursor()
    
    query = 'SELECT latitude, longtitude, signdesc1, from_time, to_time, days from signs WHERE earth_box(ll_to_earth(%s, %s), %s) @> ll_to_earth(latitude, longtitude);'

    cursor.execute(query, (lat, lng, radius))
    columns = ['latitude', 'longtitude', 'signdesc1', 'from_time', 'to_time', 'days']
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
  
    return results

def get_grouped_signs(lat, lng, radius):
    results = _find_signs(lat, lng, radius)
    d = collections.defaultdict(list)
    for item in results:
        d[(item['latitude'], item['longtitude'])].append(item)
        
    return list(d.values())

def get_signs(lat, lng, radius):
    return _find_signs(lat, lng, radius)


