def jwt_response_payload_handler(token):
    """
    Add any data you want to payload of response
    :param token:
    :return:
    """
    return {
        'token': token,
    }
