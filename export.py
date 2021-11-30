import csv
import matplotlib.pyplot as plt

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    counter = 0
    data = []
    daily_total = 0
    days = []
    for row in reader:
        daily_total += float(row[9]) # 8th field (9 in array, since arrays are 0 based) is the solar power field.
        counter += 1
        if counter % 24 == 0:
            data.append(daily_total)
            daily_total = 0
            days.append(row[0]) #first field is the day in DD/MM/YYYY format
    avg  = []
    day_tot = 0
    for day in data:
        day_tot += day
        avg.append(day_tot / 7)
        day_tot = 0
    plt.plot(days,avg) # plot by days in x axis and averages in y axis
    plt.xlabel("Day")
    plt.ylabel("MWh")
    plt.title("Daily Average of Generated Solar Energy in Turkey in 2020.")
    plt.show()
# data.csv is exported from https://seffaflik.epias.com.tr/transparency/uretim/gerceklesen-uretim/gercek-zamanli-uretim.xhtml