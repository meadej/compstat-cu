import sys
import os

if len(sys.argv) < 3:
    print("Usage: python make_geojson_web_ready.py [input file] [output file]")

input_name = sys.argv[1]
output_name = sys.argv[2]

input_file = os.getcwd() + "/" + input_name
output_file = os.getcwd() + "/" + output_name

in_handle = open(input_file, 'r')
out_handle = open(output_file, 'w')

data = in_handle.read()
data = "var data = " + data
out_handle.write(data)

in_handle.close()
out_handle.close()
