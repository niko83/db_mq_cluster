build:
	sudo docker build --tag psql postgresql;
	sudo docker build --tag mq rabbitmq;
start: 
	sudo docker run -ti -d --hostname=db1 --name=db1 psql;
	sudo docker run -ti -d --hostname=db2 --name=db2 psql;
	sudo docker run -ti -d --hostname=db3 --name=db3 psql;
	sudo docker run -ti -d --hostname=db4 --name=db4 psql;
	sudo docker run -ti -d --hostname=mq1 --name=mq1 mq;
	sudo docker run -ti -d --hostname=mq2 --name=mq2 mq;
	sudo docker run -ti -d --hostname=mq3 --name=mq3 mq;
stop:
	sudo docker rm -f db1 db2 db3 db4 db5 db6 db7 db8 mq1 mq2 mq3;
dns_update:
	sudo ~/update-docker-dns.sh;
	sudo service dnsmasq restart;

