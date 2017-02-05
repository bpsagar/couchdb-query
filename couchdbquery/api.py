import json

OPERATORS = {
    'eq': '==',
    'neq': '!=',
    'lt': '<',
    'lte': '<=',
    'gt': '>',
    'gte': '>='
}


def _map_function(**params):
    conditions = []
    for name, value in params.items():
        key, operator_name = name.split('__')
        operator = OPERATORS[operator_name]
        condition = 'doc.{key} {operator} {value}'.format(
            key=key, operator=operator, value=json.dumps(value))
        conditions.append(condition)
    return '''
        function (doc) {
            if (%s) emit(doc, null)
        }
    ''' % (' && '.join(conditions))


def query(db, **params):
    return db.query(_map_function(**params))
