build:
	sudo docker build --tag psql postgresql;
	sudo docker build --tag mq rabbitmq;
	sudo docker build --tag app application;
start: 
	sudo docker run -ti -d --hostname=db1 --name=db1 psql;
	sudo docker run -ti -d --hostname=db2 --name=db2 psql;
	sudo docker run -ti -d --hostname=mq1 --name=mq1 mq;
	sudo docker run -ti -d --hostname=mq2 --name=mq2 mq;
	sudo docker run  -ti --hostname=app1 --name=app1 -d -v /home/niko/projects/db_mq_cluster/app/:/data/app app
	sudo docker run  -ti --hostname=app2 --name=app2 -d -v /home/niko/projects/db_mq_cluster/app/:/data/app app
	sudo docker run  -ti --hostname=app3 --name=app3 -d -v /home/niko/projects/db_mq_cluster/app/:/data/app app
	sudo docker run  -ti --hostname=app4 --name=app4 -d -v /home/niko/projects/db_mq_cluster/app/:/data/app app
stop:
	sudo docker rm -f db1 db2 mq1 mq2 app1 app2 app3 app4;
restart:
	sudo docker rm -f app1 app2 app3 app4;
	sudo docker run  -ti --hostname=app1 --name=app1 -d -v /home/niko/projects/db_mq_cluster/app/:/data/app app
	sudo docker run  -ti --hostname=app2 --name=app2 -d -v /home/niko/projects/db_mq_cluster/app/:/data/app app
	sudo docker run  -ti --hostname=app3 --name=app3 -d -v /home/niko/projects/db_mq_cluster/app/:/data/app app
	sudo docker run  -ti --hostname=app4 --name=app4 -d -v /home/niko/projects/db_mq_cluster/app/:/data/app app
dns_update:
	sudo ~/update-docker-dns.sh;
	sudo service dnsmasq restart;

