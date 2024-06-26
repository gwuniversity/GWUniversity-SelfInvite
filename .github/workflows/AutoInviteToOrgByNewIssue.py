## GWU Modified Code from this repository.
## Max Base
## 2021-06-19
## https://github.com/BaseMax/AutoInviteToOrgByIssueComment

import os
import sys
import json
import requests

MY_GITHUB_KEY = os.environ['MY_GITHUB_KEY']
COMMUNITY_TEAM_ID = os.environ['COMMUNITY_TEAM_ID']

file = open(os.environ['GITHUB_EVENT_PATH'])
data = json.load(file)

# print("Data:")
# print(data)

COMMENT = data["issue"]["title"]
USERNAME = data["issue"]["user"]["login"] # assumes this value is always present

# print("COMMENT:")
# print(COMMENT)
# print("USERNAME:")
# print(USERNAME)

if "RAISEHIGH" not in COMMENT.upper():
  sys.exit()
else:

  print('Send invite for the @'+USERNAME)

  # TODO: check user already joined or no....
  url = 'https://api.github.com/teams/'+COMMUNITY_TEAM_ID+'/memberships/' + USERNAME
  payload=''
  headers = {
      'Accept': 'application/vnd.github.v3+json',
      'Authorization': 'token '+MY_GITHUB_KEY
  }
  response = requests.request("PUT", url, headers=headers, data=payload)
  print(response.text)
