from datetime import datetime
from datetime import timedelta
from data_fetcher import data_fetcher

def get_last_sixty_days():
    numdays = 60
    base = datetime.today()
    date_list = [base - timedelta(days=x) for x in range(0, numdays)]
    return date_list

def format_date_string(input_date, format_string):
    return input_date.strftime(format_string)

def main():
    pdf_fetcher = data_fetcher()
    date_list = get_last_sixty_days()
    url_list = []
    for date in date_list:
        url_list.append("https://www.colorado.edu/police/blotter/" + str(format_date_string(date,"%Y%m%d")) + ".pdf")
    pdf_list = pdf_fetcher.get_list_objects(url_list)
    pdf_fetcher.store_objects_locally(pdf_list, "/pdfs/")
    return

main()