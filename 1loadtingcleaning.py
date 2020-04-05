#loading data
import pandas as pd                 # pandas is a dataframe library


#Reading data from CSV
#This will read the entire file.
df = pd.read_csv("pima-data.csv")
#print(df)

#finding the number of rows and coloums. This is not mandatory if we are printing above statement.
#print(df.shape)

#finding top 5 rows
#(df.head(5))

#finding the bottom 5 rows
#print(df.tail(5))



