#!/bin/bash

echo -e "\n$(date): BT Buzz-------------------------------" >> /home/andrew/scripts/logs/halloween.service.log

bluetoothctl devices | cut -f2 -d' ' | while read uuid; do bluetoothctl info $uuid; done|grep -e "Device\|Connected\|Name"

/home/andrew/directory_env/hallo/bin/python /home/andrew/scripts/bt_buzz.py >> /home/andrew/scripts/logs/halloween.service.log 2>&1 

