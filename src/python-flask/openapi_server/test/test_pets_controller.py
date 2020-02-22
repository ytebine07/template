# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.pet import Pet  # noqa: E501
from openapi_server.test import BaseTestCase


class TestPetsController(BaseTestCase):
    """PetsController integration test stubs"""

    def test_create_pets(self):
        """Test case for create_pets

        Create a pet
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1/pets',
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_pets(self):
        """Test case for list_pets

        List all pets
        """
        query_string = [('limit', 56)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1/pets',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_show_pet_by_id(self):
        """Test case for show_pet_by_id

        Info for a specific pet
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/v1/pets/{pet_id}'.format(pet_id='pet_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
