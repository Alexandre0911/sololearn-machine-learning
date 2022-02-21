import pandas as pd



df = pd.read_csv('C:\\Users\\vampi\\Documents\\GitHub\\sololearn-machine-learning\\1 - The Basics\\4.1\\titanic.csv')



col = df['Fare']          #* To select a single column, we use the square brackets and the column name.
print(col)