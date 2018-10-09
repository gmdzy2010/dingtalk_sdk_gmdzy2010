import settings
from base_request import BaseRequest


class DeptUserRequest(BaseRequest):
    """
    Description: TODO

    parameter_R: <access_token>, <userid>
    parameter_O: None

    post_data_R: None
    post_data_O: None

    Return: TODO

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/ege851
    """
    request_url = settings.GET_DEPT_USER
    
    def get_unionid(self, **kwargs):
        """Method to get the unionid"""
        response = self.get_json_response(**kwargs)
        return response.get("unionid", None)
    
    def get_openid(self, **kwargs):
        """Method to get the openid"""
        response = self.get_json_response(**kwargs)
        return response.get("openid", None)
    
    def get_userinfo(self, **kwargs):
        """Method to get current user's name, mobile, email and position."""
        response = self.get_json_response(**kwargs)
        wanted_fields = ["name", "mobile", "orgEmail", "position", "avatar"]
        userinfo = {key: response.get(key, None) for key in wanted_fields}
        return userinfo


class AdminUsersRequest(BaseRequest):
    """
    Description: TODO

    parameter_R: <access_token>
    parameter_O: None

    post_data_R: None
    post_data_O: None

    Return: TODO

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/ege851
    """
    request_url = settings.GET_ADMIN_USERS
    
    def get_admin_ids(self, **kwargs):
        """Method to get the administrator id list."""
        response = self.get_json_response(**kwargs)
        admins = response.get("admin_list", None)
        admin_ids = [admin_id for admin_id in admins["userid"]]
        return admin_ids


class DeptUsersRequest(BaseRequest):
    """
    Description: only parameters of offset and size set at the same time, the
    function of page query could be effective. TODO

    parameter_R: <access_token>, <department_id>, <offset>, <size>
    parameter_O: <order>

    post_data_R: None
    post_data_O: None

    Return: TODO

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/ege851
    """
    request_url = settings.GET_DEPT_USERS
    
    def get_dept_users_detail(self, **kwargs):
        """Method to get the userinfo list in detail for the specified
        department."""
        response = self.get_json_response(**kwargs)
        dept_users_detail = response.get("userlist", None)
        return dept_users_detail


class DeptUsersSimpleRequest(BaseRequest):
    """
    Description: only parameters of offset and size set simultaneously, the
    function of page query could be effective. TODO

    parameter_R: <access_token>, <department_id>
    parameter_O: <offset>, <size>, <order>

    post_data_R: None
    post_data_O: None

    Return: a couple of message of users

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/ege851
    """
    request_url = settings.GET_DEPT_USERS_SIMPLE
    
    def get_dept_users_brief(self, **kwargs):
        """Method to get set that contain userid and name."""
        response = self.get_json_response(**kwargs)
        dept_users_brief = response.get("userlist", None)
        return dept_users_brief


class DeptUserIdsRequest(BaseRequest):
    """
    Description: TODO

    parameter_R: <access_token>, <deptId>
    parameter_O: None

    post_data_R: None
    post_data_O: None

    Return: TODO

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/ege851
    """
    request_url = settings.GET_DEPT_USER_IDS
    
    def get_dept_user_ids(self, **kwargs):
        """Method to get all department members."""
        response = self.get_json_response(**kwargs)
        dept_user_ids = response.get("userIds", None)
        return dept_user_ids
