import json
import os 

#load the json data
def load_data(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base_dir, filename)
    with open(path , "r") as f:
        return json.load(f)

#function for find people you may know

def find_people_you_may_know(user_id ,data):
    #accessing all the friends in users
    user_friends = {}
    for user in data["users"]:
        user_friends[user['id']] = set(user['friends'])

    #if given user id is not exist then return an empty list
    if user_id not in user_friends:
        return []

    #accessing direct friends of given user id
    direct_friends = user_friends[user_id]
    suggestions = {}
    for friend in direct_friends:
        for mutual in user_friends[friend]: #accessing friends of direct friends of given user id
            if mutual != user_id and mutual not in direct_friends: #if mutual id is not the same user and not already direct friend of user 
                suggestions[mutual] = suggestions.get(mutual , 0) + 1

    sorted_sugg = sorted(suggestions.items() , key= lambda x: x[1] , reverse= True)
    return [user_id for user_id , _ in sorted_sugg]

#load data
data = load_data("data.json")
user_id = 1
recc = find_people_you_may_know(user_id , data)
print(f"find people you may know for user {user_id} : {recc}")