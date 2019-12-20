#create file
import requests

url = "http://s3.zylowski.net/public/input/5.txt"

r = requests.get(url)
with open('file.txt', 'w') as file:
    file.write(r.text)