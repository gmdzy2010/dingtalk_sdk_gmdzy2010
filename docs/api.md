#### base_request.py
方法（属性）|说明 
:---|:---
BaseRequest._logs_path_|执行的日志文件的路径
BaseRequest._request_url_|请求API的URL
BaseRequest._request_methods_valid_|RFC2616定义的HTTP请求方法
BaseRequest._request_method_|请求方法的设置，默认为get方法
BaseRequest._set_logger()_|程序运行增加logger，具体的logger可选
BaseRequest._get_response()_|请求的原始响应
BaseRequest._get_json_response()_|原始响应序列化，获取JSON
BaseRequest._get_call_status_|获取请求的结果，返回逻辑值

#### authority_request.py
方法（属性）|说明 
:---|:---
AccessTokenRequest._get_access_token()_|获取access_token的值
SnsAccessTokenRequest._get_sns_access_token()_|获取sns_access_token的值
PersistentCodeRequest._get_openid()_|获取用户openid的值
PersistentCodeRequest._get_unionid()_|获取用户unionid的值
PersistentCodeRequest._get_persistent_code()_|获取用户持久授权码
PersistentCodeRequest._get_ticket_for_sns_token()_|组合方法，为扫码登陆做准备
SnsTokenRequest._get_sns_token()_|获取用户sns_token的值
SnsTokenRequest._get_expiring_time()_|获取用户token过期时间
UserInfoRequest._get_user_info()_|获取用户钉钉信息（昵称等）
AuthAddressBookRequest._get_auth_org_scopes()_|获取通讯录权限范围

#### user_request.py
方法（属性）|说明 
:---|:---
DeptUserRequest._get_unionid()_|获成员的unionid
DeptUserRequest._get_openid()_|获成员的openid
DeptUserRequest._get_userinfo()_|获成员的基本信息
AdminUsersRequest._get_admin_ids()_|获取公司钉钉管理员ID列表
DeptUsersRequest._get_dept_users_detail()_|获取部门成员的详细信息列表
DeptUsersSimpleRequest._get_dept_users_brief()_|获取部门成员的简要信息列表
DeptUserIdsRequest._get_dept_user_ids()_|获取部门成员的ID列表
UseridByUnionidRequest._get_userid()_|根据unionid获取userid

#### department_request.py
方法（属性）|说明 
:---|:---
DeptRequest._get_dept_name()_|获取部门名称
DeptRequest._get_dept_manager_ids()_|获取部门的管理员ID列表
DeptsRequest._get_depts(dept_name=None)_|用部门名称获取部门ID，多个同名部门返回列表
SubDeptIdsRequest._get_sub_dept_ids()_|获取获取子部门ID列表
DeptUserIdsRequest._get_parent_dept_path()_|获取部门的父部门路径，以ID表示

#### message_request.py
方法（属性）|说明 
:---|:---
DeptRequest._get_task_id()_|获取发送工作通知的ID
GetWorkNoticeSendProgressRequest._get_progress()_|获取工作通知进度
GetWorkNoticeSendResultRequest._get_send_result()_|获取工作通知结果
CreateGroupChatRequest._get_chat_id()_|获取创建群聊的ID
GetGroupChatRequest._get_chat_info()_|获取群聊的名称，群主等信息
GetGroupChatRequest._get_specified_group_user_ids()_|获取群聊的成员ID列表
SendGroupChatRequest._get_message_id()_|获取群聊消息的ID
GetReadGroupChatUserIdsRequest._get_message_id()_|获取群消息已读人员ID列表
