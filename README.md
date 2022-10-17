
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
```

sudo systemctl add halloween.service
