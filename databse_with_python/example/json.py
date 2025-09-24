import json

json_data = {
    'name': 'Gabriel',
    'age': 32,
    'address': [
        'A',
        'B'
    ]
}

with open('data.json', 'w') as f:
    json.dump(json_data, f)

with open('data.json', 'r') as f:
    read_data = json.load(f)
    print(read_data)