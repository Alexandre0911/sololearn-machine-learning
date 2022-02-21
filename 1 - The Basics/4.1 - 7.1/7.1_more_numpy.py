import pandas as pd



df = pd.read_csv('C:\\Users\\vampi\\Documents\\GitHub\\sololearn-machine-learning\\1 - The Basics\\4.1\\titanic.csv')           #! The "df" object is a DataFrame which contains a Titanic DataSet



#! Selecting From Array !#

#myArray = df[['Pclass', 'Fare', 'Age']].values

#print(myArray[0, 1])                    #* To print a specific value of a combined row and column (0 being the row number (1st row), and 1 being the column number (2nd column))
#print(myArray[0])                       #* To print ONLY a specific WHOLE ROW
#print(myArray[:, 2])                    #* To print ONLY a specific WHOLE COLUMN (thus the ":," syntax, makes the program NOT print ANY ROW)



#!  Masking !#

myArray = df[['Pclass', 'Fare', 'Age']].values

mask = myArray[:, 2] < 18                #* This will select the "Age" column and the ARRAY "mask" will be a boolean array (Contains only "True" or "False" values)

#print(mask)                            #* Printing an ARRAY containing the values "True" for any age bellow 18, if it is 18 or bigger, the values should be "False"

#print(myArray[mask])                    #* This will print all the columns of every "True" value. The print being on this format "[Pclass, Fare, Age]"
#print(myArray[myArray[:, 2] < 18])      #* Same as the above, just a 1-line method of doing it

print(mask.sum())                        #* Counts how many "True" values are in the array. "True" = "1" and "False" = "0".
print((myArray[:, 2] < 18).sum())