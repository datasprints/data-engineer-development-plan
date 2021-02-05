## Pull and run ElasticSearch
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.10.2
docker run --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -d docker.elastic.co/elasticsearch/elasticsearch:7.10.2

## Pull and run Kibana
docker pull docker.elastic.co/kibana/kibana:7.10.2
docker run --name kibana --link elasticsearch:elasticsearch -p 5601:5601 -d docker.elastic.co/kibana/kibana:7.10.2