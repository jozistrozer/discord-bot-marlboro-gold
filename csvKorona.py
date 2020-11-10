import requests
from contextlib import closing
import csv
import datetime
from datetime import date
import langDay

url = "https://raw.githubusercontent.com/sledilnik/data/master/csv/stats.csv"

rowDatum = 1
rowOkuzeni = 6
rowSprejetiVBol = 27
rowUmrli = 29
rowOpravljeni = 4


def GetCases(arg=None):
    global rowDan
    csvArray = []
    rowDan = -2

    # Branje CSV
    with closing(requests.get(url, stream=True)) as r:
        count = 0
        f = (line.decode('utf-8') for line in r.iter_lines())
        reader = csv.reader(f, delimiter=',', quotechar='"')
        for row in reader:
            vrstica = [row[rowDatum], row[rowOkuzeni], row[rowSprejetiVBol], row[rowOpravljeni], row[rowUmrli], count]
            csvArray.append(vrstica)
            count += 1

    # Računanje dneva & obdelovanje argumenta

    if arg is not None:
        dFormatArg = "%d.%m.%Y"
        dFormatCSV = "%Y-%m-%d"
        dTarget = datetime.datetime.strptime(arg, dFormatArg)
        dStart = datetime.datetime.strptime(csvArray[-2][0], dFormatCSV)
        indexTarget = csvArray[-2][5] - (dStart - dTarget).days
        rowDan = indexTarget
    # Izvleček podatkov & računanje
    try:
        datetime_obj = datetime.datetime.strptime(csvArray[rowDan][0], "%Y-%m-%d")
        varWeekDay = langDay.GetWeekDay(datetime_obj.strftime("%A"))
        varBolnica = str(abs(int(csvArray[rowDan][2]) - int(csvArray[rowDan-1][2])))
        varUmrli = str(abs(int(csvArray[rowDan][4]) - int(csvArray[rowDan-1][4])))
        varOpravljeniTesti = csvArray[rowDan][3]
        varPotrjeni = csvArray[rowDan][1]
        # Oblikovanje sporočila
        msg = "**" + datetime_obj.strftime(varWeekDay + ", %d. %m. %Y") + "**" + \
              "\nOpravljeni testi: " + "**" + varOpravljeniTesti + "**\n" \
                                                                   "Potrjeni primeri: " + "**" + varPotrjeni + "**\n" + \
              "Sprejeti v bolnišnico: " + "**" + varBolnica + "**\n" + \
              "Umrli: " + "**" + varUmrli + "**"
    except IndexError:
        msg = "Nimam podatke ob podanem datumu."

    return msg
