from faker import Faker
import csv


faker = Faker()
count = 30000
data = [faker.profile() for i in range(count+1)]

header = list(data[0].keys())

with open('data.csv', 'w', encoding='UTF8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)


file.close()
