# Code2040 Fellows Application
# Technical Assessment
# Chinasa T. Okolo, Fall 2016

import json, unittest, requests, math, time, datetime

# My API token
TOKEN = '887f59644a4b65b0f9a3cf52ba293ce3'

# Step 1 - Connect to the registration endpoint
def Step1Registration(): 
    myEndpoint = 'http://challenge.code2040.org/api/register'
    myGitHub = 'https://github.com/ChiNasa511/CODE2040TechnicalAssessment/'
    myKeys = {'token': TOKEN, 'github': myGitHub}
    response = requests.post(myEndpoint, myKeys)
    
    if response.status_code != 200:
        print 'Registration Failed'
    else:
        print 'Registration Successful'

    # Print the content of the response
   # print response.text
    #return response.text

# Ensure JSON response is received from requests
def receiveJSON(myEndpoint):
    request = requests.post(myEndpoint, data = {'token': TOKEN})
    return request.json()
    
# Check all steps using unit tests
class APIChallengeTest(unittest.TestCase):
    
    def Step1Test(self):
        self.assertEqual("Step 1 Complete", Step1Registration())

# Trick for code to act as reusable module or as standalone program
if __name__ == "__main__":
    unittest.main()

