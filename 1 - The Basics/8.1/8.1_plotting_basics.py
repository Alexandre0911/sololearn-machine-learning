import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('C:\\Users\\vampi\\Documents\\GitHub\\sololearn-machine-learning\\1 - The Basics\\4.1 - 7.1\\titanic.csv')           #! The "df" object is a DataFrame which contains a Titanic DataSet



plt.xlabel('Age')                                       #* Labels X-Axis as "Age".
plt.ylabel('Fare')                                      #* Labels Y-Axis as "Fare".

#plt.scatter(df['Age'], df['Fare'])                      #* Plots our data. 1st argument ("Age" on this code) is the X-Axis. 2nd argument ("Fare" on this code) is the Y-Axis.
plt.scatter(df['Age'], df['Fare'], c=df['Pclass'])      #* Same as the above, but with colors because of the "Pclass" column which contains 3 possible values. 1st class, 2nd class and 3rd class, each having a different color overlaying "Fare" and "Age".
                                                        #* Purple dots are 1st class, green dots are 2nd class and yellow dots are 3rd class.
                                                        
plt.plot([0,80], [85, 5])                               #* [0, 80] x1=0, x2=80 (Line Length Coordinates). [85, 5] y1=85, y2=5 (Line Inclination Coordinates).
                                                        #* This will draw a line that goes from the point (0, 85) to the point (80, 5).



plt.show()                                              #* Opens secondary window with plot