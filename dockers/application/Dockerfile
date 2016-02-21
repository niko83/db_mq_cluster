FROM centos:centos7
MAINTAINER niko

RUN yum update -y && yum install -y vim-enhanced sudo && yum clean all

RUN yum install -y gcc postgresql-devel openssl-devel wget make && yum clean all

RUN wget "https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tar.xz" && \
tar xf Python-3.5.1.tar.xz && cd Python-3.5.1 && ./configure && make install  && \
pip3.5 install virtualenv pip -U


EXPOSE 22
EXPOSE 80

RUN yum install -y openssh-server  && yum clean all
ADD sshd_config /etc/ssh/sshd_config

RUN useradd -s /bin/bash app_user
RUN mkdir /home/app_user/.ssh/     
ADD authorized_keys /home/app_user/.ssh/authorized_keys
RUN chmod 600 /home/app_user/.ssh/authorized_keys 
RUN chown app_user:app_user /home/app_user/.ssh/authorized_keys 

RUN ssh-keygen -A
RUN echo 'root:rootroot' | chpasswd
RUN echo 'app_user:app_user' | chpasswd

RUN virtualenv-3.5 --python=python3.5 /venv
ADD packages /venv/packages

RUN /venv/bin/pip install -r /venv/packages

RUN chown app_user:app_user -R /venv

RUN mkdir /data
RUN chown app_user:app_user -R /data

RUN echo "source /venv/bin/activate" >> /home/app_user/.bashrc
RUN echo "cd /data/app" >> /home/app_user/.bashrc

ADD all_commands.sh /all_commands.sh
RUN chown app_user:app_user -R /all_commands.sh && chmod +x /all_commands.sh

CMD /all_commands.sh && /bin/bash
