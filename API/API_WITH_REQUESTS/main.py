import requests

url = "https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json"

response = requests.get(url)
print(response)
res = response.json()

if response.status_code == 200:    
    restaurant_dto = {}

    for item in res:
        name = item["Company"]

        if name not in restaurant_dto:
            restaurant_dto[name] = []
        
        restaurant_dto[name].append({
            "item": item["Item"],
            "price": item["price"],
            "description": item["description"]
        })
       

    print(restaurant_dto["McDonald’s"])
else:
    print(f"O erro foi {response.status_code}")
