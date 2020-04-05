
#loading data
import pandas as pd                 # pandas is a dataframe library
import matplotlib.pyplot as plt  


#Reading data from CSV
#This will read the entire file.
df = pd.read_csv("pima-data.csv")


#common things we have to check 
# 1. Not used
# 2. No values
# 3. Duplicates


#finding null values. This will return if there is any null values in the file
#print(df.isnull().values.any())



#Finding corelated coloums. In this matrix we can see the highly co-related with another coloum
#Dark red means highly positivly co-related
# Since this application runs all rows and coloums, the diagnol should have same data. i.e. comparing the features it self.
# The other coloums in red should considered. Because those data is highly co-realeted

#I have comment plot_corr(df) . So make sure to uncomment it
def plot_corr(df, size=55):
    """
    Function plots a graphical correlation matrix for each pair of columns in the dataframe.

    Input:
        df: pandas DataFrame
        size: vertical and horizontal size of the plot

    Displays:
        matrix of correlation between columns.  Blue-cyan-yellow-red-darkred => less to more correlated
                                                0 ------------------>  1
                                                Expect a darkred line running from top left to bottom right
    """

    corr = df.corr()    # data frame correlation function
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr)   # color code the rectangles by correlation value
    plt.xticks(range(len(corr.columns)), corr.columns)  # draw x tick marks
    plt.yticks(range(len(corr.columns)), corr.columns)  # draw y tick marks
    plt.show(fig)

#plot_corr(df)


# Finding the co-relation values 1.0 means highly positivly co-related
#print(df.corr())


# In this case skin and thickness coloums are highly positivly co-related so we have to delete one coloum
# I will delete skin from this
del df['skin']

# Again Finding is there any co-relation values 
print(df.corr())


def plot_corr1(df, size=55):
    """
    Function plots a graphical correlation matrix for each pair of columns in the dataframe.

    Input:
        df: pandas DataFrame
        size: vertical and horizontal size of the plot

    Displays:
        matrix of correlation between columns.  Blue-cyan-yellow-red-darkred => less to more correlated
                                                0 ------------------>  1
                                                Expect a darkred line running from top left to bottom right
    """

    corr = df.corr()    # data frame correlation function
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr)   # color code the rectangles by correlation value
    plt.xticks(range(len(corr.columns)), corr.columns)  # draw x tick marks
    plt.yticks(range(len(corr.columns)), corr.columns)  # draw y tick marks
    plt.show(fig)

#plot_corr1(df)
