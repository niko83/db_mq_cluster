cat /data/app/docker-container-hosts >> /etc/hosts;
/bin/bash -c "/venv/bin/python /data/app/service3.py &>> /data/app/logs/service.log &"
# 
# && /usr/sbin/sshd
