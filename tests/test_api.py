import unittest
import couchdb
import couchdbquery


class QueryTest(unittest.TestCase):
    """Tests for each of the operators"""

    def setUp(self):
        self.couch = couchdb.Server()
        self.db = self.couch.create('test')

    def tearDown(self):
        self.couch.delete('test')

    def test_eq(self):
        """Testing equals operator"""
        docs = [
            {'_id': 'testeq1', 'number': 10, 'string': 'abc'},
            {'_id': 'testeq2', 'number': 20, 'string': 'abc'},
            {'_id': 'testeq3', 'number': 10, 'string': 'def'}
        ]
        for doc in docs:
            self.db.save(doc)

        results = couchdbquery.query(self.db, number__eq=10, string__eq='abc')
        ids = [row.id for row in results.rows]
        self.assertEqual(ids, ['testeq1'])

        results = couchdbquery.query(self.db, number__eq=10)
        ids = [row.id for row in results.rows]
        self.assertEqual(ids, ['testeq1', 'testeq3'])

        results = couchdbquery.query(self.db, string__eq='abc')
        ids = [row.id for row in results.rows]
        self.assertEqual(ids, ['testeq1', 'testeq2'])

    def test_neq(self):
        """Testing not equals operator"""
        docs = [
            {'_id': 'testeq1', 'number': 10, 'string': 'abc'},
            {'_id': 'testeq2', 'number': 20, 'string': 'abc'},
            {'_id': 'testeq3', 'number': 10, 'string': 'def'}
        ]
        for doc in docs:
            self.db.save(doc)

        results = couchdbquery.query(
            self.db, number__neq=10, string__neq='abc')
        ids = [row.id for row in results.rows]
        self.assertEqual(ids, [])

        results = couchdbquery.query(self.db, number__neq=10)
        ids = [row.id for row in results.rows]
        self.assertEqual(ids, ['testeq2'])

        results = couchdbquery.query(self.db, string__neq='def')
        ids = [row.id for row in results.rows]
        self.assertEqual(ids, ['testeq1', 'testeq2'])

    def test_lt(self):
        """Testing less than operator"""
        docs = [
            {'_id': 'testeq1', 'number': 10, 'string': 'abc'},
            {'_id': 'testeq2', 'number': 20, 'string': 'abc'},
            {'_id': 'testeq3', 'number': 10, 'string': 'def'}
        ]
        for doc in docs:
            self.db.save(doc)

        results = couchdbquery.query(self.db, number__lt=30, string__lt='def')
        ids = [row.id for row in results.rows]
        self.assertEqual(ids, ['testeq1', 'testeq2'])

        results = couchdbquery.query(self.db, number__lt=20)
        ids = [row.id for row in results.rows]
        self.assertEqual(ids, ['testeq1', 'testeq3'])

        results = couchdbquery.query(self.db, string__lt='def')
        ids = [row.id for row in results.rows]
        self.assertEqual(ids, ['testeq1', 'testeq2'])

    def test_lte(self):
        """Testing less than or equal to operator"""
        docs = [
            {'_id': 'testeq1', 'number': 10, 'string': 'abc'},
            {'_id': 'testeq2', 'number': 20, 'string': 'abc'},
            {'_id': 'testeq3', 'number': 10, 'string': 'def'}
        ]
        for doc in docs:
            self.db.save(doc)

        results = couchdbquery.query(
            self.db, number__lte=20, string__lte='def')
        ids = [row.id for row in results.rows]
        self.assertEqual(ids, ['testeq1', 'testeq2', 'testeq3'])

        results = couchdbquery.query(self.db, number__lte=10)
        ids = [row.id for row in results.rows]
        self.assertEqual(ids, ['testeq1', 'testeq3'])

        results = couchdbquery.query(self.db, string__lte='def')
        ids = [row.id for row in results.rows]
        self.assertEqual(ids, ['testeq1', 'testeq2', 'testeq3'])

    def test_gt(self):
        """Testing less than operator"""
        docs = [
            {'_id': 'testeq1', 'number': 10, 'string': 'abc'},
            {'_id': 'testeq2', 'number': 20, 'string': 'abc'},
            {'_id': 'testeq3', 'number': 10, 'string': 'def'}
        ]
        for doc in docs:
            self.db.save(doc)

        results = couchdbquery.query(self.db, number__gt=10, string__gt='abc')
        ids = [row.id for row in results.rows]
        self.assertEqual(ids, [])

        results = couchdbquery.query(self.db, number__gt=10)
        ids = [row.id for row in results.rows]
        self.assertEqual(ids, ['testeq2'])

        results = couchdbquery.query(self.db, string__gt='abc')
        ids = [row.id for row in results.rows]
        self.assertEqual(ids, ['testeq3'])

    def test_gte(self):
        """Testing less than or equal to operator"""
        docs = [
            {'_id': 'testeq1', 'number': 10, 'string': 'abc'},
            {'_id': 'testeq2', 'number': 20, 'string': 'abc'},
            {'_id': 'testeq3', 'number': 10, 'string': 'def'}
        ]
        for doc in docs:
            self.db.save(doc)

        results = couchdbquery.query(
            self.db, number__gte=10, string__gte='abc')
        ids = [row.id for row in results.rows]
        self.assertEqual(ids, ['testeq1', 'testeq2', 'testeq3'])

        results = couchdbquery.query(self.db, number__gte=20)
        ids = [row.id for row in results.rows]
        self.assertEqual(ids, ['testeq2'])

        results = couchdbquery.query(self.db, string__gte='def')
        ids = [row.id for row in results.rows]
        self.assertEqual(ids, ['testeq3'])
