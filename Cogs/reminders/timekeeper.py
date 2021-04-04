import json
import datetime
import time

import asyncio

def timer():
    print("ready!") 
    while True:
        try: 
            data = load()
        except: 
            pass
        for item in data:
            today = str(datetime.datetime.today()).split(".")[0]
            chid = str(item).split(" ")[2]
            date = str(item).split(" ")[0] + " " + str(item).split(" ")[1]
            if today in date:
                print(data[item])
                del data[item]             
                with open("Cogs/reminders/reminders.json", 'w') as data_file:
                    data = json.dump(data, data_file, sort_keys=True, indent=4)
                break
        time.sleep(0.6)

def load(): 
    with open("Cogs/reminders/reminders.json", "r") as data_file: 
                data = json.load(data_file)
    return data