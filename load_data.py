import requests
from datastore import db
from datastore.models import ParkingSlot


def new_parking_slot(pos_lat, pos_long, extra_info):
        parking_slot = ParkingSlot(pos_lat=pos_lat,
                                   pos_long=pos_long,
                                   extra_info=extra_info)
        db.session.add(parking_slot)
        db.session.commit()
        return parking_slot


def parse_caceres():
    url = 'http://opendata.caceres.es/GetData/GetData?dataset=om:PlazaMovilidadReducida&format=json'
    response = requests.get(url)
    json_data = response.json()
    for entry in json_data['results']['bindings']:
        pos_lat = entry['geo_lat']['value']
        pos_long = entry['geo_long']['value']
        extra_info = entry['rdfs_label']['value']
        new_parking_slot(pos_lat=pos_lat,
                         pos_long=pos_long,
                         extra_info=extra_info)



'''
http://www.plumislandmedia.net/mysql/haversine-mysql-nearest-loc/

SELECT id, pos_lat, pos_long,
      111.045* DEGREES(ACOS(COS(RADIANS(latpoint))
                 * COS(RADIANS(pos_lat))
                 * COS(RADIANS(longpoint) - RADIANS(pos_long))
                 + SIN(RADIANS(latpoint))
                 * SIN(RADIANS(pos_lat)))) AS distance_in_km
 FROM parking_slot
 JOIN (
     SELECT  39.472  AS latpoint,  -6.40567 AS longpoint
   ) AS p ON 1=1
 ORDER BY distance_in_km
 LIMIT 15;
'''
