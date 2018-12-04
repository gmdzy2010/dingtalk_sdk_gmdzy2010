from dingtalk_sdk_gmdzy2010 import settings
from dingtalk_sdk_gmdzy2010.base_request import BaseRequest


class DeptUserRequest(BaseRequest):
    """
    Description: The response of DeptUserRequest contains a department member's
    detail information specified by userid

    parameter_R: <access_token>, <userid>
    parameter_O: None

    post_data_R: None
    post_data_O: None

    Return: a department member's detail information specified by userid

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/ege851
    """
    request_url = settings.GET_DEPT_USER
    
    def get_unionid(self):
        """Method to get the unionid"""
        return self.json_response.get("unionid", None)
    
    def get_openid(self):
        """Method to get the openid"""
        return self.json_response.get("openid", None)
    
    def get_userinfo(self):
        """Method to get current user's name, mobile, email and position."""
        wanted_fields = ["name", "mobile", "orgEmail", "position", "avatar"]
        userinfo = {k: self.json_response.get(k, None) for k in wanted_fields}
        return userinfo


class AdminUsersRequest(BaseRequest):
    """
    Description: The response of AdminUsersRequest contains all admin user's id
    list

    parameter_R: <access_token>
    parameter_O: None

    post_data_R: None
    post_data_O: None

    Return: admin user's id list

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/ege851
    """
    request_url = settings.GET_ADMIN_USERS
    
    def get_admin_ids(self):
        """Method to get the administrator id list."""
        admins = self.json_response.get("admin_list", None)
        admin_ids = [admin_id for admin_id in admins["userid"]]
        return admin_ids


class DeptUsersRequest(BaseRequest):
    """
    Description: The response of DeptUsersRequest contains all members detailed
    information for specified department by department_id. Only parameters of
    offset and size set at the same time, the function of page query could be
    effective

    parameter_R: <access_token>, <department_id>, <offset>, <size>
    parameter_O: <order>

    post_data_R: None
    post_data_O: None

    Return: all members detailed information for specified department by
    department_id

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/ege851
    """
    request_url = settings.GET_DEPT_USERS
    
    def get_dept_users_detail(self):
        """Method to get the userinfo list in detail for the specified
        department."""
        dept_users_detail = self.json_response.get("userlist", None)
        return dept_users_detail


class DeptUsersSimpleRequest(BaseRequest):
    """
    Description: The response of DeptUsersSimpleRequest contains all members
    brief information for specified department by department_id.

    parameter_R: <access_token>, <department_id>
    parameter_O: <offset>, <size>, <order>

    post_data_R: None
    post_data_O: None

    Return: all members brief information for specified department by
    department_id

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/ege851
    """
    request_url = settings.GET_DEPT_USERS_SIMPLE
    
    def get_dept_users_brief(self):
        """Method to get set that contain userid and name."""
        dept_users_brief = self.json_response.get("userlist", None)
        return dept_users_brief


class DeptUserIdsRequest(BaseRequest):
    """
    Description: The response of DeptUserIdsRequest contains a member id list
    for specified department by deptId.

    parameter_R: <access_token>, <deptId>
    parameter_O: None

    post_data_R: None
    post_data_O: None

    Return: a member id list for specified department by deptId.

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/ege851
    """
    request_url = settings.GET_DEPT_USER_IDS
    
    def get_dept_user_ids(self):
        """Method to get all department members."""
        dept_user_ids = self.json_response.get("userIds", None)
        return dept_user_ids


class UseridByUnionidRequest(BaseRequest):
    """
    Description: The response of UseridByUnionidRequest contains wanted userid
    by unionid. Attention! this access token is the global access token, not
    the sns access token.

    parameter_R: <access_token>, <unionid>
    parameter_O: None

    post_data_R: None
    post_data_O: None

    Return: userid.

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/ege851
    """
    request_url = settings.GET_USER_ID_BY_UNIONID
    
    def get_userid(self):
        """Method to get all department members."""
        userid = self.json_response.get("userid", None)
        return userid
