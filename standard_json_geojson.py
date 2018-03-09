import json
import os

def read_standard_json(string):
    j_data = json.loads(string)
    return j_data

def convert_to_geojson(s_json):
    ret_dict = {}
    geo_dict = {}
    prop_dict = {}
    ret_dict["type"] = "Feature"
    case_number = list(s_json.keys())[0]
    geo_dict["type"] = "Point"
    geo_dict["coordinates"] = [s_json[case_number]["coordinates"]["lat"], s_json[case_number]["coordinates"]["lon"]]
    ret_dict["geometry"] = geo_dict
    prop_dict["category"] = s_json[case_number]["category"]
    ret_dict["properties"] = prop_dict
    ret_json = json.dumps(ret_dict)
    return ret_json

def write_geojson_header_to_file(file_location):
    f_handle = open(file_location, 'w')
    opening_json_string = "{\"type\": \"FeatureCollection\",\"features\": [\n"
    f_handle.write(opening_json_string)
    f_handle.close()

def write_geojson_data_to_file(file_location, data):
    f_handle = open(file_location, 'a')
    f_handle.write(data + ",\n")
    f_handle.close()

def write_geojson_closer_to_file(file_location):
    r_handle = open(file_location, 'r')
    f_content = r_handle.read()
    f_content = f_content.strip().strip(",")
    r_handle.close()
    f_handle = open(file_location, 'w')
    closing_json_string = "]}"
    f_handle.write(f_content)
    f_handle.write(closing_json_string)
    f_handle.close()

data_file = os.getcwd() + "/full_crime_db.json"
out_file = os.getcwd() + "/crime_db.geojson"

data_handle = open(data_file)

write_geojson_header_to_file(out_file)

for line in data_handle.readlines():
    j_data = read_standard_json(line)
    ret_data = convert_to_geojson(j_data)
    write_geojson_data_to_file(out_file, ret_data)

write_geojson_closer_to_file(out_file)
data_handle.close()
