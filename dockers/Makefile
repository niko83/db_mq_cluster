build:
	sudo docker build --tag psql postgresql;
	sudo docker build --tag mq rabbitmq;
	sudo docker build --tag app application;
start: 
	sudo docker run -ti -d --hostname=db1 --name=db1 psql;
	sudo docker run -ti -d --hostname=db2 --name=db2 psql;
	sudo docker run -ti -d --hostname=mq1 --name=mq1 mq;
	sudo docker run -ti -d --hostname=mq2 --name=mq2 mq;
	# sudo docker run -ti -d --hostname=app1 --name=app1 app;
stop:
	sudo docker rm -f db1 db2 mq1 mq2;
restart:
	# sudo docker rm -f app1;
	# sudo docker run -ti -d --hostname=app1 --name=app1 app;
dns_update:
	sudo ~/update-docker-dns.sh;
	sudo service dnsmasq restart;

