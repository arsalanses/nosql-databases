```sh
docker pull neo4j:5.13.0
docker run --rm -d --name neo4 --restart always --publish=7474:7474 --publish=7687:7687 --env NEO4J_AUTH=neo4j/your_password neo4j:5.13.0
docker exec -it neo4 cypher-shell
docker exec -i neo4 cypher-shell < test.txt
```

```
https://console.neo4j.io/
https://neo4j.com/download/
```

```sh
CREATE (p:Person {name:"Matin"});
CREATE (c:Company {name:"Quera"});
# (first_node)-[:relation_lable]->(second_node)
CREATE (p)-[:WORKED_AT]->(c);
```

```sh
MERGE (p:Person {name:"mohammad"});
MERGE (p:Person {name:"Matin"});
MERGE (p:Person {name:"MohammadAli"});
```

```sh
MERGE (p:Person);
RETURN (p);

MATCH v=(d:Developer)-[]->() RETURN v;
```
