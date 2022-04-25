import requests

URL = "http://127.0.0.1:5000/users/"

def del_user(user_id):
    response = requests.delete(URL+str(user_id))
    if response.status_code == 204:
        print("Success")
    else:
        print("error deleting user")

if __name__ == "__main__":
    user_id = input("enter user's id: ")
    del_user(user_id)
