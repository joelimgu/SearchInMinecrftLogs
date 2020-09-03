# Search In Minecraft Logs

It downloads the logs from players from super log pluggin in minecraft and stores them in a dictionary to search what players accessed an inventory

The superlog pluggin must be configured with the following event:

```  
InventoryOpenEvent:
      enabled: true
      message: '{PLAYER.NAME} opened {TYPE} (x: {LOCX},y: {LOCY},z: {LOCZ}) on {LOCWORLD}'
```


and gzip logs should be disabled:
```
gzip-logs-after: 0
```

to download the files you must ccreate a file named: **credentials.json** and add this inside:
```
{
  "ip": "your FTP ip",
  "username": "your FTP Username",
  "password": "your FTP Password"
}
```