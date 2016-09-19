# Code2040 Fellows Application
# Technical Assessment
# Chinasa T. Okolo, Fall 2016

import json, unittest, requests, math, time, datetime

# My API token
TOKEN = '887f59644a4b65b0f9a3cf52ba293ce3'

# Step 1 - Connect to the registration endpoint
def Step1(): 
    myEndpoint = 'http://challenge.code2040.org/api/register'
    myGitHub = 'https://github.com/ChiNasa511/CODE2040TechnicalAssessment/'
    myKeys = {'token': TOKEN, 'github': myGitHub}
    response = requests.post(myEndpoint, myKeys)
    
    # Check for accuracy (was trying to do unit tests but not working)
    if response.status_code != 200:
        print response.text
        return response.text
   
# Step 2 - Reverse a string
def Step2(): 
    myEndpoint = 'http://challenge.code2040.org/api/reverse'
    yourEndpoint = 'http://challenge.code2040.org/api/reverse/validate'
    myKey = {'token': TOKEN}
    string = requests.post(myEndpoint, myKey)
    
    # Reverse and send string back
    reverseString = string.text[::-1]
    myKey = {'token': TOKEN, 'string': reverseString}
    string = requests.post(yourEndpoint, myKey)
    
    # Check if string sent 
    print string.text
    return string.text

# Ensure JSON response is received from all requests
def receiveJSON(myEndpoint):
    request = requests.post(myEndpoint, data = {'token': TOKEN})
    return request.json()
    
# Step 3 - Needle in a haystack
def Step3(): 
    dict = 'http://challenge.code2040.org/api/haystack'
    yourEndpoint = 'http://challenge.code2040.org/api/haystack/validate'
    needle = 'needle'
    haystack = 'haystack'
    myKey = {'token': TOKEN}
    
    # Get index
    for i, j in enumerate(haystack):
        if j == needle:
            needleIndex = i
            print needleIndex
    
    # Send index
    myKey = {'token': TOKEN, 'needle': needleIndex}
    result = requests.post(yourEndpoint, myKey)
    
    # Check if string sent 
    # if reverseString.status_code != 200:
    print result.text
    return result.text

# Trick for code to act as reusable module or as standalone program
if __name__ == "__main__":
    #Step1()
    #Step2()
    Step3()

