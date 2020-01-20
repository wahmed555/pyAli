import numpy as np
import pandas as pd

# Read the cont ents of the file including the State (Area in Column 1, beginning in Row 4} and the census 1990 and 2000 (Columns Band C beginning at Row 5).
# Reading the file
df0=pd.read_excel('Attachment_1572378335-1.xlsx',skiprows=3)

# Write this data to a new workbook named panda_census_data.xlsx on a new worksheet named 'Census
# saving the data to a new file

df0.to_excel('panda_census_data.xlsx', sheet_name='Cencus')


# Create a new worksheet named 'PopulationChangeRecords'. Find the following information among all areas (includes SO states plus the District of Columbia}
# Find the area with the highest change in population.
# Find the area with the lowest change in population.
# Find the average change in population among all areas.
# Write those findings, including the area and the amount, to the table as shown in Figure 3.
# copying only the relevant rows in new dataframe
df1=df0.iloc[:51,:].copy()
# df1

# finding the change

df1['Change_in_population']=df1['Total 2000']-df1['Total 1990']
# df1
df2=df1.sort_values('Change_in_population', ascending= False)
# df2

# the state with the highest change in population

df2.iloc[0]['Area'].strip()

# the highest change in population

df2.iloc[0]['Change_in_population']

# State of Lowest change in Population

df2.iloc[-1]['Area'].strip()

#  Lowest change in population state

df2.iloc[-1]['Change_in_population']


# averge change in Population

df2['Change_in_population'].mean()


## Making a new Dataframe
data = [['Highest Change in Population', 'California', 4111627.0], ['Lowest Change in Population', 'District of Columbia', -34841.0], ['Averge Change in Population', np.NaN, 641412.41]] 

df_= pd.DataFrame(data,index=[1,2,3], columns=['item','state','record'])
# df_ = df_.fillna(0) # with 0s rather than NaNs
# df_

# Saving a excel file with 2nd sheet
from openpyxl import load_workbook

with pd.ExcelWriter('panda_census_data.xlsx') as writer:  # doctest: +SKIP
    df0.to_excel(writer, sheet_name='Cencus')
    df_.to_excel(writer, sheet_name='PopulationChangeRecords')