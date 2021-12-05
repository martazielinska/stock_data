import os
from urllib.request import urlopen
import glob
import csv
import json


def getdata(folderpath, stock):
    try:
        url = 'https://query1.finance.yahoo.com/v7/finance/download/' + stock + '?period1=1587042293&period2=1618578293&interval=1d&events=history&includeAdjustedClose=true'
        local_path = os.path.join(folderpath, stock + '.csv')
        with urlopen(url) as file, open(local_path, 'wb') as f:
            f.write(file.read())
    except:
        print("The ticket you entered is invalid, please try again.")


def addchangecolumn(folderpath):
    for file_name in glob.glob(folderpath + '*.csv'):
        with open(file_name, mode='r') as csv_filer:
            csv_reader = csv.DictReader(csv_filer)
            headers = []
            dict_list = []
            try:
                for row in csv_reader:
                    change = (float(row["Close"]) - float(row["Open"])) / float(row["Open"])
                    change_dict = {"Change": change}
                    row.update(change_dict)
                    headers = list(row.keys())
                    dict_list.append(row)
            except:
                next(file_name)

        with open(file_name, mode='w', newline='') as csv_filew:
            writer = csv.DictWriter(csv_filew, fieldnames=headers)
            writer.writeheader()

            for data in dict_list:
                writer.writerow(data)


stock_list = ['GOOG', 'FB', 'MSFT', 'AAPL']
folderpath = 'C:/Users/zieli/Downloads/'

for i in stock_list:
    getdata(folderpath, i)

addchangecolumn(folderpath)
