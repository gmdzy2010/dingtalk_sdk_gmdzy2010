import settings
from base_request import BaseRequest


class WorkNoticeRequest(BaseRequest):
    """
    Description: parameters of <userid_list> and <dept_id_list> should NOT keep
    null simultaneously, or request would fail. TODO

    parameter_R: <access_token>
    parameter_O: None

    post_data_R: <agent_id>, <msg>
    post_data_O: <userid_list>, <dept_id_list>, <to_all_user>

    Return: send result json response

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/pgoxpy
    """
    request_url = settings.SEND_WORK_NOTICE


class CreateGroupChatRequest(BaseRequest):
    """
    Description: TODO

    parameter_R: <access_token>
    parameter_O: None

    post_data_R: <name>, <owner>, <useridlist>
    post_data_O: <showHistoryType>

    Return: the chatid of group create json response

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/isu6nk
    """
    request_url = settings.CREATE_GROUP_CHAT
    
    def get_chatid(self, **kwargs):
        """Method to get chatid of group created."""
        response = self.get_json_response(**kwargs)
        chatid = response.get("chatid", None)
        return chatid


class UpdateGroupChatRequest(BaseRequest):
    """
    Description: TODO

    parameter_R: <access_token>
    parameter_O: None

    post_data_R: <chatid>
    post_data_O: <name>, <owner>, <add_useridlist>, <del_useridlist>

    Return: the chatid of group create json response

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/isu6nk
    """
    request_url = settings.UPDATE_GROUP_CHAT


class GetGroupChatRequest(BaseRequest):
    """
    Description: TODO

    parameter_R: <access_token>
    parameter_O: None

    post_data_R: <chatid>
    post_data_O: None

    Return: the chatid of group create json response

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/isu6nk
    """
    request_url = settings.UPDATE_GROUP_CHAT
    chat_info = None
    
    def get_chat_info(self, **kwargs):
        """Method to get chatid of group created."""
        response = self.get_json_response(**kwargs)
        chat_info = response.get("chat_info", None)
        self.chat_info = chat_info
        return chat_info
    
    def get_specified_group_user_ids(self):
        user_ids = self.chat_info.get("useridlist", None)
        return user_ids


class SendGroupChatRequest(BaseRequest):
    """
    Description: TODO

    parameter_R: <access_token>
    parameter_O: None

    post_data_R: <chatid>, <msg>
    post_data_O: None

    Return: the chatid of group create json response

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/isu6nk
    """
    request_url = settings.SEND_GROUP_CHAT
    
    def get_message_id(self, **kwargs):
        """Method to get messageId of group created."""
        response = self.get_json_response(**kwargs)
        message_id = response.get("messageId", None)
        return message_id


class GetReadGroupChatUserIdsRequest(BaseRequest):
    """
    Description: TODO

    parameter_R: <access_token>, <messageId>, <cursor>, <size>
    parameter_O: None

    post_data_R: <chatid>, <msg>
    post_data_O: None

    Return: the chatid of group create json response

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/isu6nk
    """
    request_url = settings.GET_READ_USERS
    
    def get_read_user_ids(self, **kwargs):
        """Method to get chatid of group created."""
        response = self.get_json_response(**kwargs)
        read_user_ids = response.get("readUserIdList", None)
        return read_user_ids

