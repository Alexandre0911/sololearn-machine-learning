import pandas as pd
pd.options.display.max_columns = 6         #? Option to make pandas display a max number of 6 columns



df = pd.read_csv('C:\\Users\\vampi\\Documents\\GitHub\\sololearn-machine-learning\\1 - The Basics\\4.1\\titanic.csv')           #! The "df" object is a DataFrame which contains a Titanic DataSet



print(df.head())            #! head() function returns first 5 rows of a DataFrame
print(df.describe())            #! describe() function returns a table of statistics about the columns of our DataFrame



#! You should uncomment or comment whatever you want or not to be run!