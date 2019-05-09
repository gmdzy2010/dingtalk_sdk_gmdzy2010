"""
This module contains some useful tool for simplifying request process
"""
import os

from dingtalk_sdk_gmdzy2010.authority_request import AccessTokenRequest,\
    SnsAccessTokenRequest, PersistentCodeRequest, SnsTokenRequest,\
    UserInfoRequest
from dingtalk_sdk_gmdzy2010.department_request import DeptsRequest,\
    SubDeptIdsRequest
from dingtalk_sdk_gmdzy2010.message_request import SendGroupChatRequest,\
    WorkNoticeRequest
from dingtalk_sdk_gmdzy2010.user_request import UseridByUnionidRequest,\
    DeptUsersSimpleRequest


# You should store these credentials into os environment variables

# Credentials for api invoking
DINGTALK_APPID = os.environ.get("DINGTALK_APPID")
DINGTALK_APPSECRET = os.environ.get("DINGTALK_APPSECRET")

# Credentials for OAuth of dingtalk
DINGTALK_APPKEY = os.environ.get("DINGTALK_APPKEY")
DINGTALK_SECRET = os.environ.get("DINGTALK_APPID")


def dingtalk_auth(request):
    """
    A function for the oauth of dingtalk
    :param request: A standard WSGI request
    :return: unionid, userid
    """
    
    # STEP 1. Get sns access_token
    params_1 = {"appid": DINGTALK_APPID, "appsecret": DINGTALK_APPSECRET}
    req_sns_access_token = SnsAccessTokenRequest(params=params_1)
    req_sns_access_token.get_json_response()
    sns_access_token = req_sns_access_token.get_sns_access_token()
    
    # STEP 2. Get persistent code
    params_2 = {"access_token": sns_access_token}
    data = {"tmp_auth_code": request.GET["code"]}
    req_persistent_code = PersistentCodeRequest(params=params_2, json=data)
    req_persistent_code.request_method = "post"
    req_persistent_code.get_json_response()
    ticket = req_persistent_code.get_ticket_for_sns_token()
    
    # STEP 3. Get sns token
    params_3 = {"access_token": sns_access_token}
    req_sns_token = SnsTokenRequest(params=params_3, json=ticket)
    req_sns_token.request_method = "post"
    req_sns_token.get_json_response()
    sns_token = req_sns_token.get_sns_token()
    
    # STEP 4. Get unionid
    params_4 = {"sns_token": sns_token}
    req_user_info = UserInfoRequest(params=params_4)
    req_user_info.get_json_response()
    user_info = req_user_info.get_user_info()
    unionid = user_info["unionid"]
    
    # STEP 5. Get userid
    params_5 = {"appkey": DINGTALK_APPKEY, "appsecret": DINGTALK_SECRET}
    req_access_token = AccessTokenRequest(params=params_5)
    req_access_token.get_json_response()
    params_6 = {
        "access_token": req_access_token.get_access_token(),
        "unionid": user_info["unionid"]
    }
    req_userid = UseridByUnionidRequest(params=params_6)
    req_userid.get_json_response()
    userid = req_userid.get_userid()
    return unionid, userid


def get_token(**credentials):
    request = AccessTokenRequest(params=credentials)
    request.get_json_response()
    access_token = request.get_access_token()
    return access_token


def recur_department_ids(init_ids=None, total_ids=None, access_token=None):
    """
    The recursion tool for acquiring all sub departments
    :param init_ids: the initial id list
    :param total_ids: the accumulated is list coupled with recursion
    :param access_token: the global access token
    :return: the final "total id list" until there aren't any sub node.
    """
    if init_ids:
        total_sub_department_ids = []
        for _id in init_ids:
            params = {"access_token": access_token, "id": _id}
            sub_department_ids_request = SubDeptIdsRequest(params=params)
            sub_department_ids_request.get_json_response()
            sub_department_ids = sub_department_ids_request.get_sub_dept_ids()
            if not sub_department_ids:
                continue
            total_sub_department_ids.extend(sub_department_ids)
        total_ids.extend(total_sub_department_ids)
        return recur_department_ids(
            init_ids=total_sub_department_ids, total_ids=total_ids,
            access_token=access_token)
    else:
        return total_ids


def get_department_users(access_token=None, department_name=None, root=1):
    """
    Method to collect all of the members for specified department are not
    supplied officially, the only way to make it is to the recursion as below.
    """
    if access_token is None or department_name is None:
        raise ValueError("No access_token or department name, return nothing!")
    
    params = {"access_token": access_token, "id": root, "fetch_child": False}
    departments_request = DeptsRequest(params=params)
    departments_request.get_json_response()
    sub_departments = departments_request.get_depts(dept_name=department_name)
    
    # the recursion function to collect members.
    department_ids = recur_department_ids(
        init_ids=[sub_departments["id"]], total_ids=[sub_departments["id"]],
        access_token=access_token)
    if not department_ids:
        return department_ids
    
    department_users = []
    for _id in department_ids:
        params = {"access_token": access_token, "department_id": _id}
        dept_users_request = DeptUsersSimpleRequest(params=params)
        dept_users_request.get_json_response()
        department_users.extend(dept_users_request.get_dept_users_brief())
    return department_users


class DingtalkNotificationMixin(object):
    """Mixin that supply dingtalk functions to django ModelAdmin"""
    appkey = None
    appsecret = None
    send_dingtalk_result = False
    
    def get_dingtalk_token(self):
        params = {"appkey": self.appkey, "appsecret": self.appsecret}
        request = AccessTokenRequest(params=params)
        request.get_json_response()
        return request.get_access_token()
    
    def send_work_notice(self, content, sender, recipient_list):
        params = {"access_token": self.get_dingtalk_token()}
        data = {
            "agent_id": sender,
            "userid_list": recipient_list,
            "msg": {"msgtype": "text", "text": {"content": content}}
        }
        request = WorkNoticeRequest(params=params, json=data)
        request.request_method = "post"
        request.get_json_response()
        self.send_dingtalk_result = request.call_status
    
    def send_group_message(self, content, chat_id):
        params = {"access_token": self.get_dingtalk_token()}
        data = {
            "chatid": chat_id,
            "msg": {"msgtype": "text", "text": {"content": content}}
        }
        request = SendGroupChatRequest(params=params, json=data)
        request.request_method = "post"
        request.get_json_response()
        self.send_dingtalk_result = request.call_status
