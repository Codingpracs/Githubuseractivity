import os
from argparse import ArgumentParser
import requests

class HTTPerror():
    pass

def fetch(username) -> None:
    url = f"https://api.github.com/users/{username}/events"
    headers = {"Content-Type": "application/json"}
    try:
        response = requests.get(url, headers = headers)
        response.json()
    except HTTPerror as e:
        if e.status_code == 404:
            print("Error: User not found")
        else:
            print(f"HTTP Error:{e.status_code} ")

    # if response.status_code == "200":
    #     pass

def display(events):
    activity_log = []
    for event in events[:5]:
        event_type = event['type']
        if event_type == "WatchEvent":
            activity_log.append(f"starred {event['repo']['name']}")
        elif event_type == "PushEvent":
            push_counts = len(event['payloads']['commits'])
            repo = event['repo']['name']
            activity_log.append(f"pushed {push_counts} commits to {repo}")
        elif event_type == "CommitCommentEvent":
            pass
        elif event_type == "CreateEvent":
            pass
        elif event_type == "DeleteEvent":
            pass
        elif event_type == "ForkEvent":
            pass
        elif event_type == "GollumEvent":
            pass
        elif event_type == "IssueCommentEvent":
            pass
        elif event_type == "IssuesEvent":
            pass
        elif event_type == "MemberEvent":
            pass
        elif event_type == "PublicEvent":
            pass
        elif event_type == "PullRequestEvent":
            pass
        elif event_type == "ReleaseEvent":
            pass



def main() -> None:
    parser = ArgumentParser(description = "useractivity CLI")
    parser.add_argument("username", type = str.lower, help = "Github Username")
    parser.set_defaults(func = fetch)
    args = parser.parse_args()


if __name__ == "__main__":
    main()