make a halloween.service in ~/.config/systemd/user/halloween.service

and execute the below commands:

```
systemctl --user enable halloween.service
systemctl --user start halloween.service
```

And to enable it on boot and not user login
```
sudo loginctl enable-linger <user>
```
and verify that an empty user file exists in:
/var/lib/systemd/linger/<user>

halloween.service
```
[Unit]
Description=Halloween Stuff

[Service]
ExecStart=/home/andrew/scripts/hallo_exec.sh
Restart=always

[Install]
WantedBy=default.target

```

