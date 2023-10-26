#Use the Salaries.csv file calculate:
#What is the ratio between people in the fire department over people in the police department

import pandas as pd

#Create a bool column for POLICE and FIREDEPT
#use str.contains to find a partial match. 
#This cannot be used in a lambda function because searching a single column is seen as a data series rather than a data frame. And str.contains() cannot work on a data series. 

df["POLICE"] = df["JobTitle"].str.contains("POLICE", case=False, na=False)
df["FIREDEPT"] = df["JobTitle"].str.contains("FIRE DEP", case=False, na=False)


#To count bool True values: 
df["POLICE"].sum()

#Use ~df for the False values: 
~df["POLICE"].sum()

#Calculate the ratio: 
ratio_police_to_firedept = (df["POLICE"].sum())/((df["FIREDEPT"]).sum())

#Calculate the base salary for each profession: 

#Bool True and False equates to 1 and 0 values. So we can multiply the BasePay by the bool column. 
df.loc[:,"POLICE"] = df.loc[:,"POLICE"].mul(df["BasePay"])


#sum() counts the number of occurrences. 
#The first part of the expression adds up the total salaries
#The second part counts the number of rows with a salary (ie number of POLICE)
df.POLICE.sum() / (df.POLICE > 1).sum()

df.FIREDEPT.sum() / (df.FIREDEPT > 1).sum()
