import requests
from datetime import datetime

pixela_endpoint="https://pixe.la/v1/users"
USER_NAME="aloysiousmichael"
TOKEN="hjk12uyu73bspd99"
GRAPH_ID="graph2"

use_params={
    "token" : "hjk12uyu73bspd99",
    "username" : "aloysiousmichael",
    "agreeTermsOfService" : "yes",
    "notMinor":"yes",
}

#AUTHENTICATION
# response=requests.post(url=pixela_endpoint,json=use_params)
# print(response.text)

graph_endpoint=f"{pixela_endpoint}/{USER_NAME}/graphs"


graph_config={
    "id":GRAPH_ID,
    "name":"Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color":"ajisai",
}

headers={
    "X-USER-TOKEN" :TOKEN
}


pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today=datetime.now()
pixel_data={
    "date": today.strftime("%Y%m%d"),
    "quantity":input("How many hours did u studied today ?.")
}

response=requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)

#TO UPDATE DATA
# update_endpoint=f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response=requests.put(url=delete_endpoint,headers=headers)

#TO DELETE DATA
# delete_endpoint=f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response=requests.delete(url=delete_endpoint,headers=headers)


print(response.text)

