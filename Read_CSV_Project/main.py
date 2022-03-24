import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
print(gray_count)

black_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_count)

cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(cinnamon_count)

data_dict = {
    "Fur Color": ["Grey", "Red", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}

squirrel_color_data = pandas.DataFrame(data_dict)
print(squirrel_color_data)
squirrel_color_data.to_csv("squirrel_count.csv")
