import requests

class data_fetcher:
    def store_object_locally(self, object, local_destination):
        try:
            outputWriter = open(local_destination)
            outputWriter.write(object)
            outputWriter.close()
        except:
            raise IOError("Unable to write object to " + str(local_destination))

    def get_object_from_url(self, url):
        try:
            object = requests.get(str(url))
            return object
        except:
            raise IOError("Unable to fetch object at " + str(url))