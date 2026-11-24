import pandas as pd

coviddf = pd.read_csv('DataVisiulization/Covid19Info.csv')
print(coviddf.head(5))
totalcasesinindia = coviddf['Total Cases'].sum()
print(
  'Total number of cases in India:', totalcasesinindia
)
deathratio = coviddf[(coviddf['Death Ratio']>1 )& (coviddf['Population']>4000000)]['State/UTs']
print(
  'States with death ration > 1.0 and population > 4000000:', deathratio.tolist()
)
print('Descriptive statictics:')
print(coviddf.describe())
print('Data types of each column:')
print(coviddf.info())