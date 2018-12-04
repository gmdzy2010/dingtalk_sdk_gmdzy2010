"""
This module contain the global settings for the python sdk of dingtalk
"""


# The root url of dingtalk api

URL_ROOT = "https://oapi.dingtalk.com/"

# The access token should be got from the url below
# Attention: be care the limits of this api

GET_TOKEN = URL_ROOT + "gettoken"

# Authentication scopes of address book

AUTH_ADDRESS_BOOK = URL_ROOT + "auth/scopes"

GET_SNS_ACCESS_TOKEN = URL_ROOT + "sns/gettoken"

GET_PERSISTENT_CODE = URL_ROOT + "sns/get_persistent_code"

GET_SNS_TOKEN = URL_ROOT + "sns/get_sns_token"

GET_USERINFO = URL_ROOT + "sns/getuserinfo"

# Department management

DEPT_ROOT = URL_ROOT + "department/"

GET_DEPT = DEPT_ROOT + "get"

GET_DEPTS = DEPT_ROOT + "list"

GET_SUB_DEPT_IDS = DEPT_ROOT + "list_ids"

GET_PARENT_DEPT_PATH = DEPT_ROOT + "list_parent_depts_by_dept"

# User management

USER_ROOT = URL_ROOT + "user/"

GET_DEPT_USER = USER_ROOT + "get"

GET_ADMIN_USERS = USER_ROOT + "get_admin"

GET_DEPT_USERS = USER_ROOT + "listbypage"

GET_DEPT_USERS_SIMPLE = USER_ROOT + "simplelist"

GET_DEPT_USER_IDS = USER_ROOT + "getDeptMember"

GET_USER_ID_BY_UNIONID = USER_ROOT + "getUseridByUnionid"

# Work notice

WORK_NOTICE_ROOT = URL_ROOT + "topapi/message/corpconversation/"

SEND_WORK_NOTICE = WORK_NOTICE_ROOT + "asyncsend_v2"

GET_WORK_NOTICE_SEND_PROGRESS = WORK_NOTICE_ROOT + "getsendprogress"

GET_WORK_NOTICE_SEND_RESULT = WORK_NOTICE_ROOT + "getsendresult"

# The group and group chat

CHAT_ROOT = URL_ROOT + "chat/"

CREATE_GROUP_CHAT = CHAT_ROOT + "create"

UPDATE_GROUP_CHAT = CHAT_ROOT + "update"

GET_GROUP_CHAT = CHAT_ROOT + "get"

SEND_GROUP_CHAT = CHAT_ROOT + "send"

GET_READ_USERS = CHAT_ROOT + "getReadList"
