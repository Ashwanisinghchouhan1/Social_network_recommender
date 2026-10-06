# Here we are cleaning the data
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def clean_data(data):
    # remove users with blank names
    data["users"] = [user for user in data["users"] if user['name'].strip()]

    # remove duplicate friends
    for user in data["users"]:
        user["friends"] = list(set(user["friends"]))

    # remove inactive users (no friends and no liked pages)
    data["users"] = [
        user for user in data["users"]
        if user["friends"] or user["liked_pages"]
    ]

    # remove duplicate pages
    unique_pages = {}
    for page in data["pages"]:
        unique_pages[page['id']] = page

    data["pages"] = list(unique_pages.values())
    return data

# load, clean and save data
input_path = os.path.join(BASE_DIR, "data2.json")
output_path = os.path.join(BASE_DIR, "clean_data.json")

with open(input_path, "r") as f:
    data = json.load(f)

data = clean_data(data)

with open(output_path, "w") as f:
    json.dump(data, f, indent=4)

print("Data cleaned successfully")