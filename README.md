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


## Also add  repeating thunder noise to stop bluetooth speaker auto-disconnect

- Add below to: ~/.config/systemd/user/bluetooth_buzz.service

```
[Unit]
Description=Bluetooth Buzz to maintain connection

[Service]
ExecStart=/home/andrew/scripts/hallo_bt.sh
Restart=always
RestartSec=90

[Install]
WantedBy=default.target

```

- And execute below to enable and start on boot:
```
systemctl --user enable bluetooth_buzz.service
systemctl --user start bluetooth_buzz.service
sudo loginctl enable-linger <user>
```
