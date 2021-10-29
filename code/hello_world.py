import requests


def get_users(n_of_users):
    """retrieve the user names from random user API

    Args:
        n_of_users ([integer]): [how many users data we are looking for]
    """
    response = requests.get(f"https://randomuser.me/api/?results={n_of_users}")
    data = response.json()

    for user in data["results"]:
        email = user["email"]
        print(email)
