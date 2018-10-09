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
    request_url = settings.CREATE_GROUP_CHAT
