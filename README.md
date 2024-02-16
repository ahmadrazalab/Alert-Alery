# What is this and How this works
This is a very simple alert mechanism which is written in python 
This works with cron and smtp mail to send the alert message when certain thresholds are reached 
In this example i have set "cpu/ram/diskusge" for alert purposes you can modify this as per your needs


# Prerequicites
```
apt-get update
apt-get install -y python3 python3-pip
pip3 install psutil
```

# add the smtp creds alery python script in usr dir
```
/usr/local/bin/ssh-login
```

# update the cron timing in the etc cron dir 
```
/etc/cron.weekly/ssh_login_cron
```

# build the package 
```
dpkg-deb --build sshd-alert
```

# and install the package
```
dpkg -i sshd-alert.deb
```

# how to use in cmd line mode (manual)
```
python3 ssh-login
python3 /usr/local/bin/ssh-login
```
