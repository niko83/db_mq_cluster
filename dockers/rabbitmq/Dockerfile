FROM centos:centos6
MAINTAINER niko
EXPOSE 5672 15672
RUN yum update -y && yum install -y vim-enhanced sudo && yum clean all

RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm \
 && yum install -y rabbitmq-server \
 && yum clean all

ADD bin/rabbitmq-start /usr/local/bin/
RUN chmod +x /usr/local/bin/rabbitmq-start

CMD ["rabbitmq-start"]
