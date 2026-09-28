import requests
from json import JSONDecodeError,loads
import sys
#used to send http requests to a site from a python program 
response = requests.get("https://google.com")
#send get request to this url 

code = response.status_code
print(code)
text = response.text
#print(text)

#A lot of modern websites doesn't send html they send json 
#json stands for javascript object notation 
try:
    data = response.json() #api gave json and now convert it to python data
    print(data)
    data = str(data)
    print(loads(data))
    sys.exit()
except JSONDecodeError:
    print("Response is not valid JSON.")

print(text)

#difference between string and object json 

#string json - '{"name":"sreelekshmi"}
#object json - {"name":"sreelekshmi"}