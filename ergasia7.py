import urllib.request
import json
import datetime
import requests
import numpy as np
from datetime import datetime

date_day = datetime.now().day #παίρνει την ημερομηνία την σημερινή ημερομηνία
date_now = datetime.now()
#print(date_now)
str_time=date_now.strftime("%H:%M:%S") #convering time into a string
str_month_year = date_now.strftime("%Y-%m")
#print(str_month_year)
print("Το πρόγραμμα έχει αρχίσει. Τα αποτελέσματα είναι μέχρι την ώρα: "+str_time+"\n")

for i in range(date_day): #επανάληψη για να τρέξει το πρόγραμμα μέχρι την μέρα που εκτελείται το πρόγραμμα
    str_i = str(i+1) #i was an integer,starting from 0
    if i<9:
        str_i="0"+str_i #adding 0 in front of the number (in order to match the requested form of date )
    str_date = str_month_year + "-" + str_i #fixing the date
    #str_date = "2021-02" + "-" + str_i

    #print(str_date)
    url1 ="https://api.opap.gr/draws/v3.0/1100/draw-date/"+str_date + "/" +str_date + "/draw-id" #taking the ids of todays draws

    r=urllib.request.urlopen(url1)
    html=r.read()
    html=html.decode() #convert bytes into string
    #print(html)

    ids = html.replace('[','')
    ids = ids.replace(']','')
    ids_list =list(map(int, ids.split(','))) #convert ids into a list
    #print(ids_list)

    def listmaker(n):
        listofzeros = [0] * n
        return listofzeros

    table = listmaker(80) #set empty table of 80 zeros
    #print(table)

    for id in ids_list:
        id_str = str(id)
        url_id = "https://api.opap.gr/draws/v3.0/1100/" + id_str #taking data of todays draws(oles tis klrhrwseis)
        r1=urllib.request.urlopen(url_id)
        html1=r1.read()
        html1=html1.decode() #convert bytes into string
        data=json.loads(html1)

        x = data["winningNumbers"].get('list') #taking the values of the list

        #x.sort() #κατά αύξουσα σειρά
        #print(x)
        for number in x:
            #print(number) #τυπώνει κάθετα τους αριθμόυς
            table[number-1] = table[number-1]+1 #adding 1 in the right place of the table,when the corresponding number is displayed

        #print(table)

        table_array = np.array(table) #using np to change table into a tupple
        maximum = np.where(table_array==max(table)) #taking the maximum values

        maximum_list = list(maximum[0]) #converting tupple into a list

        maximum_list = [item+1 for item in maximum_list] #table starts from 0 to 79
        #print(type(maximum_list))
    #print(table)

    print("Την ημερομηνία "+str_date+ " οι πιο συχνά εμφανιζόμενοι αριθμοί είναι:",maximum_list)
    print("\n")
