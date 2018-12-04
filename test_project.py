import os
import requests
from dingtalk_sdk_gmdzy2010.authority_request import (
    AccessTokenRequest, PersistentCodeRequest, AuthAddressBookRequest
)
from dingtalk_sdk_gmdzy2010.user_request import (
    DeptUserRequest, AdminUsersRequest, DeptUsersRequest,
    DeptUsersSimpleRequest, DeptUserIdsRequest
)


# certifications needed

appkey = os.environ["DINGTALK_APPKEY"]
appsecret = os.environ["DINGTALK_SECRET"]
agent_id = os.environ["DINGTALK_AGENT_ID"]


def get_token():
    params = {"appkey": appkey, "appsecret": appsecret}
    request = AccessTokenRequest(params=params)
    request.request_method = "get"
    request.get_json_response()
    token = request.get_access_token()
    return token


class TestModuleAuthority:
    """The class to test authority_request.py"""
    
    def test_authentication(self):
        params = {"appkey": appkey, "appsecret": appsecret}
        request = AccessTokenRequest(params=params)
        request.request_method = "get"
        response = request.get_json_response()
        assert response["errmsg"] == "ok"
    
    def test_address_book_scope(self):
        """To test the given scope of address book"""
        params = {"access_token": get_token()}
        request = AuthAddressBookRequest(params=params)
        request.request_method = "get"
        response = request.get_json_response()
        assert response["errmsg"] == "ok"

    def test_persistent_code(self):
        """To test whether a correct persistent code could be return."""
        params = {"access_token": get_token()}
        data = {"tmp_auth_code": ""}
        request = PersistentCodeRequest(params=params, json=data)
        request.request_method = "post"
        response = request.get_json_response()
        assert response["errmsg"] == "ok"


class TestModuleUser:
    """user_request.py"""
    
    def test_dept_user(self):
        params = {"access_token": get_token(), "user_id": 1}
        request = DeptUserRequest(params=params)
        request.request_method = "get"
        response = request.get_json_response()
        assert response["errmsg"] == "找不到该用户"
