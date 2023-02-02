import requests
from datetime import datetime

USERNAME = "xpaceranger"
TOKEN = "dv84n5gknbv4314p698u"
GRAPH = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }

# response = requests.post(url=pixela_endpoint, json=user_params)

# graph_endpoint = "https://pixe.la/v1/users/xpaceranger/graphs"

headers = {
    "X-USER-TOKEN": TOKEN
}

# parameters = {
#     "id": "graph1",
#     "name": "Habit Tracker",
#     "unit": "day",
#     "type": "int",
#     "color": "kuro"
# }

# response = requests.post(url=graph_endpoint, headers=headers, json=parameters)

# pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}"

#yyyyMMdd
now = datetime.now().strftime(r"%Y%m%d")

# post_params = {
#     "date": now,
#     "quantity": "2"
# }

# response = requests.post(url=pixel_creation_endpoint, headers=headers, json=post_params)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH}/{now}"

new_pixel_data = {
    "quantity": "4"
}

response = requests.put(url=update_endpoint, headers=headers, json=new_pixel_data)
print(response.text)

# print(response.text)