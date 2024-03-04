import requests
import json
import time

def create_github_issue(repo_owner, repo_name, title, body, access_token):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    headers = {
        "Authorization": f"token {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "title": title,
        "body": body
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        return
    else:
        print(f"Failed to contact GitHub. Status code: {response.status_code}")

with open("config.json") as json_config_file:
    config = json.load(json_config_file)

with open("secrets.json") as json_secrets_file:
    secrets = json.load(json_secrets_file)

repo_owner = config["repo_info"]["repo_owner"]
repo_name = config["repo_info"]["repo_name"]
title = config["issue_info"]["title"]
body = config["issue_info"]["body"]
access_token = secrets["secrets"]["github_access_token"]

num_contribs = int(input("How many contributions would you like to automate?"))
requests_sent = 0

for contribs in range(num_contribs):
    create_github_issue(repo_owner, repo_name, title, body, access_token)
    print("Contribution number " + str(requests_sent) + " out of " + str(num_contribs) + " created successfully")
    requests_sent += 1
    time.sleep(0.25)
