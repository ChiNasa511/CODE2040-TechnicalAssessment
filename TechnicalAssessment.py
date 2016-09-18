# Code2040 Fellows Application
# Technical Assessment
# Chinasa T. Okolo, Fall 2016

import json, requests, math, time, datetime

# My API token
myAPIToken = '887f59644a4b65b0f9a3cf52ba293ce3'

# Step 1 - Connect to the registration endpoint
def Step1Registration(): 
    myEndpoint = 'http://challenge.code2040.org/api/register'
    myGithub = 'https://github.com/ChiNasa511/CODE2040-TechnicalAssessment'
    myKeys = {'token': myAPIToken, 'github': myGithub}
    response = requests.post(myEndpoint, data = myKeys)

    # Print and return the content of the response
    print(response.text)
    return(response.text)

# Step 2 - Connect to the registration endpoint
def Step2():
    
    
# Step 3 - Connect to the registration endpoint
def Step3():


# Step 4 - Connect to the registration endpoint
def Step4():    
    
    
# Step 4 - Connect to the registration endpoint
def Step5(): 

