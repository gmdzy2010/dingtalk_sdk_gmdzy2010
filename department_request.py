import settings
from base_request import BaseRequest


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
    
    def get_dept_name(self, **kwargs):
        """Method to get the department name"""
        response = self.get_json_response(**kwargs)
        return response.get("name", None)
    
    def get_dept_manager_ids(self, **kwargs):
        """Method to get the id list of department manager."""
        response = self.get_json_response(**kwargs)
        return response.get("deptManagerUseridList", None)


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
    
    def get_depts(self, **kwargs):
        """Method to get the department list"""
        response = self.get_json_response(**kwargs)
        return response.get("department", None)


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
    
    def get_sub_dept_ids(self, **kwargs):
        """Method to get the department list"""
        response = self.get_json_response(**kwargs)
        return response.get("sub_dept_id_list", None)


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
    
    def get_parent_dept_path(self, **kwargs):
        """Method to get the department list"""
        response = self.get_json_response(**kwargs)
        return response.get("parentIds", None)
