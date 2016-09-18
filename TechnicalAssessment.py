# Code2040 Fellows Application
# Technical Assessment
# Chinasa T. Okolo, Fall 2016

import json
import requests
import math
import time
import datetime
import urllib2

# My API token
TOKEN = '887f59644a4b65b0f9a3cf52ba293ce3' 

# Step 1 - Connect to the registration endpoint
def Step1Registration(): 
   # myEndpoint = 'http://challenge.code2040.org/api/register'
    myGitHub = 'https://github.com/ChiNasa511/CODE2040-TechnicalAssessment/'
    #myKeys = {'token': TOKEN, 'github': myGithub}
    #response = requests.post(myEndpoint, json = myKeys)

    # Print the content of the response
    #print(response.text)
    
     registration_data = {'token': TOKEN, 'github': myGitHub}
     req = urllib2.Request('http://challenge.code2040.org/api/register')
     req.add_header('Content-Type', 'application/json')
     response = urllib2.urlopen(req, json.dumps(registration_data))

# Step 2 - Connect to the registration endpoint
def Step2():
    
    
# Step 3 - Connect to the registration endpoint
def Step3():


# Step 4 - Connect to the registration endpoint
def Step4():    
    
    
# Step 4 - Connect to the registration endpoint
def Step5(): 

