```txt
# docker.arvancloud.ir/mongo:7.0.2
docker pull mongo:7.0.2
docker run -d --rm --name some-mongo -p 27017:27017 mongo:7.0.2
docker exec -it some-mongo bash
docker exec -i some-mongo mongosh --quiet < mongo.js
```

```txt
mongosh
db
show dbs
use database_name
```

```txt
db.createCollection("users")
```

```txt
db.users.insertOne({
  name: "Matin",
  university: "IAU",
  Company: "Quera",
  email: "moeini.imp@gmail.com",
  technologies: ["python", "django"],
  date: Date()
})
```

```txt
db.users.insertMany([ 
{
  name: "Moein",
  university: "HNU",
  Company: "Quera",
  email: "moein@gmail.com",
  technologies: ["php", "laravel"],
  date: Date()
},
{
  name: "younes",
  university: "SU",
  Company: "Quera",
  email: "youness@gmail.com",
  technologies: ["php", "laravel","GO","SQL"],
  date: Date()
} 
])
```

```txt
db.users.find({name:"Moein"})
```

```txt
db.users.find({age: { $eq: 20}})

db.users.find({age: { $gt: 24}})
db.users.find({age: {$lt: 22}})
# $ne, $gte, $lte, $in
```

```txt
db.users.find({$and: [{name: "matin"}, {age: {$gt: 24}}] })
db.users.find({$or: [{name: "matin"}, {name: "ali"}]})
db.users.find({$nor: [{name: "matin"}, {name: "moein"}]})
```

```txt
db.users.updateone({name:"Moein"},{$set :{technologies:["python","php","laravel"]}})
db.techs.updateMany(
    {langs: {$in: ['python']}},
    {
        $set: {
            langs: ['python'],
            version: '3.12.0',
            usage: ['backend', 'AI', 'DataAnalytics']
        }
    },
    {upsert: true}
)
```

```txt
db.users.deleteOne({name:"Matin"})
db.users.deleteMany({technologies:"php"})
```

