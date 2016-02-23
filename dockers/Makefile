build:
	sudo docker build --tag psql postgresql;
	sudo docker build --tag mq rabbitmq;
	sudo docker build --tag app application;
	sudo docker build --tag lb nginx;
start: 
	sudo docker run -ti -d --hostname=db1 --name=db1 psql;
	sudo docker run -ti -d --hostname=db2 --name=db2 psql;
	sudo docker run -ti -d --hostname=mq1 --name=mq1 mq;
	# sudo docker run -ti -d --hostname=mq2 --name=mq2 mq;
	sudo ~/update-docker-dns.sh;
	cp /docker-container-hosts ../app/docker-container-hosts
	sleep 8;
	sudo docker run -ti -d --cpuset="0" --hostname=app1 --name=app1 -v /home/niko/projects/db_mq_cluster/app/:/data/app app
	sudo docker run -ti -d --cpuset="1" --hostname=app2 --name=app2 -v /home/niko/projects/db_mq_cluster/app/:/data/app app
	sudo docker run -ti -d --cpuset="2" --hostname=app3 --name=app3 -v /home/niko/projects/db_mq_cluster/app/:/data/app app
	sudo docker run -ti -d --cpuset="3" --hostname=app4 --name=app4 -v /home/niko/projects/db_mq_cluster/app/:/data/app app
	sudo ~/update-docker-dns.sh;
	cp /docker-container-hosts ../app/docker-container-hosts
	sudo docker run -ti -d --hostname=lb -v /home/niko/projects/db_mq_cluster/app/:/data/app --name=lb lb;
stop:
	sudo docker rm -f db1 db2 mq1 mq2 app1 app2 app3 app4 lb;
restart:
	sudo docker rm -f app1 app2 app3 app4;
	sudo docker run  -ti --hostname=app1 --name=app1 -d -v /home/niko/projects/db_mq_cluster/app/:/data/app app
	sudo docker run  -ti --hostname=app2 --name=app2 -d -v /home/niko/projects/db_mq_cluster/app/:/data/app app
	sudo docker run  -ti --hostname=app3 --name=app3 -d -v /home/niko/projects/db_mq_cluster/app/:/data/app app
	sudo docker run  -ti --hostname=app4 --name=app4 -d -v /home/niko/projects/db_mq_cluster/app/:/data/app app
dns_update:
	sudo ~/update-docker-dns.sh;
	sudo service dnsmasq restart;
hard_reset:
	make stop; make build; make start; make dns_update;

