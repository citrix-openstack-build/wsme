from test.tests import FunctionalTest
import json


class TestWS(FunctionalTest):

    def test_get_all(self):
        self.app.get('/authors')

    def test_get_author(self):
        a = self.app.get(
            '/authors/1.json',
        )
        print a
        a = json.loads(a.body)
        print a

        assert a['id'] == 1
        assert a['firstname'] == 'aname'

        a = self.app.get(
            '/authors/1.xml',
        )
        print a
        assert '<id>1</id>' in a.body
        assert '<firstname>aname</firstname>' in a.body