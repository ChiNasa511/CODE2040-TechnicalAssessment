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
    
# Helper to ensure JSON response is received from all requests
def receiveJSON(APIendpoint):
    request = requests.post(APIendpoint, data = {'token': TOKEN})
    return request.json()
    
# Step 3 - Needle in a haystack
def Step3(): 
    dict = receiveJSON('http://challenge.code2040.org/api/haystack')
    yourEndpoint = 'http://challenge.code2040.org/api/haystack/validate'
    needle = dict['needle']
    haystack = dict['haystack']
    
    # Get index - this case is best when needle is present at multiple indicies
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
    
# Step 4 - Prefix
def Step4(): 
    dict = receiveJSON('http://challenge.code2040.org/api/prefix')
    yourEndpoint = 'http://challenge.code2040.org/api/prefix/validate'
    myPrefix = dict['prefix']
    myArray = dict['array']
    
    print myArray
    
    # Return an array containing strings not starting with prefix
    newArray = [word for word in myArray if not word.startswith(myPrefix)]
    
    # Post dictionary once array is built
    myKey = {'token': TOKEN, 'array': newArray}
    posted = requests.post(yourEndpoint, json = myKey)
    
    print posted.text
    return posted.text

# Trick for code to act as reusable module or as standalone program
if __name__ == "__main__":
    #Step1()
    #Step2()
    #Step3()
    Step4()

