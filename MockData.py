from faker import Faker
# import csv
import numpy as np
from random import randint 
import random
import pandas as pd 
from faker.providers import BaseProvider
from datetime import date, timedelta

fake = Faker()
#used to generate middle name depending on gender
class CustomProvider(BaseProvider):
    __provider__ = "personalia"
    
    def personalia(self):
        gender = self.random_element(["F", "M"])
        middle_name = self.generator.first_name_male() if gender == "M" else self.generator.first_name_female()
        return middle_name 
fake.add_provider(CustomProvider)

personalia = fake.personalia()
idNumbers = [1, 2, 3, 4]
symptoms = ['insomnia', 'lack of appetite', 'irritability', 'impulsivity', 'weight gain', 'inactivity', 'hyperactivity']
moods = ['happy', 'sad', 'confused', 'frustrated', 'angry', 'tired', 'restless', 'irritable', 'impulsive']

# # create x random provider practice names
# def providerPracticeNames(x):
   
#     # pandas dataframe
#     providerdata = pd.DataFrame()
#     pd.set_option('display.max_rows', None)
#     pd.set_option('display.max_columns', 500)
#     pd.set_option('max_colwidth', 400)
#     pd.set_option('display.width', 1000)
#     pd.options.display.float_format = '{:.0f}'.format
#     for i in range(0, x):
#         providerdata.loc[i,'practiceName']= str(fake.company())
#     return providerdata
# # call provider function to generate data and place it into a variable that can be turned into a dataframe to import to excel (this can later be saved as a csv)   
# providerInfo = providerPracticeNames(4)
# providerdf = pd.DataFrame(providerInfo)
# providerdf.to_excel(r'C:\Users\dhruv\Downloads\Spring23\CS491\Fake-Data\provider.xlsx', index=False)

# ########################################################################################################################################################################

# #generate x users and their information
# def user(x):
   
#     # pandas dataframe
#     usersdata = pd.DataFrame()
#     pd.set_option('display.max_rows', None)
#     pd.set_option('display.max_columns', 500)
#     pd.set_option('max_colwidth', 400)
#     pd.set_option('display.width', 1000)
#     pd.options.display.float_format = '{:.0f}'.format
#     for i in range(0, x):
#         usersdata.loc[i,'providerId']= int(np.random.choice(idNumbers))
#         usersdata.loc[i,'firstName']= str(fake.first_name())
#         usersdata.loc[i,'lastName']= str(fake.last_name())
        
#     return usersdata
# # call user function to generate data and place it into a variable that can be turned into a dataframe to import to excel (this can later be saved as a csv)   
# users = user(4)
# usersdf = pd.DataFrame(users)
# usersdf.to_excel(r'C:\Users\dhruv\Downloads\Spring23\CS491\Fake-Data\users.xlsx', index=False)

# ########################################################################################################################################################################

# #create information for x number of random patients
# def patients(x):
   
#     # pandas dataframe
#     patientdata = pd.DataFrame()
#     pd.set_option('display.max_rows', None)
#     pd.set_option('display.max_columns', 500)
#     pd.set_option('max_colwidth', 400)
#     pd.set_option('display.width', 1000)
#     pd.options.display.float_format = '{:.0f}'.format
#     for i in range(0, x):
#         patientdata.loc[i,'providerId']= int(np.random.randint(1,14))
#         patientdata.loc[i,'active']= bool(random.getrandbits(1))
#         patientdata.loc[i,'overdue']= bool(random.getrandbits(1))
#         patientdata.loc[i,'riskStatus']= (np.random.randint(0,100))
#         patientdata.loc[i,'firstName']= str(fake.first_name())
#         patientdata.loc[i,'middleName']= str(fake.personalia())
#         patientdata.loc[i,'lastName']= str(fake.last_name())
#         patientdata.loc[i,'dateOfBirth']= fake.date_of_birth()
#     return patientdata
# # call patients function to generate data and place it into a variable that can be turned into a dataframe to import to excel (this can later be saved as a csv)   
# patientinfo = patients(365)
# patientdf = pd.DataFrame(patientinfo)
# patientdf.to_excel(r'C:\Users\dhruv\Downloads\Spring23\CS491\Fake-Data\patient.xlsx', index=False)

# ########################################################################################################################################################################

# #generate daily metrics for x patients
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days+1)):
        yield start_date + timedelta(n)

start_date = date(2023, 1, 1)
end_date = date(2023, 12, 31)

def testMetrics(x):
    testMetricsData = pd.DataFrame()
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', 500)
    pd.set_option('max_colwidth', 400)
    pd.set_option('display.width', 1000)
    pd.options.display.float_format = '{:.0f}'.format
    for i in range(0,x):
        for createdAtDate in daterange(start_date, end_date):
            testMetricsData.loc[createdAtDate,'patientId']= int(77)
            testMetricsData.loc[createdAtDate,'adhd']= (np.random.randint(0,100))
            testMetricsData.loc[createdAtDate,'anxiety']= (np.random.randint(0,100))
            testMetricsData.loc[createdAtDate,'depression']= (np.random.randint(0,100))
            testMetricsData.loc[createdAtDate,'createdAt']= (createdAtDate)
            testMetricsData.loc[createdAtDate,'mood']= (np.random.choice(moods))
            testMetricsData.loc[createdAtDate,'dosages']= int(np.random.randint(1,5))
            testMetricsData.loc[createdAtDate,'dosagesTaken']= int(np.random.randint(1,5))
            testMetricsData.loc[createdAtDate,'checkedIn']= bool(random.getrandbits(1))
            testMetricsData.loc[createdAtDate,'moodLevel']= (np.random.randint(0,100))
        return testMetricsData
dailymetr = testMetrics(np.random.randint(1,356))
metricsdf = pd.DataFrame(dailymetr)
metricsdf.to_excel(r'C:\Users\dhruv\Downloads\Spring23\CS491\Fake-Data\test.xlsx', index=False)

# ########################################################################################################################################################################

# def sideEffects(x):
   
#     # pandas dataframe
#     sideeffects = pd.DataFrame()
#     pd.set_option('display.max_rows', None)
#     pd.set_option('display.max_columns', 500)
#     pd.set_option('max_colwidth', 400)
#     pd.set_option('display.width', 1000)
#     pd.options.display.float_format = '{:.0f}'.format
#     for i in range(0, x):
#         sideeffects.loc[i,'patientMetricsId']= int(np.random.randint(1,90))
#         sideeffects.loc[i,'patientId']= int(np.random.randint(1,90))
#         sideeffects.loc[i,'title']= str(np.random.choice(symptoms))        
#     return sideeffects
# # call side effects function to generate data and place it into a variable that can be turned into a dataframe to import to excel (this can later be saved as a csv)   
# effects = sideEffects(365)
# effectsdf = pd.DataFrame(effects)
# effectsdf.to_excel(r'C:\Users\dhruv\Downloads\Spring23\CS491\Fake-Data\sideeffects.xlsx', index=False)

# ########################################################################################################################################################################
