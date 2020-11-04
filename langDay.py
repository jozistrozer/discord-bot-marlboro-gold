def GetWeekDay(day):
    switch = {
        "Monday": "Ponedeljek",
        "Tuesday": "Torek",
        "Wednesday": "Sreda",
        "Thursday": "Četrtek",
        "Friday": "Petek",
        "Saturday": "Sobota",
        "Sunday": "Nedelja",
    }

    return switch.get(day, "Error")
