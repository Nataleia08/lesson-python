users = {
    "Boby": {
        "first_name": "Bob",
        "last_name": "File",
        "location": "Las Vegas"
    },
    "Alise": {
        "first_name": "Alise",
        "last_name": "Erica",
        "location": "New York"
    }
}

for username, user_info in users.items():
    print("Username" + username)
    full_name = user_info["first_name"] + " " + user_info["last_name"]
