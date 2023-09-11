import requests

response = requests.get("http://api.open-notify.org/astros.json")
json = response.json()

print("The people currently in space are:")
for person in json["people"]:
    print(person["name"])

print("There are", json["number"], "people in space right now.")
