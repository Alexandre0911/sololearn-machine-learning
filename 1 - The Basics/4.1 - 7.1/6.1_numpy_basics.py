import pandas as pd



df = pd.read_csv('C:\\Users\\vampi\\Documents\\GitHub\\sololearn-machine-learning\\1 - The Basics\\4.1 - 7.1\\titanic.csv')           #! The "df" object is a DataFrame which contains a Titanic DataSet



fareValues = df['Fare'].values                                      #* 1-dimensional numpy array

myArrayOfValues = df[['Pclass', 'Fare', 'Age']].values              #* 2-dimensional numpy array
print(myArrayOfValues.shape)                                        #* This tells me how many rows and columns, respectively, the array has