#!/bin/bash

echo "\n$(date): BT Buzz-------------------------------" >> /home/andrew/scripts/logs/halloween.service.log 
/home/andrew/directory_env/hallo/bin/python /home/andrew/scripts/bt_buzz.py &>> /home/andrew/scripts/logs/halloween.service.log 

