import requests #Module for handing the request to the API
import json #For parsing the JSON response from the server
from subprocess import Popen
import datetime as dt


try:
    res = requests.get("http://worldtimeapi.org/api/ip")
    data = res.text #Gets the results from the API
    datetime =  json.loads(data)['datetime'];
    time = dt.datetime.fromisoformat(datetime).strftime("%H:%M:%S")

    print(time)

    Popen(['time',time],shell = True) #Executes the command and sets your computer's time
except requests.exceptions.ConnectionError:
    #This code is executed incase there is a connection error.
    print("Connection error,try again")

finally:

    while True:
        pass
    