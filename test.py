# #generate daily metrics for x patients
from faker import Faker
import numpy as np
from random import randint
import random
import pandas as pd
from faker.providers import BaseProvider
from datetime import date, timedelta
import os

moods = ['happy', 'sad', 'confused', 'frustrated', 'angry', 'tired', 'restless', 'irritable', 'impulsive']

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