# import csv

# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1].isdigit():
#             temperatures.append(row[1])
#         print(row)
#         print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)

temp_list = data["temp"].tolist()
print("Max temperature:", data["temp"].max())
print(data["day"][data.temp == data["temp"].max()])