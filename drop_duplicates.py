import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def dropDuplicates():

    df= pd.read_csv(os.getenv('DATAFRAME1'))

    print(df)

    dfuniq = df.drop_duplicates()

    print(dfuniq)

    dfuniq.to_csv('DATAFRAME2')
