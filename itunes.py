import requests
import sys
import json #used to manipulate json data

if len(sys.argv) != 2 :
    sys.exit()

response = requests.get("url")
print(response)
