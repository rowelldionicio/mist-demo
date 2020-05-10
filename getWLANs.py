"""
Written by Rowell Dionicio (@rowelldionicio)
https://rowelldionicio.com
Created on: May 8, 2020

Description: This Python module is for demo purposes of parsing through JSON.
Purpose is to get a list of SSIDs from the Mist cloud, iterate through that list,
and output the SSIDs to screen.
"""

import requests
import json
import time

base_url = 'https://api.mist.com/api/v1/' # Base URL for api
org_id = '9ae...799' # Enter your Org ID

url = base_url+"sites/"+org_id+ "/wlans" # Full URL used in request

# Headers containing authorization. Enter your token after "Basic"
headers = {'Authorization': 'Basic dm922...UTB2'}

# Pass the contents of our GET request to variable "response"
response = requests.request("GET", url, headers=headers)

def main():
    """
    Function to deserialize the text attribute of the response object,
    then iterate over the list and print out each SSID.
    """
    wlans = json.loads(response.text)

    # Iterate through the list and print out each SSID
    for wlan in wlans:
        print('SSID: ' + wlan['ssid'])

if __name__ == '__main__':
    """
    Function just to get the run time.
    """
    start_time = time.time()
    print('** Getting list of SSIDs\n')
    main()
    run_time = time.time() - start_time
    print("\n** Time to run: %s sec" % round(run_time,2))
