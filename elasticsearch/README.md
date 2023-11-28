```sh
docker network create elastic
sudo sysctl -w vm.max_map_count=262144
# docker.arvancloud.ir/
docker pull elasticsearch:8.11.1
docker run -d --rm --name es01 --net elastic -p 9200:9200 -it -m 1GB elasticsearch:8.11.1
docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic

docker cp es01:/usr/share/elasticsearch/config/certs/http_ca.crt .
curl --cacert http_ca.crt -u elastic:$ELASTIC_PASSWORD https://localhost:9200
```

