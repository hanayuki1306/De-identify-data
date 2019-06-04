import csv
from faker import Faker 
import os
faker = Faker()
# fake.name()



lookup = {}

write_file = open('output111111.csv','w')
with open('2010BA_DEIDENT_INTHB0837I_286230_10160249.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    myWriter = csv.DictWriter(write_file, fieldnames=csv_reader.fieldnames)
    for row in csv_reader:
            key = row["subscriber_primary_identifier"]
            # key = row['transaction_loop']
            if key in lookup:
                values = lookup[key]
                row['transaction_loop'] = values['transaction_loop']
                #    row['subscriber_gender_code'] = values['subscriber_gender_code']

            else:
                transaction_loop = faker.random_element(elements=("wttttttttf","wtfffffffa")
       )
                row['transaction_loop']= transaction_loop

    myWriter.writerow(row)
csv_file.close















# import csv

# csv.register_dialect('myDialect',
# delimiter = ',',
# quoting=csv.QUOTE_ALL,
# skipinitialspace=True)

# with open('2010BA_DEIDENT_INTHB0837I_286230_10160249.csv', 'r') as f:
#     reader = csv.reader(f, dialect='myDialect')
#     for row in reader:
#         print(row)
#         break

# from faker import Faker
# import csv 
# faker = Faker()

# with open('2010BA_DEIDENT_INTHB0837I_286230_10160249.csv','r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     # line_count = 0 

# File = open('output.csv','w'):
#     for row in csv_reader:
#         if row['subscriber_primary_identifier'] == row['subscriber_primary_identifier'] :
#             pass
#         else:
#             for row in csv_reader:
#         # if row['subscriber_primary_identifier']==row['subscriber_primary_identifier']:
#         #     print("something wrong")
#             simple_profile = faker.simple_profile()
#             row['subscriber_last_name'] = simple_profile["name"]
#         # print(row['subscriber_last_name'])
