from faker import Faker
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

# create x random provider practice names
def providerPracticeNames(x):
    # pandas dataframe
    providerdata = pd.DataFrame()
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', 500)
    pd.set_option('max_colwidth', 400)
    pd.set_option('display.width', 1000)
    pd.options.display.float_format = '{:.0f}'.format
    for i in range(0, x):
        providerdata.loc[i,'practiceName']= str(fake.company())
    return providerdata
# call provider function to generate data and place it into a variable that can be turned into a dataframe to import to excel (this can later be saved as a csv)
providerInfo = providerPracticeNames(4)
providerdf = pd.DataFrame(providerInfo)
providerdf.to_excel(r'C:\Users\dhruv\Downloads\Spring23\CS491\Fake-Data\provider.xlsx', index=False) #enter a path here to save output to xlsx format

# ########################################################################################################################################################################

#generate x users and their information
def user(x):
    # pandas dataframe
    usersdata = pd.DataFrame()
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', 500)
    pd.set_option('max_colwidth', 400)
    pd.set_option('display.width', 1000)
    pd.options.display.float_format = '{:.0f}'.format
    for i in range(0, x):
        usersdata.loc[i,'providerId']= int(np.random.choice(idNumbers))
        usersdata.loc[i,'firstName']= str(fake.first_name())
        usersdata.loc[i,'lastName']= str(fake.last_name())
    return usersdata
# call user function to generate data and place it into a variable that can be turned into a dataframe to import to excel (this can later be saved as a csv)
users = user(4)
usersdf = pd.DataFrame(users)
usersdf.to_excel(r'C:\Users\dhruv\Downloads\Spring23\CS491\Fake-Data\users.xlsx', index=False) #enter a path here to save output to xlsx format

# ########################################################################################################################################################################

#create information for x number of random patients
def patients(x):
    # pandas dataframe
    patientdata = pd.DataFrame()
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', 500)
    pd.set_option('max_colwidth', 400)
    pd.set_option('display.width', 1000)
    pd.options.display.float_format = '{:.0f}'.format
    for i in range(0, x):
        patientdata.loc[i,'providerId']= int(np.random.randint(1,14))
        patientdata.loc[i,'active']= bool(random.getrandbits(1))
        patientdata.loc[i,'overdue']= bool(random.getrandbits(1))
        patientdata.loc[i,'riskStatus']= (np.random.randint(0,100))
        patientdata.loc[i,'firstName']= str(fake.first_name())
        patientdata.loc[i,'middleName']= str(fake.personalia())
        patientdata.loc[i,'lastName']= str(fake.last_name())
        patientdata.loc[i,'email']= fake.date_of_birth()
        patientdata.loc[i,'birthday']= fake.date_of_birth()
    return patientdata
# call patients function to generate data and place it into a variable that can be turned into a dataframe to import to excel (this can later be saved as a csv)
patientinfo = patients(365)
patientdf = pd.DataFrame(patientinfo)
patientdf.to_excel(r'C:\Users\dhruv\Downloads\Spring23\CS491\Fake-Data\patient.xlsx', index=False) #enter a path here to save output to xlsx format

# ########################################################################################################################################################################

startingPatientId = 1
finalPatientId = 10
outfileExtension = '.xlsx'
outfilePath = 'C:\\Users\\dhruv\\Downloads\\Spring23\\CS491\\Fake-Data\\dailymetric'

outfileExtension = '.xlsx'
originFileName = 'dailymetric'
originFileNumber = 1
outfileOriginal = ("".join([originFileName, str(originFileNumber), outfileExtension]))

for i in range(startingPatientId, finalPatientId):
    outfileFinal= ("".join([outfilePath, str(startingPatientId), outfileExtension]))
    outfileDelete = ("".join([originFileName, str(originFileNumber+1), outfileExtension]))
    print(outfileDelete)
    def daterange(start_date, end_date):
        for n in range(int((end_date - start_date).days+1)):
            yield start_date + timedelta(n)
    start_date = date(2023, 1, 1)
    end_date = date(2023, 12, 31)

    def testMetrics():
        testMetricsData = pd.DataFrame()
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', 500)
        pd.set_option('max_colwidth', 400)
        pd.set_option('display.width', 1000)
        pd.options.display.float_format = '{:.0f}'.format
        for createdAtDate in daterange(start_date, end_date):
            testMetricsData.loc[createdAtDate,'patientId']= int(startingPatientId-1)
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

    startingPatientId+=1
    
    dailymetr = testMetrics()
    metricsdf = pd.DataFrame(dailymetr)
    metricsdf.to_excel(outfileFinal, index=False) #enter a path here to save output to xlsx format


    # read the data of excel file you want information from
    df=pd.read_excel(outfileFinal)

    # appending the data of df after the data of the excel file you want the data in
    with pd.ExcelWriter(outfileOriginal,mode="a",engine="openpyxl",if_sheet_exists="overlay") as writer:
        df.to_excel(writer, sheet_name="Sheet1",header=None, startrow=writer.sheets["Sheet1"].max_row,index=False)
    originFileNumber+=1

# ########################################################################################################################################################################

startingPatientId = 1
finalPatientId = 91
outfileExtension = '.xlsx'
outfilePath = 'C:\\Users\\dhruv\\Downloads\\Spring23\\CS491\\Fake-Data\\sideeffects'

outfileExtension = '.xlsx'
originFileName = 'sideeffects'
originFileNumber = 1
outfileOriginal = ("".join([originFileName, str(originFileNumber), outfileExtension]))

for i in range(startingPatientId, finalPatientId):
    outfileFinal= ("".join([outfilePath, str(startingPatientId), outfileExtension]))
    outfileDelete = ("".join([originFileName, str(originFileNumber+1), outfileExtension]))
    # print(outfileDelete)
    def daterange(start_date, end_date):
        for n in range(int((end_date - start_date).days+1)):
            yield start_date + timedelta(n)
    start_date = date(2023, 1, 1)
    end_date = date(2023, 12, 31)

    def testMetrics():
        sideeffects = pd.DataFrame()
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', 500)
        pd.set_option('max_colwidth', 400)
        pd.set_option('display.width', 1000)
        pd.options.display.float_format = '{:.0f}'.format
        for createdAtDate in daterange(start_date, end_date):
            sideeffects.loc[createdAtDate,'patientMetricsId']= int(startingPatientId-1)
            sideeffects.loc[createdAtDate,'patientId']= int(startingPatientId-1)
            sideeffects.loc[createdAtDate,'title']= str(np.random.choice(symptoms))
            sideeffects.loc[createdAtDate,'titlePercent']= int(np.random.randint(1,90))
        return sideeffects

    startingPatientId+=1
    
    effects = testMetrics()
    effectsdf = pd.DataFrame(effects)
    effectsdf.to_excel(outfileFinal, index=False) #enter a path here to save output to xlsx format


    # read the data of excel file you want information from
    df=pd.read_excel(outfileFinal)

    # appending the data of df after the data of the excel file you want the data in
    with pd.ExcelWriter(outfileOriginal,mode="a",engine="openpyxl",if_sheet_exists="overlay") as writer:
        df.to_excel(writer, sheet_name="Sheet1",header=None, startrow=writer.sheets["Sheet1"].max_row,index=False)
    originFileNumber+=1


# ########################################################################################################################################################################
