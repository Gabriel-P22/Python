import csv

with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow([
        'name',
        'age'
    ])
    writer.writerow([
        'Gabriel',
        '23'
    ])