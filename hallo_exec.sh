#!/bin/bash

echo -e "\n$(date) Hallo World----------------------------" >> /home/andrew/scripts/logs/halloween.service.log 
/home/andrew/directory_env/hallo/bin/python /home/andrew/scripts/hallo_world.py >> /home/andrew/scripts/logs/halloween.service.log 2>&1

