from geocoding_interface import geocoding_interface
import os
import time
import json

def read_addresses_from_file(file_location, address_arr):
    file_handle = open(file_location, 'r')
    for line in file_handle.readlines():
        j_data = json.loads(line.strip())
        case_num = list(j_data.keys())[0]
        address = j_data[case_num]["address"]
        address_arr.append(address)

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
read_addresses_from_file(os.getcwd() + data_file, address_arr)

for address in address_arr:
    time.sleep(1)
    ll = lookup_address(address, geo_int)
    j_styled_data = {"lon":ll[0], "lat":ll[1]}
    j_data = json.dumps(j_styled_data)
    if (ll != None):
        print(j_data)
