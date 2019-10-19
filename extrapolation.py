#!/usr/bin/env python3

import csv
import sys

def get_data_set_by_id(idContractor):
    val_set = {}
    with open('out.txt', mode='r') as csv_file:
        csv_data = csv.DictReader(csv_file)
        for row in csv_data:
            if row["id"] == idContractor:
                val_set = {
                    5:float(row["5_units"]),
                    50:float(row["50_units"]),
                    500:float(row["500_units"]),
                    5000:float(row["5000_units"]),
                    50000:float(row["50000_units"])
                }
    return val_set

def extrapolate(x, x_inf, y_inf, x_sup, y_sup):
    res = y_inf+(((x-x_inf)/(x_sup-x_inf))*(y_sup-y_inf))
    return round(res,2)

#1 Ask for the contractor id
idContractor = str(sys.argv[1])
#2 Ask for the number of units to quote. 
units = float(str(sys.argv[2]))
#3 Extract the contractor base dataset to perform the estimation, using the csv file as a source.
val_set = get_data_set_by_id(idContractor)
print("For contractor with id ", idContractor, " and current quoting values ",val_set)
#4 Detect to what range of units belongs the input value.
#5 Perform the extrapolation formula.
#6 Show the result to the user.
print("The value of ",units," units is: ")
if 5<=units<=50:
    print(extrapolate(units,5,val_set[5],50,val_set[50]))
elif 50<units<=500:
    print(extrapolate(units,50,val_set[50],500,val_set[500]))
elif 500<units<=5000:
    print(extrapolate(units,500,val_set[500],5000,val_set[5000]))
elif 5000<units<=50000:
    print(extrapolate(units,5000,val_set[5000],50000,val_set[50000]))
else:
    print("The value is out of the range")