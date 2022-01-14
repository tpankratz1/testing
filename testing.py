# This is a test file
# This file was changed on GitHub. Testing pull.

import csv
import os
def samplefunction(a = 5, b = 7, myvalue1 = 6, myvalue2 = 6 , j = 6):
    g = a + b
    print(f" calculated value g is {g} ")
    k = 4
    x = "y"
    while x == "y":
        p = 5
        l = 3
        k = p*k/10**p - l
        print(f" k value is {k}")
        if myvalue2 == myvalue1:
            for x in list(range(5)):
                print(x)
                word = "peace"
                for k in word:
                    print(k)
        elif j*myvalue1 == 36:
            accounting_df = os.read_csv("accounting.csv")
            print(accounting_df.head())
        else:
            mylist2 = list(range(77,88))
            for x in mylist2:
                print(x)
        x = input("enter y or n")

samplefunction(a = 5, b = 7, myvalue1 = 6, myvalue2 = 6 , j = 6)
