FROM debian:jessie

MAINTAINER NGINX Docker Maintainers "docker-maint@nginx.com"

ENV NGINX_VERSION 1.9.11-1~jessie

RUN apt-key adv --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62 \
    && echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y vim ca-certificates nginx=${NGINX_VERSION} gettext-base \
    && rm -rf /var/lib/apt/lists/*

## forward request and error logs to docker log collector
RUN ln -sf /data/app/logs/nginx_lb_access.log /var/log/nginx/access.log \
    && ln -sf /data/app/logs/nginx_lb_error.log /var/log/nginx/error.log
 
ADD lb.conf /etc/nginx/conf.d/lb.conf

RUN mkdir /data

EXPOSE 80 443

CMD cat /data/app/docker-container-hosts >> /etc/hosts && etc/init.d/nginx start && /bin/bash

