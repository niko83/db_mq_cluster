cat /data/app/docker-container-hosts >> /etc/hosts;
/bin/bash -c "/venv/bin/python /data/app/service.py &>> /data/app/service.log &" &&
/usr/sbin/sshd
