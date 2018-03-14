from geocoding_interface import geocoding_interface
import os
import time
import json
import sys

def lookup_address(address_string, gi):
    try:
        url = gi.format_address_into_census_query(address_string)
        content = gi.query_census_for_content(url)
        lat_long = gi.get_lat_long_from_census_content(content)
        return lat_long
    except:
        try:
            time.sleep(1)
            url = gi.format_address_into_osm_query(address_string)
            content = gi.query_osm_for_content(url)
            lat_long = gi.get_lat_long_from_osm_content(content)
            return lat_long
        except:
            return None

if len(sys.argv) < 3:
    print("Usage: python lookup_addresses.py [input file] [output file]")
    exit(1)

address_arr = []
geo_int = geocoding_interface()
data_file = sys.argv[1]
out_file = sys.argv[2]

f_handle = open(os.getcwd() + "/" + data_file, 'r')
o_handle = open(os.getcwd() + "/" + out_file, 'w')

for line in f_handle.readlines():
    j_line_data = json.loads(line)
    case_number = list(j_line_data.keys())[0]
    lat_lon = lookup_address(j_line_data[case_number]['address'], geo_int)
    if lat_lon != None:
        j_line_data[case_number]["coordinates"] = {}
        j_line_data[case_number]["coordinates"]["lat"] = float(lat_lon[0])
        j_line_data[case_number]["coordinates"]["lon"] = float(lat_lon[1])
        j_return_data = json.dumps(j_line_data)
        o_handle.write(j_return_data + "\n")

f_handle.close()
o_handle.close()
