# Repo

## Query

```graphql
query topics {
  topics {
    edges {
      node {
        comments(last: 1) {
          edges {
            node {
              id
            }
          }
        }
      }
    }
  }
}
```

## Error

```log
GraphQL request:2:3
1 | query topics {
2 |   topics {
  |   ^
3 |     edges {
Traceback (most recent call last):
  File ".venv\Lib\site-packages\graphql\execution\execute.py", line 521, in execute_field
    result = resolve_fn(source, info, **args)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".venv\Lib\site-packages\strawberry_django\optimizer.py", line 1092, in resolve
    ret = _next(root, info, *args, **kwargs)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".venv\Lib\site-packages\strawberry\schema\schema_converter.py", line 740, in _resolver
    return _get_result_with_extensions(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".venv\Lib\site-packages\strawberry\schema\schema_converter.py", line 727, in extension_resolver
    return reduce(
           ^^^^^^^
  File ".venv\Lib\site-packages\strawberry_django\fields\field.py", line 401, in resolve
    return self.connection_type.resolve_connection(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".venv\Lib\site-packages\strawberry_django\relay.py", line 128, in resolve_connection
    conn = super().resolve_connection(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".venv\Lib\site-packages\strawberry\relay\types.py", line 922, in resolve_connection
    for i, v in enumerate(iterator)
                ^^^^^^^^^^^^^^^^^^^
  File ".venv\Lib\site-packages\django\db\models\query.py", line 400, in __iter__
    self._fetch_all()
  File ".venv\Lib\site-packages\django\db\models\query.py", line 1930, in _fetch_all
    self._prefetch_related_objects()
  File ".venv\Lib\site-packages\django\db\models\query.py", line 1320, in _prefetch_related_objects
    prefetch_related_objects(self._result_cache, *self._prefetch_related_lookups)
  File ".venv\Lib\site-packages\django\db\models\query.py", line 2381, in prefetch_related_objects
    obj_list, additional_lookups = prefetch_one_level(
                                   ^^^^^^^^^^^^^^^^^^^
  File ".venv\Lib\site-packages\django\db\models\query.py", line 2545, in prefetch_one_level
    ) = prefetcher.get_prefetch_querysets(
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".venv\Lib\site-packages\django\db\models\fields\related_descriptors.py", line 791, in get_prefetch_querysets     
    for rel_obj in queryset:
  File ".venv\Lib\site-packages\django\db\models\query.py", line 400, in __iter__
    self._fetch_all()
  File ".venv\Lib\site-packages\django\db\models\query.py", line 1928, in _fetch_all
    self._result_cache = list(self._iterable_class(self))
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".venv\Lib\site-packages\django\db\models\query.py", line 91, in __iter__
    results = compiler.execute_sql(
              ^^^^^^^^^^^^^^^^^^^^^
  File ".venv\Lib\site-packages\django\db\models\sql\compiler.py", line 1549, in execute_sql
    sql, params = self.as_sql()
                  ^^^^^^^^^^^^^
  File ".venv\Lib\site-packages\django\db\models\sql\compiler.py", line 755, in as_sql
    result, params = self.get_qualify_sql()
                     ^^^^^^^^^^^^^^^^^^^^^^
  File ".venv\Lib\site-packages\django\db\models\sql\compiler.py", line 691, in get_qualify_sql
    qualify_sql, qualify_params = self.compile(self.qualify)
                                  ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".venv\Lib\site-packages\django\db\models\sql\compiler.py", line 546, in compile
    sql, params = node.as_sql(self, self.connection)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File ".venv\Lib\site-packages\django\db\models\sql\where.py", line 176, in as_sql
    raise FullResultSet
django.core.exceptions.FullResultSet
```
