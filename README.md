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
5. Run main.py to begin. Enter the number of contributions you would like to make.
6. Enter the delay between contributions. A lower number contributes faster but increases the risk of Github limiting your API usage. A good amount is between 20-30 seconds.

![image](https://github.com/NorthernChicken/github-contrib-grinder/assets/144752748/bdb6cdb5-bda6-49d3-9746-533871497ef9)

Results after running for 20 minutes on an alt. Note that the number of contributions in a certain time depends on your contribution delay.

# Troubleshooting

If GitHub limits your requests (Status code 403), then you just have to wait a few hours. Try increasing the contribution delay to avoid detection. 

By default, the bot opens issues on this repo, but I've found that changing repos occasionally in config.json can solve some problems. If you make your own private repo for that purpose, then make sure "Include private contributions on my profile" is selected in Public Profile settings, or the contributions won't show on your profile.

Basically any problems with Github limiting your API usage are cleared up if you just wait a few hours.

# DISCLAIMER

I am not responsible for any damages incurred by the use of this bot. Please use responsibly and only bot issues on this repository or one of your own.

While you likely won't get banned for using this, use at your own discretion.
