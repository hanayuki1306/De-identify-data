from faker import Faker
import datetime
import json
faker = Faker()
people = []

for _ in range(10):
    simple_profile = faker.simple_profile()

    person = {
        "name":simple_profile["name"],
        "age": datetime.date.today().year - simple_profile["birthdate"].year,
        "date":str(simple_profile["birthdate"]),
        "sex":simple_profile["sex"],
        "com    pany": faker.company()
        }
    people.append(person)
File = open("output.txt","w")
File.write(json.dumps(people))
File.close()