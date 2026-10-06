import json
import os 

#load the json data
def load_data(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, filename)
    with open(path , "r") as f:
        return json.load(f)

#function for find pages you might like

def find_pages_you_might_like(user_id ,data):
    #accessing all the liked_pages by all users
    user_pages = {}
    for user in data["users"]:
        user_pages[user['id']] = set(user['liked_pages'])

    #if given user id is not exist then return an empty list
    if user_id not in user_pages:
        return []

    user_liked_pages = user_pages[user_id]
    page_suggestions = {}

    for other_pages , pages in user_pages.items():
        if other_pages != user_id:
            shared_pages = user_liked_pages.intersection(pages)
            for page in pages:
                if page not in user_liked_pages:
                    page_suggestions[page] = page_suggestions.get(page , 0) + len(shared_pages)

    #sort recoomended pages based on the number of shared intersection
    sorted_pages = sorted(page_suggestions.items() , key= lambda x: x[1] , reverse= True)

    return [page_id for page_id , _ in sorted_pages]     

#load data 
data = load_data("data.json")
user_id = 1;
page_recommendations = find_pages_you_might_like(user_id , data)   
print(f"pages You might like for user {user_id} : {page_recommendations}")        