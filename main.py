from ftplib import FTP
from typing import List
from transform import get_event
from ftp import download_logs


ftp = FTP("168.119.28.33")

welcomeMessage = ftp.getwelcome()

print(welcomeMessage)

respMessage = ftp.login("", "")

print(respMessage)

print("Connected to ftp server")


downloaded_files = download_logs("/plugins/SuperLog/logs/players/", ftp)
events = []
for i in range(len(downloaded_files))
    with open(downloaded_files[i], "r") as file:
        lines = file.read().split("\n")

    for n in range(len(lines) - 1):
        events.append(get_event(lines[n]))
        print(get_event(lines[n]))

print(events)



#with open('downloads/01-09-20_InventoryEvents-SuperLog.log', 'wb') as fp:
#    ftp.retrbinary('RETR 01-09-20_InventoryEvents-SuperLog.log', fp.write)
