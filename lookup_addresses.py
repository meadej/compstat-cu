from geocoding_interface import geocoding_interface as gi

def read_addresses_from_file(file_location, address_arr):
    file_handle = open(file_location, 'r')
    for line in file_handle.readlines():
        address = line.strip()
        address_arr.append(address)

def lookup_address(address_string):
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
            print("No matches found")


address_arr = []
read_addresses_from_file("/home/jon/code/cu-blotter/address_db.txt", address_arr)

for address in address_arr:
    lat_long = lookup_address(address)
    print(lat_long)
    lat_long = lookup_address(address)
