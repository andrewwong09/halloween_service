#!/bin/bash

echo "$(date)---------------------------------------" >> /home/andrew/scripts/logs/halloween.service.log 
/home/andrew/directory_env/hallo/bin/python /home/andrew/scripts/hello_world.py &>> /home/andrew/scripts/logs/halloween.service.log 
