# #generate daily metrics for x patients
from faker import Faker
import numpy as np
from random import randint
import random
import pandas as pd
from faker.providers import BaseProvider
from datetime import date, timedelta
import os

symptoms = ['insomnia', 'lack of appetite', 'irritability', 'impulsivity', 'weight gain', 'inactivity', 'hyperactivity']



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

