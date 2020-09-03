import json
from ftplib import FTP
from typing import List
from transform import get_event
from ftp import download_logs


with open("credentials.json", "r") as file:
    credentials = json.loads(file.read())
try:
    ftp = FTP(credentials["ip"])

    welcomeMessage = ftp.getwelcome()

    print(welcomeMessage)

    respMessage = ftp.login(credentials["username"], credentials["password"])

    print(respMessage)

    print("Connected to ftp server")
except:
    print("an error has occurred with the ftp")


downloaded_files = download_logs("/plugins/SuperLog/logs/players/", ftp)
events = []
for i in range(len(downloaded_files)):
    with open(downloaded_files[i], "r") as file:
        try:
            lines = file.read().split("\n")
        except:
            print("error splitting file")
    for n in range(len(lines) - 1):
        try:
            events.append(get_event(lines[n]))
        except:
            pass
        print(get_event(lines[n]))

print(events)

# {'x': -70, 'y': 75, 'z': -54}
#events = [{'time': {'hours': '07', 'minutes': '33'}, 'player': 'pou', 'inventoryType': 'WORKBENCH', 'coordinates': {'x': -101, 'y': 75, 'z': -192}, 'dimension': 'world'}]

#print(events[0].get('player'))


for i in range(len(events)):
    try:
        if events[i]["coordinates"]["x"] == -101 and events[i]["coordinates"]["y"] == 75 and events[i]["coordinates"]["z"] == -192:
            print("found event: %s" % events[i])
    except TypeError:
        pass
