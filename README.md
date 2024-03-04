# github-contrib-grinder

Using this bot, you can finally achieve that shiny, solid-green contribution history.

# Requirements

* Git
* Python

# Installation and Usage

1. Download the Repo: ``git clone https://github.com/NorthernChicken/github-contrib-grinder``
2. Enter the downloaded directory: ``cd github-contrib-grinder``
3. Install requirements: ``pip install -r requirements.txt``
4. Setup GitHub Access Token:
  * Log into GitHub.
  * Click your profile picture on the top right and go to "settings"
  * Navigate to "Developer options"
  * Go to "Personal Access tokens" and then "Tokens (classic)"
  * Generate a new classic token and under "select scopes" check "repo"
  * Generate the token and copy the Access Code
  * Paste the Access code in "secrets.json" under "github_access_token"
5. Run main.py to begin
