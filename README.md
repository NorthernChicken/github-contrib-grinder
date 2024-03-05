# github-contrib-grinder

Using this bot, you can finally achieve that shiny, solid-green contribution history.

# Requirements

* Git
* Python

# Installation and Usage

1. Download the Repo: ``git clone https://github.com/NorthernChicken/github-contrib-grinder-main``
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

![image](https://github.com/NorthernChicken/github-contrib-grinder/assets/144752748/bdb6cdb5-bda6-49d3-9746-533871497ef9)
Results after running for 20 minutes on an alt. Note that not every contribution that the bot sends will make it through, and GitHub will flag most of them as spam.

# Troubleshooting

If GitHub limits your requests (Status code 403), then either wait a while or turn on a VPN. You might also want to try another repository. By default, it opens issues on this repo, but I've found that changing repos occasionally in config.json can solve some problems. If you make your own private repo for that purpose, then make sure "Include private contributions on my profile" is selected in Public Profile settings.

# DISCLAIMER

I am not responsible for any damages incurred by the use of this bot. Please use responsibly and only bot issues on this repository or one of your own.
