#!/bin/bash

echo -e "\n$(date) Hallo World----------------------------" >> /home/andrew/scripts/logs/halloween.service.log

sleep 10

bluetoothctl connect F4:4E:FD:52:5C:A9 >> /home/andrew/scripts/logs/halloween.service.log 2>&1

/home/andrew/directory_env/hallo/bin/python /home/andrew/scripts/hallo_world.py >> /home/andrew/scripts/logs/halloween.service.log 2>&1

