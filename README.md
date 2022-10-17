
make a halloween.service in /lib/systemd/system/halloween.service

```
[Unit]
Description=Halloween Stuff
After=multi-user.target

[Service]
Type=simple
ExecStart=/home/andrew/scripts/hallo_exec.sh
Restart=on-abort

[Install]
WantedBy=multi-user.target
```

```
sudo systemctl start halloween.service
sudo systemctl enable halloween.service
```
