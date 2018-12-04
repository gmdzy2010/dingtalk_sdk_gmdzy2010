from dingtalk_sdk_gmdzy2010 import settings
from dingtalk_sdk_gmdzy2010.base_request import BaseRequest


class WorkNoticeRequest(BaseRequest):
    """
    Description: The WorkNoticeRequest send work notice to specified user
    (userid), parameters of <userid_list> and <dept_id_list> should NOT keep
    null simultaneously, or request would fail

    parameter_R: <access_token>
    parameter_O: None

    post_data_R: <agent_id>, <msg>
    post_data_O: <userid_list>, <dept_id_list>, <to_all_user>

    Return: send result json response

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/pgoxpy
    """
    request_url = settings.SEND_WORK_NOTICE
    task_id = None
    
    def get_task_id(self):
        """Method to get all department members."""
        task_id = self.json_response.get("task_id", None)
        self.logger.info("%s\t%s" % (self.request_method, self.request_url))
        return task_id


class GetWorkNoticeSendProgressRequest(BaseRequest):
    """
    Description: The response of GetWorkNoticeSendProgressRequest shows the
    progress of sending work notice

    parameter_R: <access_token>
    parameter_O: None

    post_data_R: <agent_id>, <msg>
    post_data_O: <userid_list>, <dept_id_list>, <to_all_user>

    Return: the progress of sending work notice

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/pgoxpy
    """
    request_url = settings.GET_WORK_NOTICE_SEND_PROGRESS
    
    def get_progress(self):
        """Method to get the progress of work notice sending."""
        progress = self.json_response.get("progress", None)
        self.logger.info("%s\t%s" % (self.request_method, self.request_url))
        return progress


class GetWorkNoticeSendResultRequest(BaseRequest):
    """
    Description: The response of GetWorkNoticeSendResultRequest shows the
    result of sending work notice

    parameter_R: <access_token>
    parameter_O: None

    post_data_R: None
    post_data_O: <agent_id>, <task_id>

    Return: send result json response

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/pgoxpy
    """
    request_url = settings.GET_WORK_NOTICE_SEND_RESULT
    
    def get_send_result(self):
        """Method to get the progress of work notice sending."""
        send_result = self.json_response.get("send_result", None)
        self.logger.info("%s\t%s" % (self.request_method, self.request_url))
        return send_result


class CreateGroupChatRequest(BaseRequest):
    """
    Description: The CreateGroupChatRequest aims to create a group chat for
    some user(userid)

    parameter_R: <access_token>
    parameter_O: None

    post_data_R: <name>, <owner>, <useridlist>
    post_data_O: <showHistoryType>

    Return: the chatid of group create json response

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/isu6nk
    """
    request_url = settings.CREATE_GROUP_CHAT
    
    def get_chat_id(self):
        """Method to get chatid of group created."""
        chat_id = self.json_response.get("chatid", None)
        self.logger.info("%s\t%s" % (self.request_method, self.request_url))
        return chat_id


class UpdateGroupChatRequest(BaseRequest):
    """
    Description: The UpdateGroupChatRequest aims to update the group chat such
    as the user list, name or something else

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
    Description: The GetGroupChatRequest aims to get information of a existed
    group chat by chatid

    parameter_R: <access_token>
    parameter_O: None

    post_data_R: <chatid>
    post_data_O: None

    Return: the chatid of group create json response

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/isu6nk
    """
    request_url = settings.UPDATE_GROUP_CHAT
    chat_info = None
    
    def get_chat_info(self):
        """Method to get chatid of group created."""
        chat_info = self.json_response.get("chat_info", None)
        self.chat_info = chat_info
        self.logger.info("%s\t%s" % (self.request_method, self.request_url))
        return chat_info
    
    def get_specified_group_user_ids(self):
        user_ids = self.chat_info.get("useridlist", None)
        self.logger.info("%s\t%s" % (self.request_method, self.request_url))
        return user_ids


class SendGroupChatRequest(BaseRequest):
    """
    Description: The SendGroupChatRequest aims to send group chat message

    parameter_R: <access_token>
    parameter_O: None

    post_data_R: <chatid>, <msg>
    post_data_O: None

    Return: the message id of group chat

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/isu6nk
    """
    request_url = settings.SEND_GROUP_CHAT
    
    def get_message_id(self):
        """Method to get messageId of group created."""
        message_id = self.json_response.get("messageId", None)
        self.logger.info("%s\t%s" % (self.request_method, self.request_url))
        return message_id


class GetReadGroupChatUserIdsRequest(BaseRequest):
    """
    Description: The GetReadGroupChatUserIdsRequest aims to get the user id
    list of whom has read message by messageId

    parameter_R: <access_token>, <messageId>, <cursor>, <size>
    parameter_O: None

    post_data_R: <chatid>, <msg>
    post_data_O: None

    Return: the user id list which has read the message

    doc_links: https://open-doc.dingtalk.com/microapp/serverapi2/isu6nk
    """
    request_url = settings.GET_READ_USERS
    
    def get_read_user_ids(self):
        """Method to get chatid of group created."""
        read_user_ids = self.json_response.get("readUserIdList", None)
        self.logger.info("%s\t%s" % (self.request_method, self.request_url))
        return read_user_ids
