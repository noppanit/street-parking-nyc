import os
import collections
import psycopg2

from dateutil.parser import parse

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
  
    street_signs = []
    for r in results:
        days = []
        if r['days']:        
            days = r['days'].split(',')
            days = list(filter(None, days))
            days = [d.strip() for d in days]
            
        street_sign = {
                'parkable': {
                    'isParkable': None,
                    'parkableDays': {
                        'days': days,
                        'from_time': r['from_time'],
                        'to_time': r['to_time']
                        }
                    },
                'description': r['signdesc1'],
                'longtitude': r['longtitude'],
                'latitude': r['latitude']
                }
        street_signs.append(street_sign)
    return street_signs

def get_grouped_signs(lat, lng, radius):
    results = _find_signs(lat, lng, radius)
    d = collections.defaultdict(list)
    for item in results:
        d[(item['latitude'], item['longtitude'])].append(item)
        
    return list(d.values())

def get_signs(lat, lng, radius):
    return _find_signs(lat, lng, radius)


