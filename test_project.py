from .dingtalk_sdk_gmdzy2010.authority_request import AccessTokenRequest


appkey = "a key which is definitely invalid"
appsecret = "repeat those words above."
agent_id = "test"


def set_authorization(appkey, appsecret):
    params = {"appkey": appkey, "appsecret": appsecret}
    request = AccessTokenRequest(params=params)
    request.request_method = "get"
    response = request.get_json_response()
    return response


def test_answer():
    response = set_authorization(appkey, appsecret)
    assert response["errmsg"] == "test"
