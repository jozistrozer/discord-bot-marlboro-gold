import requests
from contextlib import closing
import csv
import datetime
import langDay

url = "https://raw.githubusercontent.com/sledilnik/data/master/csv/stats.csv"

rowDatum = 1
rowOkuzeni = 6

csvArray = []

with closing(requests.get(url, stream=True)) as r:

    f = (line.decode('utf-8') for line in r.iter_lines())
    reader = csv.reader(f, delimiter=',', quotechar='"')

    for row in reader:
        vrstica = [row[rowDatum], row[rowOkuzeni]]
        csvArray.append(vrstica)


def GetCases():
    datetime_obj = datetime.datetime.strptime(csvArray[-2][0], "%Y-%m-%d")
    weekDay = langDay.GetWeekDay(datetime_obj.strftime("%A"))
    return datetime_obj.strftime("%d.%m.%Y (" + weekDay + ")") + ": " + "{:,} potrjenih primerov oseb okuženih z COVID-19".format(int(csvArray[-2][1]))