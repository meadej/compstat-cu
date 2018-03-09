from geocoding_interface import geocoding_interface
import os
import time
import json

def lookup_address(address_string, gi):
    try:
        url = gi.format_address_into_census_query(address_string)
        content = gi.query_census_for_content(url)
        lat_long = gi.get_lat_long_from_census_content(content)
        return lat_long
    except:
        try:
            url = gi.format_address_into_osm_query(address_string)
            content = gi.query_osm_for_content(url)
            lat_long = gi.get_lat_long_from_osm_content(content)
            return lat_long
        except:
            print("No matches found - " + address_string)


address_arr = []
geo_int = geocoding_interface()
data_file = "/crime_db.json"

f_handle = open(data_file)
for line in f_handle.readlines():
    j_line_data = json.loads(line)
    case_number = list(j_line_data.keys())[0]
    lat_lon = lookup_address(j_line_data[case_number]['address'])
    if lat_lon != None:
        j_line_data[case_number]["coordinates"]["lat"] = lat_lon[0]
        j_line_data[case_number]["coordinates"]["lon"] = lat_lon[1]