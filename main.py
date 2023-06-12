import requests
import random

def car():
    response = requests.get("https://api.thecatapi.com/v1/images/search").json()
    json = response[0]
    cat_url = json["url"]

    img = requests.get(cat_url).content
    with open(f'{random.randint(0,99999)}.jpg', 'wb') as handler:
        handler.write(img)

ans = input("How many cat images do you want to download: ")

for i in range(int(ans)):
    car()
print(f"Downloaded {ans} cat images.")
