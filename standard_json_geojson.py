import json
import os

def read_standard_json(string):
    j_data = json.loads(string)
    return j_data

def convert_to_geojson(s_json):
    ret_dict = {}
    geo_dict = {}
    prop_dict = {}
    ret_dict['type'] = "Feature"
    case_number = list(s_json.keys())[0]
    geo_dict['type'] = "Point"
    geo_dict['coordinates'] = [s_json[case_number]["coordinates"]["lat"], s_json[case_number]["coordinates"]["lon"]]
    ret_dict['geometry'] = geo_dict
    prop_dict['category'] = s_json[case_number]["category"]
    ret_dict['properties'] = prop_dict
    ret_json = json.dumps(ret_dict)
    return ret_json

def write_geojson_header_to_file(file_location):
    f_handle = open(file_location, 'w')
    opening_json_string = "{\"type\": \"FeatureCollection\",\"features\": ["
    f_handle.write(opening_json_string)
    f_handle.close()

def write_geojson_data_to_file(file_location, data):
    f_handle = open(file_location, 'a')
    f_handle.write(data + "\n")
    f_handle.close()

def write_geojson_closer_to_file(file_location):
    f_handle = open(file_location, 'a')
    closing_json_string = "]}"
    f_handle.write(closing_json_string)
    f_handle.close()

data_file = os.getcwd() + "/crime_db.json"
out_file = os.getcwd() + "/crime_db.geojson"

write_geojson_header_to_file(out_file)

for line in open(data_file).readlines():
    j_data = read_standard_json(line)
    ret_data = convert_to_geojson(j_data)
    write_geojson_data_to_file(ret_data)

write_geojson_closer_to_file(out_file)

