import json

def load_data(filename):
    with open(filename, 'r') as f:
        return json.load(f)
    
# People you may know

def people_you_may_know(user_id, data):
    user_friends = {}
    for user in data['users']:
        user_friends[user['id']] = set(user['friends'])

    
    # Default case
    if user_id not in user_friends:
        print(f"User ID {user_id} not found.")
        return
    
    direct_friends = user_friends[user_id]

    suggestions = {}
    for friend in direct_friends:
        for mutual in user_friends[friend]:
            if mutual != user_id and mutual not in direct_friends:
                # Count mutual friends 
                if mutual not in suggestions:
                    suggestions[mutual] = 0   #Initialize the count for mutual friends
                suggestions[mutual] += 1      # Increment the count for mutual friends (if it is present again through another friend)

    # Sort suggestions by number of mutual friends
    sorted_suggestions = sorted(suggestions.items(), key=lambda x: x[1], reverse=True)


    # Return the suggestions
    return [user for user, count in sorted_suggestions]

            
    


# Load the data
data = load_data('massivedata.json')

user_id = 11
recc =  people_you_may_know(user_id, data)
print(recc)

