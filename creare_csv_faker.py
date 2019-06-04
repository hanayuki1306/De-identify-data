import csv 
from faker  import Faker 
fake = Faker()

lookup={}

son_write = open('test_output.csv', 'w')
with open ('2010BA_DEIDENT_INTHB0837I_286230_10160249.csv','r') as csv_file:

    spamreader = csv.DictReader(csv_file)
    my_write = csv.DictWriter(son_write,fieldnames=spamreader.fieldnames) 
    
    for row in spamreader:

        key = row['subscriber_primary_identifier']

        if key in lookup:

            values = lookup[key]

            row['subscriber_last_name']= values['subscriber_last_name']

            row['subscriber_address_line'] = values['subscriber_address_line']

            row['subscriber_city_name'] = values['subscriber_city_name']

        else:
            fake_name= fake.name()
            fake_address = fake.address()
            sex = fake.random_element(elements=('F','M'))

            row['subscriber_last_name'] = fake_name

            row['subscriber_address_line'] = fake_address

            row['subscriber_city_name'] = sex

            lookup[key] = {
                'subscriber_last_name': fake_name,

                'subscriber_address_line': fake_address,

                'subscriber_city_name': sex
            }
        my_write.writerow(row)
    
son_write.close()