import requests
from models import ParkingSlot


def parse_caceres():
    url = 'http://opendata.caceres.es/GetData/GetData?dataset=om:PlazaMovilidadReducida&format=json'
    response = requests.get(url)
    json_data = response.json()
    for entry in json_data['results']['bindings']:
        pos_lat = entry['geo_lat']['value']
        pos_lon = entry['geo_long']['value']
        extra_info = entry['rdfs_label']['value']
        parking_slot = ParkingSlot(pos_lat=pos_lat,
                                   pos_lon=pos_lon,
                                   extra_info=extra_info)
        parking_slot.save()

parse_caceres()