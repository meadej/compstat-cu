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

    def get_list_objects(self, url_list):
        return_array = []
        try:
            for url in url_list:
                return_array.append(self.get_object_from_url(url))
        except:
            raise Exception("Failed to get objects in list")
        return return_array

    def store_objects_locally(self, object_list, local_destination):
        for object in object_list:
            self.store_object_locally(object, local_destination)