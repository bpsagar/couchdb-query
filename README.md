# couchdb-query
A minimal python wrapper for querying Apache CouchDB

## Usage
```
import couchdbquery
results = couchdbquery.query(db, **params)
```

## Query parameters
Operator | Suffix | Example
--- | --- | ---
== | eq | name__eq='John'
!= | neq | name__neq='John'
< | lt | age__lt=20
<= | lte | age__lte=20
> | gt | age__gt=20
>= | gte | age__gte=20
