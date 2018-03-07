import re
import os

def get_file_list(dir_loc):
    return os.listdir(dir_loc)

def read_file(file_location):
    f_handle = open(file_location, 'r')
    return_str = f_handle.read()
    return return_str

def parse_crime_strings_from_file_text(file_text):
    split_array = file_text.split("Date/Time Occured")
    split_array.pop(len(split_array) - 1)
    return split_array

def parse_address_from_crime_string(cr_string):
    second_string = re.split('[0-9]{4}-[0-9]{8}', cr_string)[1]
    address_suffix = re.split('8[0-9]{4}', second_string)[0]
    address_arr = address_suffix.split(" ")
    address = address_arr[3:len(address_arr) - 1]
    return address

absolute_dir = "/home/jon/code/cu-blotter/pdfs/"
files = get_file_list(absolute_dir)
for i in range(0, len(files)):
    files[i] = absolute_dir + files[i]

#Testing purposes
#files = ["/home/jon/code/cu-blotter/pdfs/20180227.txt"]
for filename in files:
    if filename.endswith(".txt"):
        file_content = read_file(filename)
        crime_strings = parse_crime_strings_from_file_text(file_content)
        for cr_string in crime_strings:
            address_arr = parse_address_from_crime_string(cr_string)
            address = " ".join(address_arr)
            if "Boulder" in address:
                print(address)
