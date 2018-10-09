import settings
from base_request import BaseRequest


class AccessTokenRequest(BaseRequest):
    """
    Description: The access token is globally valid within 7200 seconds. To get
    the token, two url parameters are necessary: appkey and appsecret, by
    default, those should be contained in module settings.py

    parameter_R: <appkey>, <appsecret>
    parameter_O: None

    post_data_R: None
    post_data_O: None

    Return: TODO

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/vt6v7m
    """
    request_url = settings.GET_TOKEN
    
    def get_access_token(self, **kwargs):
        json_response = self.get_json_response(**kwargs)
        access_token = json_response.get("access_token", None)
        return access_token


class AuthAddressBookRequest(BaseRequest):
    """
    Description: TODO

    parameter_R: <access_token>
    parameter_O: None

    post_data_R: None
    post_data_O: None

    Return: TODO

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/vt6v7m
    """
    request_url = settings.AUTH_ADDRESS_BOOK
    
    def get_auth_org_scopes(self, **kwargs):
        response = self.get_json_response(**kwargs)
        return response.get("auth_org_scopes", None)
