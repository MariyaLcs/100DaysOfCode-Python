import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

#data_dict = data.to_dict()
# print(data_dict)

#temp_list = data["temp"].to_list()
#print(temp_list)

# average_temp = sum(temp_list)/len(temp_list)
# print(average_temp)

#***Same

#print(data["temp"].mean())
#print(data["temp"].max())

#***Get Data in Columns
#print(data["condition"])
#print(data.condition)

#***Get Data in Row
#print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp_F = int(monday.temp)*9/5+32
# print(monday_temp_F)

#***Create a Dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")