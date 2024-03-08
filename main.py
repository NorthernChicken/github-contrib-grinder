import requests
import json
import time
import sys

def create_github_issue(repo_owner, repo_name, title, body, access_token):
    global requests_sent
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    headers = {
        "Authorization": f"token {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "title": title,
        "body": body
    }
    try:
        response = requests.post(url, headers=headers, json=data)
    except Exception as e:
        print("Could not reach Github. Check your internet connection.")
    if response.status_code == 201:
        print("Contribution number " + str(requests_sent) + " out of " + str(num_contribs) + " created successfully")
    elif response.status_code == 429:
        print("Github is rate limiting you! Please wait or turn on a VPN.")
        requests_sent -= 1
        time.sleep(5)
    elif response.status_code == 403:
        print("Github is blocking your requests! Github likely suspects spam, so try another repository and increase the contribution delay.")
        requests_sent -= 1
        time.sleep(50)
    elif response.status_code == 404:
        print("Could not find the requested repository.")
        requests_sent -= 1
        time.sleep(50)
    else:
        print(f"Failed to contact GitHub. Status code: {response.status_code}")
        requests_sent -= 1
        time.sleep(5)

with open("config.json") as json_config_file:
    config = json.load(json_config_file)

with open("secrets.json") as json_secrets_file:
    secrets = json.load(json_secrets_file)

repo_owner = config["repo_info"]["repo_owner"]
repo_name = config["repo_info"]["repo_name"]
title = config["issue_info"]["title"]
body = config["issue_info"]["body"]
access_token = secrets["secrets"]["github_access_token"]

try:
    num_contribs = int(input("How many contributions would you like to automate? "))
    contribs_delay = int(input("How long should the delay be between contribs? (In seconds. Shorter times may result in being rate limited by github faster): "))
except KeyboardInterrupt:
    print("")
    sys.exit("Abort.")
requests_sent = 1

for contribs in range(num_contribs):
    try:
        create_github_issue(repo_owner, repo_name, title, body, access_token)
        requests_sent += 1
        time.sleep(contribs_delay)
    except KeyboardInterrupt:
        sys.exit("Stopped.")
    except Exception as e:
        sys.exit("Sorry, something went wrong. Please try again.")
