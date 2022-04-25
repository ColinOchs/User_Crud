import requests
from pprint import pprint

URL = "http://127.0.0.1:5000/users"   


def deactivate_user(user_data, user_id):                #updated
    url = "%s/%s/" % (URL, user_id)                 #updated
    response = requests.delete(url, json=user_data)    #updated
    if response.status_code == 204:
        print("Successfully updated user.")
    else:
        print("Something went wrong while trying to update user")


def get_user(user_id):
    url = "%s/%s/" % (URL, user_id)                 #updated
    response = requests.get(url)                    #updated
    if response.status_code == 200:
        print("User: ")
        pprint(response.json())
        return response.json().get("user")[0]       #updated
    else:
        print("Something went wrong while trying to retrieve the user.")
        return ""


if __name__ == "__main__":
    user_id = input("Type in the user's id: ")
    target_user = get_user(int(user_id))
    active = input("deactivate user? (Y/N): ")   
    if active == "y" or active == "Y":
        active = 0
        target_user["active"] = active   
    deactivate_user(target_user, user_id)
        
    option = input("Would you like to see the updated user? [y/N]: ")
    if option == "y" or option == "Y":
        get_user(user_id)