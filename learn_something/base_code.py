from faker import Faker
from faker.providers import person, address
import csv
import os
from pprint import pprint
faker = Faker()
faker.add_provider(person)
faker.add_provider(address)
subcriber = [
    'subscriber_last_name',
    'subscriber_first_name',
    'subscriber_middle_name_or_initial',
    'subscriber_name_suffix',
    'subscriber_primary_identifier',  # key
    'subscriber_address_line',
    'subscriber_city_name',
    'subscriber_postal_zone_or_zip_code',
    'subscriber_birth_date'
]
subcriber_faker = [
    'last_name',
    'first_name',
    'suffix',
    'random_uppercase_letter',
    'ean13',
    'street_address',
    'city_suffix',
    'zipcode',
    'date'
]

look_up = {}


# {
#     '87987897978': {
#                         'subscriber_gender_code': "nam",
#                         'date_time_period_format_qualifier': "asdfadf"
#                     },
#     '12121211212': {
#                         'subscriber_gender_code': "nu",
#                         'date_time_period_format_qualifier': '798798'
#                     },
# }


write_file = open('output.csv', 'w')
with open('2010BA_DEIDENT_INTHB0837I_286230_10160249.csv', 'r') as file:
    spamreader = csv.DictReader(file)
    myWriter = csv.DictWriter(write_file, fieldnames=spamreader.fieldnames)
    for row in spamreader:
        key = row["subscriber_primary_identifier"]

        if key in look_up:
            # Look up existing values
            values = look_up[key]
            # {
#                         'subscriber_gender_code': "nam",
#                         'date_time_period_format_qualifier': "asdfadf"
#                     }
            row['subscriber_gender_code'] = values['subscriber_gender_code']
            row[
                'date_time_period_format_qualifier'
            ] = values['date_time_period_format_qualifier']
        else:
            # Create new vlues
            subscriber_gender_code = faker.random_element(
                elements=('nam', 'nu')
            )
            row['subscriber_gender_code'] = subscriber_gender_code

            dtpfq = faker.random_element(
                elements=('sdf', 'asdfadf', '798798')
            )
            row['date_time_period_format_qualifier'] = dtpfq

            look_up[key] = {
                'subscriber_gender_code': subscriber_gender_code,
                'date_time_period_format_qualifier': dtpfq
            }

        myWriter.writerow(row)

write_file.close()
# for row in spamreader:
#     print(row)
output_dir = 'Output'
# if(os.path.exists(output_dir)):
#     with open(output_dir + '/2010BA_DEIDENT_INTHB0837I_286230_10160249_new.csv', 'w', newline='') as csv_file:
#         # fieldnames = row.keys()
#         writer = csv.writer(csv_file)
#         header = spamreader[0].keys()
#         writer.writeheader(header)
#         for row in spamreader:

#             writer.writerow(row)

# else:
#     os.makedirs(output_dir)
#     with open(output_dir + '/2010BA_DEIDENT_INTHB0837I_286230_10160249_new.csv', 'w', newline='') as csv_file:
#         writer = csv.writer(csv_file)
#         header = row.keys()
#         writer.writeheader(header)
#         for row in spamreader:
#             header = row.keys()
#             writer.writeheader(header)
#             writer.writerow(row)