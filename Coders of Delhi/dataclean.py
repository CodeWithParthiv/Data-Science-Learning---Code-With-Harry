import json

def load_data(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

data = load_data('data2.json')

def clean_data(data):

    # Deleting the users which do not have names
    data['users'] = [user for user in data['users'] if user['name'].strip()]

    # Removing duplicate friends
    for user in data['users']:
        user['friends'] = list(set(user['friends']))

    # Remove inactive users
    data['users'] = [user for user in data['users'] if user['friends'] or user['liked_pages']]

    # Remove duplicate pages
    unique_pages = {}
    for page in data['pages']:
        unique_pages[page['id']] = page
    data['pages'] = list(unique_pages.values())
    

    return data

cleaned_data = json.dump(clean_data(data), open('cleaned_data.json', 'w'), indent=4)


