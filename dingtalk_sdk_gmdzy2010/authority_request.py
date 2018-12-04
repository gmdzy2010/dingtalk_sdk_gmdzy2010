from dingtalk_sdk_gmdzy2010 import settings
from dingtalk_sdk_gmdzy2010.base_request import BaseRequest


class AccessTokenRequest(BaseRequest):
    """
    Description: The access token is globally valid within 7200 seconds. To get
    the token, two url parameters are necessary: appkey and appsecret, by
    default, those should be contained in module settings.py

    parameter_R: <appkey>, <appsecret>
    parameter_O: None

    post_data_R: None
    post_data_O: None

    Return: the access_token of dingtalk api.

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/gh60vz
    """
    request_url = settings.GET_TOKEN
    
    def get_access_token(self):
        access_token = self.json_response.get("access_token", None)
        self.logger.info("%s\t%s" % (self.request_method, self.request_url))
        return access_token


class SnsAccessTokenRequest(BaseRequest):
    """
    Description: The sns access token is globally valid within 7200 seconds.
    Note that this access token is just for the sns authentication, which is
    different from access token for global authentication

    parameter_R: <appid>, <appsecret>
    parameter_O: None

    post_data_R: None
    post_data_O: None

    Return: the sns access_token of dingtalk api.

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/gh60vz
    """
    request_url = settings.GET_SNS_ACCESS_TOKEN
    
    def get_sns_access_token(self):
        access_token = self.json_response.get("access_token", None)
        self.logger.info("%s\t%s" % (self.request_method, self.request_url))
        return access_token


class PersistentCodeRequest(BaseRequest):
    """
    Description: The persistent_code, openid and unionid are contained in the
    json response of this api, the parameter <access_token> and post data
    <tmp_auth_code> is required.

    parameter_R: <access_token>
    parameter_O: None

    post_data_R: <tmp_auth_code>
    post_data_O: None

    Return: the persistent_code, openid and unionid of dingtalk api.

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/athq8o
    """
    request_url = settings.GET_PERSISTENT_CODE
    
    def get_openid(self):
        openid = self.json_response.get("openid", None)
        self.logger.info("%s\t%s" % (self.request_method, self.request_url))
        return openid

    def get_unionid(self):
        unionid = self.json_response.get("unionid", None)
        self.logger.info("%s\t%s" % (self.request_method, self.request_url))
        return unionid

    def get_persistent_code(self):
        persistent_code = self.json_response.get("persistent_code", None)
        self.logger.info("%s\t%s" % (self.request_method, self.request_url))
        return persistent_code
    
    def get_ticket_for_sns_token(self):
        """This is a shortcut for getting the sns_token, as a post data of
        request body."""
        self.logger.info("%s\t%s" % (self.request_method, self.request_url))
        return {
            "openid": self.get_openid(),
            "persistent_code": self.get_persistent_code(),
        }


class SnsTokenRequest(BaseRequest):
    """
    Description: The sns_token is contained in the json response of this api,
    the parameter <access_token> and post data <openid>, <persistent_code>
    is required.

    parameter_R: <access_token>
    parameter_O: None

    post_data_R: <openid>, <persistent_code>
    post_data_O: None

    Return: the sns_token

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/athq8o
    """
    request_url = settings.GET_SNS_TOKEN
    
    def get_sns_token(self):
        sns_token = self.json_response.get("sns_token", None)
        self.logger.info("%s\t%s" % (self.request_method, self.request_url))
        return sns_token
    
    def get_expiring_time(self):
        """The sns_token will expire within 7200 secs"""
        expires_in = self.json_response.get("expires_in", None)
        return expires_in


class UserInfoRequest(BaseRequest):
    """
    Description: The only parameter required is <sns_token>

    parameter_R: <sns_token>
    parameter_O: None

    post_data_R: None
    post_data_O: None

    Return: the userinfo of the specified user including nick_name, the openid
    and the unionid.

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/athq8o
    """
    request_url = settings.GET_USERINFO
    
    def get_user_info(self):
        user_info = self.json_response.get("user_info", None)
        self.logger.info("%s\t%s" % (self.request_method, self.request_url))
        return user_info


class AuthAddressBookRequest(BaseRequest):
    """
    Description: The response of this request show the scopes of current
    requester owns.

    parameter_R: <access_token>
    parameter_O: None

    post_data_R: None
    post_data_O: None

    Return: the department id list which is authorized

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/vt6v7m
    """
    request_url = settings.AUTH_ADDRESS_BOOK
    
    def get_auth_org_scopes(self):
        self.logger.info("%s\t%s" % (self.request_method, self.request_url))
        return self.json_response.get("auth_org_scopes", None)
