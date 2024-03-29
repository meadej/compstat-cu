import requests
import urllib.parse
import json

class geocoding_interface():
    def __init__(self):
        return

    def handle_exception(self, ex, method_name):
        """
        #Debugging stuff below
        print(type(ex))
        print(ex)
        print(method_name)
        """
        raise Exception

    def format_address_url_safe(self, address):
        try:
            return urllib.parse.quote_plus(address)
        except Exception as ex:
            self.handle_exception(ex, "format_address_url_safe")

    def format_address_into_census_query(self, address):
        address = self.format_address_url_safe(address)
        prefix = "https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?address="
        suffix = "&benchmark=9&format=json"
        return prefix + address + suffix

    def format_address_into_osm_query(self, address):
        address = self.format_address_url_safe(address)
        prefix = "https://nominatim.openstreetmap.org/search?q="
        suffix = "&format=json"
        return prefix + address + suffix

    def query_census_for_content(self, url):
        try:
            census_return = requests.get(url)
            return census_return.content.decode('utf-8')
        except Exception as ex:
            self.handle_exception(ex, "query_census_for_content")

    def query_osm_for_content(self, url):
        try:
            osm_return = requests.get(url)
            return osm_return.content.decode('utf-8')
        except Exception as ex:
            self.handle_exception(ex, "query_osm_for_content")


    def get_lat_long_from_census_content(self, content):
        j_data = json.loads(content)
        try:
            lon = j_data['result']['addressMatches'][0]['coordinates']['x']
            lat = j_data['result']['addressMatches'][0]['coordinates']['y']
            return (lat, lon)
        except Exception as ex:
            self.handle_exception(ex, "get_lat_long_from_census_content")

    def get_lat_long_from_osm_content(self, content):
        j_data = json.loads(content)
        try:
            lat = j_data[0]['lat']
            lon = j_data[0]['lon']
            return (lat, lon)
        except Exception as ex:
            self.handle_exception(ex, "get_lat_long_from_osm_content")


