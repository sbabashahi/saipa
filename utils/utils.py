from django.utils.translation import ugettext
from querystring_parser import parser

from utils.exceptions import CustomException


def jwt_response_payload_handler(token):
    """
    Add any data you want to payload of response
    :param token:
    :return:
    """
    return {
        'token': token,
    }


def pagination_util(request):
    arguments = parser.parse(request.GET.urlencode())
    try:
        size = int(arguments.pop('size', 20))
        index = int(arguments.pop('index', 0))
    except ValueError:
        raise CustomException(detail=ugettext('Size and index query param for pagination must be integer.'), code=400)
    size = index + size
    return index, size
