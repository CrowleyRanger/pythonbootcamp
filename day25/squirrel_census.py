import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# squirrel_colors = data["Primary Fur Color"].tolist()
grays = len(data[data["Primary Fur Color"] == "Gray"])
cinnamons = len(data[data["Primary Fur Color"] == "Cinnamon"])
blacks = len(data[data["Primary Fur Color"] == "Black"])
# print(f"Grays: {grays}")
# print(f"Cinnamons: {cinnamons}")
# print(f"Blacks: {blacks}")

dict = {
    "Fur Color": ["Gray", "Cinnamons", "Black" ],
    "Quantity": [grays, cinnamons, blacks]
}

pd.DataFrame(dict).to_csv("squirrel_count.csv")
squirel_data = pd.read_csv("squirrel_count.csv")
print(squirel_data)

# for squirrel_color in squirrel_colors:
#     if squirrel_color == "gray":
#         gray += 1
#     elif squirrel_color == "cinammon":
#         cinammons += 1
#     elif squirrel_color == "black":
#         blacks += 1

# print(f"Grays: {grays}")
# print(f"Cinammons: {cinammons}")
# print(f"Grays: {grays}")