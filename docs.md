# SDK文档
----------

### base_request.py
BaseRequest:  所有钉钉请求的超类，提供一些通用属性与实例方法   
>BaseRequest.`logs_path`: 执行的日志文件的路径    
>BaseRequest.`request_url`: 请求API的URL   
>BaseRequest.`request_methods_valid`: 有效的请求方法，一般为正常的HTTP请求方法    
>BaseRequest.`request_method`: 请求方法的设置，默认为get方法    
>   
>BaseRequest.`set_logger()`: 此方法为程序运行增加logger，具体的logger可选    
>BaseRequest.`get_response()`: 此方法获取请求的原始响应   
>BaseRequest.`get_json_response()`: 该方法将原始响应序列化，获取JSON    
>BaseRequest.`get_call_status()`: 该方法获取请求的结果，返回逻辑值    

### authority_request.py
AccessTokenRequest(BaseRequest):  获取钉钉access_token   
>AccessTokenRequest.`get_access_token()`: 该方法获取access_token的值        

AuthAddressBookRequest(BaseRequest):  获取钉钉通讯录权限范围   
>AuthAddressBookRequest.`get_auth_org_scopes()`: 该方法获取通讯录权限范围     

### user_request.py
DeptUserRequest(BaseRequest):  获取部门成员（ID）   
>DeptUserRequest.`get_unionid()`: 该方法获成员的unionid     
>DeptUserRequest.`get_openid()`: 该方法获成员的openid     
>DeptUserRequest.`get_userinfo()`: 该方法获成员的基本信息     

AdminUsersRequest(BaseRequest):  获取管理员（ID）   
>AdminUsersRequest.`get_admin_ids()`: 该方法获取公司钉钉管理员ID列表     

DeptUsersRequest(BaseRequest):  获取部门成员的详细信息   
>DeptUsersRequest.`get_dept_users_detail()`: 该方法获取部门成员的详细信息列表     

DeptUsersSimpleRequest(BaseRequest):  获取部门成员的简要信息   
>DeptUsersSimpleRequest.`get_dept_users_brief()`: 该方法获取部门成员的简要信息列表     

DeptUserIdsRequest(BaseRequest):  获取部门成员的ID列表   
>DeptUserIdsRequest.`get_dept_user_ids()`: 该方法获取部门成员的ID列表     

### department_request.py
DeptRequest(BaseRequest):  获取部门详细信息   
>DeptRequest.`get_dept_name()`: 该方法获取部门名称     
>DeptRequest.`get_dept_manager_ids()`: 该方法获取部门的管理员ID列表     

DeptsRequest(BaseRequest):  获取部门列表   
>DeptsRequest.`get_depts(dept_name=None)`: 该方法用部门名称获取部门ID，多个同名部门返回列表     

SubDeptIdsRequest(BaseRequest):  获取子部门ID列表   
>SubDeptIdsRequest.`get_sub_dept_ids()`: 该方法获取获取子部门ID列表         

DeptUserIdsRequest(BaseRequest):  向上获取部门的上级部门路径，直到根部门（公司）   
>DeptUserIdsRequest.`get_parent_dept_path()`: 该方法获取部门的父部门路径，以ID表示     

### message_request.py
WorkNoticeRequest(BaseRequest):  发送工作通知   
>DeptRequest.`get_task_id()`: 该方法获取发送工作通知的ID，便于跟踪通知状态       

GetWorkNoticeSendProgressRequest(BaseRequest):  获取工作通知进度   
>GetWorkNoticeSendProgressRequest.`get_progress()`: 该方法获取工作通知进度     

GetWorkNoticeSendResultRequest(BaseRequest):  获取工作通知结果   
>GetWorkNoticeSendResultRequest.`get_send_result()`: 该方法获取工作通知结果         

CreateGroupChatRequest(BaseRequest):  创建群聊   
>CreateGroupChatRequest.`get_chat_id()`: 该方法获取刚刚创建群聊的ID     

UpdateGroupChatRequest(BaseRequest):  更新群聊   

GetGroupChatRequest(BaseRequest):  查看指定群聊   
>GetGroupChatRequest.`get_chat_info()`: 该方法获取群聊的名称，群主等信息    
>GetGroupChatRequest.`get_specified_group_user_ids()`: 该方法获取群聊的成员ID列表    

SendGroupChatRequest(BaseRequest):  发送群聊消息   
>SendGroupChatRequest.`get_message_id()`: 该方法获取群聊消息的ID  

GetReadGroupChatUserIdsRequest(BaseRequest):  获取群消息已读人员ID列表   
>GetReadGroupChatUserIdsRequest.`get_read_user_ids()`: 该方法获取群消息已读人员ID列表  
