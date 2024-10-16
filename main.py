import pandas as pd
import os

from dotenv import load_dotenv
from drop_duplicates import dropDuplicates

load_dotenv()

dropDuplicates

viasinalizacao = pd.read_csv(os.getenv('DATAFRAME2'))
multimodal = pd.read_csv(os.getenv('DATAFRAME3'))

dfcompare = pd.merge(
    viasinalizacao, 
    multimodal,
    how='inner',
    left_on=['VIASINALIZACAO'],
    right_on=['MULTIMODAL']
)

print(dfcompare)

dfcompare.to_csv('DATAFRAME4.csv')
