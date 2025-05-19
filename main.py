import os
from argparse import ArgumentParser
import requests
from requests.exceptions import HTTPError 

# class HTTPerror():
#     pass

def fetch(username) -> None:
    url = f"https://api.github.com/users/{username}/events"
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.get(url, headers = headers)
        # raise HTTPError 
        response.raise_for_status()
        return response.json()
    except HTTPError as e:
        if e.status_code == 404:
            print("Error: User not found")
        else:
            print(f"HTTP Error:{response.status_code} ")
        return [] # return empty list if error occurs
    except Exception as e:
        print(f"unexpected error: {e}")
        return []

    # if response.status_code == "200":
    #     pass

def display(events):
    activity_log = []
    for event in events[:10]:
        event_type = event['type']

        if event_type == "WatchEvent":
            activity_log.append(f"starred {event['repo']['name']}")

        elif event_type == "PushEvent":
            push_counts = len(event['payload']['commits'])
            repo = event['repo']['name']
            activity_log.append(f"pushed {push_counts} commits to {repo}")

        elif event_type == "CommitCommentEvent":
            activity_log.append(f"committed comment to {event['repo']['name']}")

        elif event_type == "CreateEvent":
            activity_log.append(f"created {event['payload']['ref_type']}")

        elif event_type == "DeleteEvent":
            activity_log.append(f"Deleted {event['payload']['ref_type']}")

        elif event_type == "ForkEvent":
            activity_log.append(f"Forked {event['repo']['name']}")
        
        elif event_type == "IssuesEvent":
            activity_log.append(f"{event['payload']['action']} in {event['repo']['name']} ")

        else:
            activity_log.append(f"Performed {event['type']} on {event['repo']['name']}")

    return activity_log

def main() -> None:
    parser = ArgumentParser(description = "useractivity CLI")
    parser.add_argument("username", type = str, help = "Github Username")
    args = parser.parse_args()

    event = fetch(args.username)

    if event:
        activity_log = display(event)
        print("\nRecent Activity:")
        for activity in activity_log:
            print(f"- {activity}")
    else:
        print ("No Recent Activities Found")


if __name__ == "__main__":
    main()