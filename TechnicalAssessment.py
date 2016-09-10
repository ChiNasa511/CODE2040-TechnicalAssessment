# Code2040 Fellows Application
# Technical Assessment
# Chinasa T. Okolo, Fall 2016

import json, requests, math, time, datetime

# My API token
token = '887f59644a4b65b0f9a3cf52ba293ce3'

# Step 1 - Connect to the registration endpoint
def Step1Registration()
  endpoint = 'http://challenge.code2040.org/api/register'
  github = 'https://github.com/ChiNasa511/CODE2040-TechnicalAssessment'
  response = requests.post(endpoint, data = {'token': token, 'github': github});

  # Print and return the content of the response
  print(response.content)
  return(response.content)

