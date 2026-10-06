import json
import os

#function to load the data
def load_data(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, filename)
    with open(path, "r") as f:
        return json.load(f)

data = load_data("data.json")


data = load_data("data.json")

#funcion to display the data    
def display_users(data):
    print("users and their connections")
    for user in data["users"]:
        print(f"{user['name']} ({user['id']}) - friends : {user['friends'] }- liked_pages{user['liked_pages']}")

    print("\nPages and information\n")
    for page in data["pages"]:
        print(f"{page['id']}: {page['name']}")

display_users(data)        


