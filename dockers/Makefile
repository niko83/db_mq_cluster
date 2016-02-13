build:
	sudo docker build --tag psql postgresql;
	sudo docker build --tag mq rabbitmq;
	sudo docker build --tag app application;
start: 
	sudo docker run -ti -d --hostname=db1 --name=db1 psql;
	sudo docker run -ti -d --hostname=db2 --name=db2 psql;
	sudo docker run -ti -d --hostname=db3 --name=db3 psql;
	sudo docker run -ti -d --hostname=db4 --name=db4 psql;
	sudo docker run -ti -d --hostname=mq1 --name=mq1 mq;
	sudo docker run -ti -d --hostname=mq2 --name=mq2 mq;
	sudo docker run -ti -d --hostname=mq3 --name=mq3 mq;
	sudo docker run -ti -d --hostname=app1 --name=app1 app;
	sudo docker run -ti -d --hostname=app2 --name=app2 app;
	sudo docker run -ti -d --hostname=app3 --name=app3 app;
	sudo docker run -ti -d --hostname=app4 --name=app4 app;
	sudo docker run -ti -d --hostname=app5 --name=app5 app;
	sudo docker run -ti -d --hostname=app6 --name=app6 app;
	sudo docker run -ti -d --hostname=app7 --name=app7 app;
	sudo docker run -ti -d --hostname=app8 --name=app8 app;
stop:
	sudo docker rm -f db1 db2 db3 db4 db5 db6 db7 db8 mq1 mq2 mq3 app1 app2 app3 app4 app5 app6 app7 app8;
dns_update:
	sudo ~/update-docker-dns.sh;
	sudo service dnsmasq restart;

