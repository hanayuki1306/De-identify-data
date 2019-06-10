import csv 
from faker import Faker
fake = Faker()

lookup = {}

file_csv = '2010BA_DEIDENT_INTHB0837I_286230_10160249.csv'

# def root_file(file_csv):
#     return file_csv



write_out_file = open('/home/hanayuki/Desktop/trainning-ABX/DB_0406/result/change2010BA_DEIDENT_INTHB0837I_286230_10160249.csv','w')
with open(file_csv,'r') as csv_file:

    spamreader = csv.DictReader(csv_file)
    write_out_result = csv.DictWriter(write_out_file,fieldnames=spamreader.fieldnames)
    
    write_out_result.writeheader()

    for row in spamreader:
        key = row['subscriber_primary_identifier']
        
        if key in lookup:
            values = lookup[key]

            row['subscriber_last_name'] = values['subscriber_last_name']
            row['subscriber_first_name'] = values['subscriber_first_name']    
            row['subscriber_name_suffix'] = values['subscriber_name_suffix']
            row['subscriber_address_line'] = values['subscriber_address_line']
            row['subscriber_city_name'] = values['subscriber_city_name']
            row['subscriber_state_code'] = values['subscriber_state_code']
            row['subscriber_postal_zone_or_zip_code'] = values['subscriber_postal_zone_or_zip_code']
            row['subscriber_birth_date'] = values['subscriber_birth_date']
            
        else:
            row['subscriber_last_name'] = fake.last_name()
            row['subscriber_first_name'] = fake.first_name()
            row['subscriber_name_suffix'] = fake.suffix()
            row['subscriber_address_line'] = fake.address()
            row['subscriber_city_name']  = fake.city()
            row['subscriber_state_code'] = fake.military_state()    
            row['subscriber_postal_zone_or_zip_code'] = fake.postalcode()
            row['subscriber_birth_date'] = fake.date_of_birth(tzinfo=None, minimum_age=40, maximum_age=115)
           
        write_out_result.writerow(row)

    write_out_file.close()