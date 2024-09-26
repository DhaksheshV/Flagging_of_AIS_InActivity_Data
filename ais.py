#importing necessary packages
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
#Defining the function
def data():
    ds=pd.read_csv("D:\\Revolution Makers -  NK830\\AIS.csv") #Please change the location of the AIS.csv file
    Training_input_set=ds[['LAT','LON']]
    Training_output_set=ds['Reason']
    classifier=DecisionTreeClassifier()
    classifier.fit(Training_input_set.values,Training_output_set)
    lat=float(input("Enter Latitiude:"))
    lon=float(input("Enter Longitude:"))
    print(classifier.predict([[lat,lon]])[0])
#Checking status of AIS
ais=input("Enter active or inactive : ")
i=0
#Condition for function call
if ais=="inactive":
    i=1
    while(i==1):
        data()
        i=int(input("Enter 1 to run again or any other number to exit : "))
else:
    print("AIS is active")
