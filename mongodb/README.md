```sh
# docker.arvancloud.ir/mongo:7.0.2
docker pull mongo:7.0.2
docker run -d --rm --name some-mongo -p 27017:27017 mongo:7.0.2
docker exec -it some-mongo bash
```

```sh
mongosh
db
show dbs
use database_name
```

```sh
db.createCollection("users")
```

```sh
db.users.insertOne({
  name: "Matin",
  university: "IAU",
  Company: "Quera",
  email: "moeini.imp@gmail.com",
  technologies: ["python", "django"],
  date: Date()
})
```
