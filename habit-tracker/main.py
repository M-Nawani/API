import requests
from datetime import datetime

USERNAME = "mnawani"
TOKEN = "djejoewr4nijsmkjsowo"
GRAPH_ID = "test-graph"

pixela_url_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url= pixela_url_endpoint, json= user_parameters)
# print(response.text)

create_graph_url = f"{pixela_url_endpoint}/{USERNAME}/graphs"
headers = {"X-USER-TOKEN": f"{TOKEN}"}

graph_parameters = {
    "id": GRAPH_ID,
    "name": "myfisrtgraph",
    "unit": "commit",
    "type": "int",
    "color": "shibafu"

}

# response = requests.post(url=create_graph_url, headers=headers, json=graph_parameters)
# print(response.text)

get_graph_endpoint = f"{pixela_url_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/graph-def"
# response = requests.get(url=get_graph_endpoint, headers=headers).json()
# print(response)

today = datetime.now()
pixel_creation_endpoint = f"{pixela_url_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many rounds did you do today ? ")}

response = requests.post(url=pixel_creation_endpoint, headers=headers, json=pixel_data)
print(response.text)
