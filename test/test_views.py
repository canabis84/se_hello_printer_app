import unittest
from hello_world import app
from hello_world.formater import SUPPORTED
import json


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        ','.join(SUPPORTED) in rv.data

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        j = json.loads(rv.data)
        self.assertEquals("Darek", j['imie'])

    def test_msg_with_xml(self):
        rv = self.app.get('/?output=xml')
        self.assertEquals('<greetings>\n\t<name>Darek</name>\n\t \
        <msg>Hello World!</msg>\n</greetings>', rv.data)
