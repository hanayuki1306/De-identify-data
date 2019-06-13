from faker import Faker
import os
# import csv


faker = Faker()

data_file = 'subscriber_name.txt'

result_file = './result_file_txt/demo_result.txt'
with open(data_file,'r') as txt_file:


    with open(result_file,'w') as f:
        reader = txt_file.readlines()
        for row in reader:
                list_str = row.split('*')
                list_str[3] = faker.first_name()
                list_str[4] = faker.last_name()
                list_str[9] = str(faker.random_number(11, True)) + '~'
                s = '*'
                f.write(s.join(list_str) + '\n')
    f.close()

txt_file.close()


