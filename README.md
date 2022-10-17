
make a halloween.service in /lib/systemd/system/halloween.service

or... if you run into vlc not being run as root issues

make a halloween.service in ~/.config/systemd/user/halloween.service

and execute the below commands:

```
systemctl --user enable halloween.service
systemctl --user start halloween.service
```

And to enable it on boot and not user login
sudo loginctl enable-linger

and verify that an empty user file exists in:
/var/lib/systemd/linger/<user>


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


