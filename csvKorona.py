import requests
from contextlib import closing
import csv
import datetime
import langDay

url = "https://raw.githubusercontent.com/sledilnik/data/master/csv/stats.csv"

rowDatum = 1
rowOkuzeni = 6
rowSprejetiVBol = 27
rowUmrli = 29
rowOpravljeni = 4


def GetCases():
    csvArray = []

    with closing(requests.get(url, stream=True)) as r:
        f = (line.decode('utf-8') for line in r.iter_lines())
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            vrstica = [row[rowDatum], row[rowOkuzeni], row[rowSprejetiVBol], row[rowOpravljeni], row[rowUmrli]]
            csvArray.append(vrstica)

    datetime_obj = datetime.datetime.strptime(csvArray[-2][0], "%Y-%m-%d")
    weekDay = langDay.GetWeekDay(datetime_obj.strftime("%A"))

    varBolnica = str(abs(int(csvArray[-2][2]) - int(csvArray[-3][2])))
    varUmrli = str(abs(int(csvArray[-2][4]) - int(csvArray[-3][4])))

    msg = "**" + datetime_obj.strftime(weekDay + ", %d. %m %Y") + "**" +\
          "\nOpravljeni testi: " + "**" + csvArray[-2][3] + "**\n"\
          "Potrjeni primeri: " + "**"+csvArray[-2][1]+"**\n"+\
          "Sprejeti v bolnišnico: " + "**" + varBolnica + "**\n"+\
          "Umrli: " + "**" + varUmrli + "**"
    return msg