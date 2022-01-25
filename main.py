import datetime

import pandas as pd
import time
import _csv
file = open("test.txt","r");


def convert_To_Csv():
    """
        Function for converting txt files to csv.
    """
    read_file = pd.read_csv(r'alert_csv.txt',names=["unix_timestamp","timestamp", "dst_addr","dst_port","src_addr","src_port","proto","gid","sid","msg"], index_col=None)
    read_file["unix_timestamp"] =   read_file["unix_timestamp"].apply(lambda d: datetime.datetime.fromtimestamp(int(d)).strftime('%d/%m/%Y %H:%M'))
    read_file.to_csv(r'./alert.csv')

def change_Csv():
    out = _csv


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
  convert_To_Csv()