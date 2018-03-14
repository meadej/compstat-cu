import sys
import json
import os
from datetime import datetime

if len(sys.argv) < 4:
    print("Usage: python format_json_SQL.py [input file] [table name] [output file]")
    exit(1)

input_filename = sys.argv[1]
table_name = sys.argv[2]
output_filename = sys.argv[3]

input_handle = open(os.getcwd() + "/" + input_filename, 'r')
output_handle = open(os.getcwd() + "/" + output_filename, 'w')

for line in input_handle.readlines():
    j_data = json.loads(line.strip())
    case_number = str(list(j_data.keys())[0])
    SQL_statement = "INSERT INTO " + table_name + " VALUES ("
    SQL_statement = SQL_statement + "\"" + case_number + "\""
    dt_obj = datetime.strptime(j_data[case_number]["date"].split("-")[1].strip(), "%m/%d/%Y %H:%M")
    dt_ret = datetime.strftime(dt_obj, "%Y-%m-%d %H:%M:%S")
    SQL_statement = SQL_statement + ",\"" + dt_ret + "\""
    SQL_statement = SQL_statement + ",\"" + j_data[case_number]["category"] + "\""
    SQL_statement = SQL_statement + ",\"" + j_data[case_number]["address"] + "\""
    SQL_statement = SQL_statement + "," + str(j_data[case_number]["coordinates"]["lat"])
    SQL_statement = SQL_statement + "," + str(j_data[case_number]["coordinates"]["lon"])
    SQL_statement = SQL_statement + ");\n"
    output_handle.write(SQL_statement)

input_handle.close()
output_handle.close()
