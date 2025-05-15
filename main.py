import os
from argparse import ArgumentParser
import requests

def fetch(username):
    url = f"https://api.github.com/users/{username}/events"
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers = headers)
    response.json()

    if response.status_code == "200":
        pass

def display():
    pass

def main() -> None:
    parser = ArgumentParser(description = "useractivity CLI")
    parser.add_argument("username", type = str.lower, help = "Github Username")
    parser.set_defaults(func = fetch)
    args = parser.parse_args()


if __name__ == "__main__":
    main()