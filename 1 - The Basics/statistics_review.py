my_list = []
opt = 666



while opt == 666:
    print("Read File -> 0\nWrite To File -> 1\nClear File -> 2")
    opt = int(input("Your Choice >>> "))



if opt == 0:
    with open("C:\\Users\\vampi\\Documents\\GitHub\\sololearn-machine-learning\\1 - The Basics\\alex2206", "r") as list_file:
        temp_list = list_file.read()
    list_file.close()

elif opt == 1:
    numbers_to_append = int(input("Numbers To Append >>> "))
    with open("C:\\Users\\vampi\\Documents\\GitHub\\sololearn-machine-learning\\1 - The Basics\\alex2206", "a") as list_file:
        list_file.write(numbers_to_append)
        temp_list = list_file.read()
    list_file.close()

elif opt == 2:
    with open("C:\\Users\\vampi\\Documents\\GitHub\\sololearn-machine-learning\\1 - The Basics\\alex2206", "w") as list_file:
        list_file.write("")
    list_file.close()



def text_to_list(text):
    final = list(text.split(","))
    return final



temp_list = text_to_list(temp_list)
my_list = [int(x) for x in temp_list]
my_list.sort()
print("{}\n\n".format(my_list))



def mean_and_percentiles():

    # MEAN #

    mean = 0

    for i in my_list:
        mean = mean + i
        #print(i)               # Debugging
    
    mean = mean / len(my_list)

    # PERCENTILES #

    if len(my_list) % 2 != 0:
        temp = int(len(my_list))
        _25th = my_list[int(temp * .25)]
        _50th = my_list[int(temp * .5)]
        _75th = my_list[int(temp * .75)]

        print("(Odd List) Mean Value >>> {:.1f}".format(mean))
        print("(Odd List) 25th Percentile Value >>> {:.0f}".format(_25th))
        print("(Odd List) 50th Percentile Value >>> {:.0f}".format(_50th))
        print("(Odd List) 75th Percentile Value >>> {:.0f}".format(_75th))

    else:
        temp = int(len(my_list) - 1)
        _25th = int(my_list[int(temp * .25)])
        _50th = (int(my_list[int(temp * .5)]) + int(my_list[int(temp * .5) + 1])) / 2
        _75th = int(my_list[int(temp * .75)])

        print("(Even List) Mean Value >>> {:.1f}".format(mean))
        print("(Even List) 25th Percentile Value >>> {:.0f}".format(_25th))
        print("(Even List) 50th Percentile Value >>> {:.1f}".format(_50th))
        print("(Even List) 75th Percentile Value >>> {:.0f}".format(_75th))
        



mean_and_percentiles()