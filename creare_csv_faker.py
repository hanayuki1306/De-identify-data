import csv 
from faker  import Faker 
fake = Faker()

lookup={}
root_file ='2010BA_DEIDENT_INTHB0837I_286230_10160249.csv'
write_out_file = open('test_output.csv', 'w')
with open (root_file,'r') as csv_file:

    # headers ={
    #     'filename','transaction_loop','line_no,sha256_hash','entity_identifier_code','entity_type_qualifier','subscriber_last_name','subscriber_first_name','subscriber_middle_name_or_initial','identification_code_qualifier','subscriber_primary_identifier','subscriber_address_line','subscriber_address_line','subscriber_city_name','subscriber_state_code','subscriber_postal_zone_or_zip_code','location_identifier','date_time_period_format_qualifier','subscriber_birth_date','subscriber_gender_code','reference_identification_qualifier','subscriber_supplemental_identifier','subscriber_name_suffix'
    # }
    spamreader = csv.DictReader(csv_file)
    my_write = csv.DictWriter(write_out_file,fieldnames=spamreader.fieldnames) 
    my_write.writeheader()
    
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
    
write_out_file.close()