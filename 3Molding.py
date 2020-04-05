#loading data
import pandas as pd                 # pandas is a dataframe library
import matplotlib.pyplot as plt  


#Reading data from CSV
#This will read the entire file.
df = pd.read_csv("pima-data.csv")

#----------------------------------------------------------------------------------------------

# Converting everything in to numarical values
# in this program  we have true and false values. So we have to convert them in to,

# True as 1
# False as 0

# To perform this activity we have to create a mapping dictionany
dibt_map = {True:1 , False:0}

df['diabetes'] = df['diabetes'].map(dibt_map)
##print(df)

#Check class distribution
num_obs = len(df)
num_true = len(df.loc[df['diabetes'] == 1])
num_false = len(df.loc[df['diabetes'] == 0])
print("Number of True cases:  {0} ({1:2.2f}%)".format(num_true, (num_true/num_obs) * 100))
print("Number of False cases: {0} ({1:2.2f}%)".format(num_false, (num_false/num_obs) * 100))


# As per the above data set we can see there is, 
#   Number of True cases:  268 (34.90%)
#   Number of False cases: 500 (65.10%)
# are available. So we can train our training modle from the data we have
# *Note - If there is a highly variation like 95%:5% values are available, then we are unable to preform the activity

