from cgitb import small
import pandas as pd



df = pd.read_csv('C:\\Users\\vampi\\Documents\\GitHub\\sololearn-machine-learning\\1 - The Basics\\4.1 - 7.1\\titanic.csv')           #! The "df" object is a DataFrame which contains a Titanic DataSet



#col = df['Fare']          #* To select a single column, we use the square brackets and the column name.
#print(col)



#small_df = df[['Age', 'Sex', 'Survived']]          #? This makes the program print out only the selected columns
#print(small_df.head())



df['isMale'] = df['Sex'] == 'male'
print(df.head())