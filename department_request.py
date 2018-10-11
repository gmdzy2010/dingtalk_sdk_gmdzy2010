from dingtalk_sdk_gmdzy2010 import settings
from dingtalk_sdk_gmdzy2010.base_request import BaseRequest


class DeptRequest(BaseRequest):
    """
    Description: TODO

    parameter_R: <access_token>, <id> (department_id)
    parameter_O: None

    post_data_R: None
    post_data_O: None

    Return: TODO

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/dubakq
    """
    request_url = settings.GET_DEPT
    
    def get_dept_name(self):
        """Method to get the department name"""
        return self.json_response.get("name", None)
    
    def get_dept_manager_ids(self):
        """Method to get the id list of department manager."""
        return self.json_response.get("deptManagerUseridList", None)


class DeptsRequest(BaseRequest):
    """
    Description: fetch_child (Bool, default is True,
    it decides whether recursively response the sub-department). TODO

    parameter_R: <access_token>, <id> (department_id)
    parameter_O: <fetch_child>

    post_data_R: None
    post_data_O: None

    Return: TODO

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/dubakq
    """
    request_url = settings.GET_DEPTS
    
    def get_depts(self):
        """Method to get the department list"""
        return self.json_response.get("department", None)


class SubDeptIdsRequest(BaseRequest):
    """
    Description: TODO

    parameter_R: <access_token>, <id> (department_id)
    parameter_O: None

    post_data_R: None
    post_data_O: None

    Return: TODO

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/dubakq
    """
    request_url = settings.GET_SUB_DEPT_IDS
    
    def get_sub_dept_ids(self):
        """Method to get the department list"""
        return self.json_response.get("sub_dept_id_list", None)


class ParentDeptPathRequest(BaseRequest):
    """
    Description: TODO

    parameter_R: <access_token>, <id> (department_id)
    parameter_O: None

    post_data_R: None
    post_data_O: None

    Return: TODO

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/dubakq
    """
    request_url = settings.GET_PARENT_DEPT_PATH
    
    def get_parent_dept_path(self):
        """Method to get the department list"""
        return self.json_response.get("parentIds", None)
