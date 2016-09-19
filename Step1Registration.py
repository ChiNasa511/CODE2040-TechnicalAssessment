# Code2040 Fellows Application
# Technical Assessment
# Chinasa T. Okolo, Fall 2016

import json
import requests
import math
import time
import datetime

# My API token
TOKEN = '887f59644a4b65b0f9a3cf52ba293ce3'

# Step 1 - Connect to the registration endpoint
def Step1Registration(): 
    myEndpoint = 'http://challenge.code2040.org/api/register'
    myGitHub = 'https://github.com/ChiNasa511/CODE2040TechnicalAssessment/'
    myKeys = {'token': TOKEN, 'github': myGitHub}
    response = requests.post(myEndpoint, myKeys)

    # Print the content of the response
    print response.text
    return response.text

# Trick for code to act as reusable module or as standalone program
if __name__ == '__Step1Registration__':
   main()
