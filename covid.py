  
'''
This is a Coronavirus Tracker program written by Swastik.
You have to connect to internet and the run this program.
If the program will run succesfully, it will show the name of a file and its location.
In that file, all the data about different countries like no. of cases, deaths etc will be written in formatted way.
Please try running this program on desktop.
'''


import requests
import json

import json
import os


try:
    my_data=requests.get("https://api.covid19api.com/summary")

except:
    print("Please connect to Internet and try again.")

else:
    
    datastr=my_data.text

    data=json.loads(datastr)

    Global=data["Global"]
    Countries=data["Countries"]
    Date=data["Date"]
    date=Date.replace(Date[-1],"")
    date_list=date.split("T")
    data_date=date_list[0]
    data_time=date_list[1]

    filename="Coronavirus_cases_data.txt"
    write_data=""
    s_no=0
    write_data+=("This data is last updated at - "+"\nDate - "+data_date+"\nTime - "+data_time+"\n\n\n")
    write_data+=("Total Cases Worldwide -\n"+"Confirmed - "+str(Global['TotalConfirmed'])+"\n"+"Recovered - "+str(Global['TotalRecovered'])+"\n"+"Deaths - "+str(Global['TotalDeaths'])+"\n\n")
    write_data+=("\nThese the cases countrywise - \n\n")
    for c in Countries:
        s_no+=1
        spaces=(len(str(s_no))*" ")+"  "
        write_data+=str(s_no)+". Country - "+str(c['Country'])+"\n"+spaces+"Confirmed - "+str(c['TotalConfirmed'])+"\n"+spaces+"Recovered - "+str(c['TotalRecovered'])+"\n"+spaces+"Deaths - "+str(c['TotalDeaths'])+"\n\n"

    with open(filename,"w") as f_obj:
        f_obj.write(write_data)
        print(f"Your file '{filename}' is created/updated at '{os.getcwd()}'.")