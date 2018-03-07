import urllib.parse
import requests
import json
import time

def format_query(address_string):
    pre = "https://nominatim.openstreetmap.org/search?q="
    post = "&format=json"
    converted_address = urllib.parse.quote_plus(address_string)
    return str(pre) + str(converted_address) + str(post)

def perform_query(address_string):
    req = format_query(address_string)
    census_return = requests.get(req)
    return_content = census_return.content
    return_content_str = return_content.decode('utf-8')
    return_code = census_return.status_code
    if return_code != 200:
        print("Service unreachable")
        return 0
    if len(return_content_str) == 0:
        print("Unable to retreive data for " + address_string)
        return 0
    return return_content_str

def parse_query_return(return_content):
    j_data = json.loads(return_content)
    if len(j_data) < 1:
        return 0
    lat = j_data[0]['lat']
    lon = j_data[0]['lon']
    return (lat, lon)

def read_addresses_from_file(file_location):
    file_handle = open(file_location, 'r')
    for line in file_handle.readlines():
        address = line.strip()
        try:
            q_return = perform_query(address)
            q_parse = parse_query_return(q_return)
            if q_parse != 0:
                print(q_parse)
            if q_parse == 0:
                print("Unable to find address " + address)
            time.sleep(1)
        except:
            print("Exception occured for address " + address)

read_addresses_from_file("/home/jon/code/cu-blotter/address_db.txt")
