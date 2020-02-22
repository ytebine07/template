import unittest

from openapi_server.models.sample.sample import Sample


class TestSample(unittest.TestCase):

    def test_function(self):
        target = Sample()
        self.assertTrue(target.function())

    def test_test(self):
        self.assertTrue(True)
