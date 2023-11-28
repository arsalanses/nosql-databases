from elasticsearch import Elasticsearch

ELASTIC_PASSWORD = "FoJYFQz33H6F8wWCB7ZL"

client = Elasticsearch(
    "https://localhost:9200",
    ca_certs="./http_ca.crt",
    basic_auth=("elastic", ELASTIC_PASSWORD)
)

print(client.info())

# Create and Get
# client.indices.create(index="my_index")

# client.index(
#     index="my_index",
#     id="my_document_id",
#     document={
#         "Name": "Abbas",
#         "Age": "27",
#     },
# )

# res = client.get(index="my_index", id="my_document_id")

# print(res)

# Update
# client.update(
#     index="my_index",
#     id="my_document_id",
#     doc={
#         "Name": "Moein",
#         "LastName": "Moeini",
#     },
# )

# client.update(
#     index="my_index",
#     id="my_document_id",
#     script={
#         "source": "ctx._source.remove('LastName')",
#         "lang": "painless"
#     }
# )

# Delete
# client.delete(index="my_index", id="my_document_id")

# client.indices.delete(index="my_index")

result = client.search(index='people', query={
  'match': {
    'name': 'ali'
  }
})

result = client.search(index='people', query={
  'match': {
    'name': {
      'query': 'ali reza',
      'operator': 'and'
    }
  }
})

result = client.search(index='people', query={
  'term': {
    'name': 'ali'
  }
})

result = client.search(index='people', query={
  'range': {
    'age': {
      'gte': 20,
      'lte': 30,
    }
  }
})

result = client.search(index='people', query={
  'bool': {
    'filter': [
      {
        'match': {
          'name': 'ali'
        }
      },
      {
        'range': {
          'age': {
            'gte': 20,
            'lte': 30,
          }
        }
      }
    ]
  }
})

result = client.search(index='people', query={
  'bool': {
    'should': [
      {
        'match': {
          'name': 'ali'
        }
      },
      {
        'range': {
          'age': {
            'gte': 20,
            'lte': 30,
          }
        }
      }
    ]
  }
})

result = client.search(index='people', query={
  'bool': {
    'must_not': [
      {
        'match': {
          'name': 'ali'
        }
      },
      {
        'range': {
          'age': {
            'gte': 20,
            'lte': 30,
          }
        }
      }
    ]
  }
})

result = client.search(index='people', query={
  'bool': {
    'must': [
      {
        'match': {
          'name': 'ali',
          'boost': 1.0
        }
      },
      {
        'match': {
          'name': 'reza',
          'boost': 2.0
        }
      }
    ]
  }
})

result = client.search(index='people', query={
  'bool': {
    'must': [
      {
        'match': {
          'name': 'ali',
          'boost': 1.0
        }
      },
      {
        'match': {
          'name': 'reza',
          'boost': 2.0
        }
      },
      {
        'range': {
          'age': {
            'gte': 20,
            'lte': 30,
            'boost': 3.0
          }
        }
      }
    ],
    'minimum_should_match': 2
  }
})

