import connexion
import six

from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.pet import Pet  # noqa: E501
from openapi_server import util


def create_pets():  # noqa: E501
    """Create a pet

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def list_pets(limit=None):  # noqa: E501
    """List all pets

     # noqa: E501

    :param limit: How many items to return at one time (max 100)
    :type limit: int

    :rtype: List[Pet]
    """
    return 'do some magic!'


def show_pet_by_id(pet_id):  # noqa: E501
    """Info for a specific pet

     # noqa: E501

    :param pet_id: The id of the pet to retrieve
    :type pet_id: str

    :rtype: Pet
    """
    return 'do some magic!'
