```sh
docker pull neo4j:5.13.0
docker run --rm -d --name neo4 -p7474:7474 -p7687:7687 --env NEO4J_AUTH=neo4j/your_password neo4j:5.13.0
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
CREATE (d1:Developer {name:"Ali"})
CREATE (d2:Developer {name:"Matin"})
CREATE (d3:Developer {name:"Moein"})
CREATE (d1)-[:LEADS]->(d2)
CREATE (d2)-[:LEADS]->(d3);
MATCH v=(d:Developer)-[]->() RETURN v;
```
