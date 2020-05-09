"""
Written by Rowell Dionicio (@rowelldionicio)
Created on: May 8, 2020

Description: This Python module is for demo purposes of parsing through JSON.
Purpose is to get a list of SSIDs from the Mist cloud, iterate through that list,
and output the SSIDs to screen.

The auth.py file contains the Authorization token and Organization ID.
Auth file contains:

token = 'dc93...DA2'
orgid = 'xxxx-xxxx-xxxx-xxxx-xxxx'

"""

import requests
import json
import auth

base_url = 'https://api.mist.com/api/v1/' # Base URL for api
org_id = '{}'.format(auth.orgid) # Enter your Org ID

url = base_url+"sites/"+org_id+ "/wlans" # Full URL used in request

# Headers containing authorization
headers = {'Authorization': 'Basic {}'.format(auth.token)}

# Pass the contents of our GET request to variable "response"
response = requests.request("GET", url, headers=headers)

# Deserialize the text attribute of the response object
wlans = json.loads(response.text)

# Iterate through the list and print out each SSID
for wlan in wlans:
    print('SSID: ' + wlan['ssid'])
