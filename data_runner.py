from datetime import datetime
from datetime import timedelta
from data_fetcher import data_fetcher

def get_last_n_days(n):
    numdays = n
    base = datetime.today()
    date_list = [base - timedelta(days=x) for x in range(0, numdays - 1)]
    return date_list

def format_date_string(input_date, format_string):
    return input_date.strftime(format_string)

def main():
    pdf_fetcher = data_fetcher()
    date_list = get_last_n_days(50)
    url_list = []
    formatted_date_list = []
    for date in date_list:
        formatted_date_list.append(format_date_string(date, "%Y%m%d"))
        url_list.append("https://www.colorado.edu/police/blotter/" + str(format_date_string(date,"%Y%m%d")) + ".pdf")
    pdf_list = pdf_fetcher.get_list_objects(url_list)
    title_list = []
    for i in range(0, len(date_list)):
        title_list.append(str(formatted_date_list[i]) + ".pdf")
    pdf_fetcher.store_objects_locally(title_list, pdf_list, "/home/jon/code/cu-blotter/pdfs/")
    return

main()
