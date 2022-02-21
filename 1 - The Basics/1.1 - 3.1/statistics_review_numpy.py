import numpy as np
from math import *



my_list = []
opt = 666



while opt == 666:
    print("Read File -> 0\nWrite To File -> 1\nClear File -> 2")
    opt = int(input("Your Choice >>> "))



if opt == 0:
    with open("C:\\Users\\vampi\\Documents\\GitHub\\sololearn-machine-learning\\1 - The Basics\\1.1 - 3.1\\data.txt", "r") as list_file:
        temp_list = list_file.read()
    list_file.close()

elif opt == 1:
    numbers_to_append = int(input("Numbers To Append >>> "))
    with open("C:\\Users\\vampi\\Documents\\GitHub\\sololearn-machine-learning\\1 - The Basics\\1.1 - 3.1\\data.txt", "a") as list_file:
        list_file.write(numbers_to_append)
        temp_list = list_file.read()
    list_file.close()

elif opt == 2:
    with open("C:\\Users\\vampi\\Documents\\GitHub\\sololearn-machine-learning\\1 - The Basics\\1.1 - 3.1\\data.txt", "w") as list_file:
        list_file.write("")
    list_file.close()



def text_to_list(text):
    final = list(text.split(", "))
    return final



temp_list = text_to_list(temp_list)
my_list = [int(x) for x in temp_list]
my_list.sort()
print("{}\n\n".format(my_list))



def mean_and_percentiles():
    print("Mean Value >>> {:.2f}".format(np.mean(my_list)))
    print("25th Percentile Value >>> {:.2f}".format(np.percentile(my_list, 25)))
    print("50th Percentile Value >>> {:.2f}".format(np.percentile(my_list, 50)))        #? The same as " print("50th Percentile Value >>> {:.2f}".format(np.median(my_list)) " #
    print("75th Percentile Value >>> {:.2f}".format(np.percentile(my_list, 75)))
    print("Variance Value >>> {:.2f}".format(np.var(my_list)))
    print("Standard Deviation Value >>> {:.2f}".format(np.std(my_list)))



mean_and_percentiles()