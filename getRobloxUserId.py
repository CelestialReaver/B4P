import requests

API_ENDPOINT = "https://users.roblox.com/v1/usernames/users"

def getUserId(username):

    requestPayload = {
        "usernames": [
            username
        ],

        "excludeBannedUsers": True # Whether to include banned users within the request, change this as you wish
    }

    responseData = requests.post(API_ENDPOINT, json=requestPayload)

    # Make sure the request succeeded
    assert responseData.status_code == 200

    userId = responseData.json()["data"][0]["id"]

    print(f"getUserId :: Fetched user ID of username {username} -> {userId}")
    return userId
    
getUserId("Ksprinkles811")