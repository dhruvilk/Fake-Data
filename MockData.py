from faker import Faker
# import csv
import numpy as np
from random import randint 
import random as r
import pandas as pd 
from faker.providers import BaseProvider

fake = Faker()

class CustomProvider(BaseProvider):
    __provider__ = "personalia"
    
    def personalia(self):
        gender = self.random_element(["F", "M"])
        first_name = self.generator.first_name_male() if gender == "M" else self.generator.first_name_female()
        last_name = self.generator.last_name()
        email_address = f"{first_name.lower()}.{last_name.lower()}@{self.generator.domain_name()}"
        
        return {
          "First name": first_name,
          "Last Name": last_name,
          "E-mail": email_address
        }
        
fake.add_provider(CustomProvider)

personalia = fake.personalia()
idNumbers = [1111, 2222, 3333, 4444]
symptoms = ['adhd', 'anxiety', 'depression']
phonenumbers = []

for i in range(0, 10):
    phonenumbers.append(r.randint(0, 9))

#function to create 
def input_data(x):
   
    # pandas dataframe
    data = pd.DataFrame()
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', 500)
    pd.set_option('max_colwidth', 400)
    pd.set_option('display.width', 1000)
    pd.options.display.float_format = '{:.0f}'.format
    for i in range(0, x):
        data.loc[i,'id']= int(np.random.choice(idNumbers))
        data.loc[i,'user info']= str(fake.personalia())
        data.loc[i,'address']= fake.address()
        data.loc[i,'birthday']= (fake.date_between())
        data.loc[i,'last check in']= (fake.date())
        data.loc[i,'next check in']= (fake.date())
        data.loc[i,'last assessment']= (fake.date())
        data.loc[i,'next assessment']= (fake.date())
        data.loc[i,'symptoms']= str(np.random.choice(symptoms))
        data.loc[i,'phone number']= (fake.phone_number())
    
    return data
   
info = input_data(100)
df = pd.DataFrame(info)
df.to_excel(r'C:\Users\dhruv\Downloads\Spring23\CS491\FakeData\data.xlsx', index=False)


# all this isnt used
#writing the dataframe into a csv row by row
# with open('data.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow([info])

# csv to excel for clean look i guess but im not using this. instead i write the dataframe to an excel file
# read_file = pd.read_csv (r'C:\Users\dhruv\Downloads\Spring23\CS491\FakeData\data.csv')
# read_file.to_excel (r'C:\Users\dhruv\Downloads\Spring23\CS491\FakeData\data.xlsx', index = None, header=True)
# end of not used
