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
    geo_dict['coordinates'] = [s_json[case_number]["coordinates"]["lon"], s_json[case_number]["coordinates"]["lat"]]
    ret_dict['geometry'] = geo_dict
    prop_dict['category'] = s_json[case_number]["category"]
    ret_dict['properties'] = prop_dict
    ret_json = json.dumps(ret_dict)
    return ret_json

data_file = "/crime_db.json"
for line in open(os.getcwd() + data_file).readlines():
    j_data = read_standard_json(line)
    ret_data = convert_to_geojson(j_data)
    print(ret_data)
