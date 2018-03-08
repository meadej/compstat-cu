import re
import os
import json

def get_file_list(dir_loc):
    return os.listdir(dir_loc)

def read_file(file_location):
    f_handle = open(file_location, 'r')
    return_str = f_handle.read()
    return return_str

def parse_crime_strings_from_file_text(file_text):
    case_array = re.findall('[0-9]{4}-[0-9]{8}', file_text)
    split_array = re.split('[0-9]{4}-[0-9]{8}', file_text)
    split_array.pop(0)
    for i in range(0, len(split_array)):
        split_array[i] = case_array[i] + " " + split_array[i]
    return split_array

def parse_date_time_occured_from_crime_string(cr_string):
    return re.findall('[0-9]{2}/[0-9]{2}/[0-9]{4} [0-9]{2}:[0-9]{2} - [0-9]{2}/[0-9]{2}/[0-9]{4} [0-9]{2}:[0-9]{2}', cr_string)[0]

def parse_case_number_from_crime_string(cr_string):
    return re.findall('[0-9]{4}-[0-9]{8}', cr_string)[0]

def parse_address_from_crime_string(cr_string):
    address_suffix = re.split('8[0-9]{4}', cr_string)[0]
    address_arr = address_suffix.split(" ")
    address = " ".join(address_arr[4:len(address_arr) - 1])
    return address

def parse_type_from_crime_string(cr_string):
    cr_type = re.findall('8[0-9]{4} ([A-Z]{1}[a-z]*)', cr_string)[0]
    return cr_type

absolute_dir = "/home/jon/code/cu-blotter/pdfs/"
#Testing purposes
#absolute_dir = "C:/Users/Jon/Documents/GitHub/cu-blotter/pdfs/"
files = get_file_list(absolute_dir)
for i in range(0, len(files)):
    files[i] = absolute_dir + files[i]

#Testing purposes
#files = [absolute_dir + "20180227.txt"]
for filename in files:
    if filename.endswith(".txt"):
        file_content = read_file(filename)
        crime_strings = parse_crime_strings_from_file_text(file_content)
        for cr_string in crime_strings:
            address = parse_address_from_crime_string(cr_string)
            if "Boulder" in address:
                case_num = parse_case_number_from_crime_string(cr_string)
                date = parse_date_time_occured_from_crime_string(cr_string)
                category = parse_type_from_crime_string(cr_string)
                case_dict = {
                    case_num:{
                        "date":date,
                        "address":address,
                        "category":category
                    }
                }
            j_data = json.dumps(case_dict)
            print(j_data)