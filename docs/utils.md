#### 1. 扫码登陆
用于Python Web应用`扫码登陆`的一个功能函数。
dingtalk_auth(_request_)

参数|说明 
:---|:---
_request_|一个标准的`WSGI HTTP Request`，详见`PEP333`/`PEP3333`
---|---
_DINGTALK_APPID_|钉钉E应用的APPID，请自行存储于os.environ
_DINGTALK_APPSECRET_|钉钉E应用的APPSECRET，请自行存储于os.environ
_DINGTALK_APPKEY_|钉钉扫码登陆（网页认证）的APPKEY，请自行存储于os.environ
_DINGTALK_SECRET_|钉钉扫码登陆（网页认证）的SECRET，请自行存储于os.environ
---|---

#### 2. 部门成员获取
get_department_users(_access_token=None, department_name=None, root=1_)

参数|说明 
:---|:---
_access_token_|全局的access_token
_department_name_|部门名称，不论几级部门均可
_root_|请求的初始部门ID，默认为根部门

#### 3. Django集成
DingtalkNotificationMixin

方法（属性）|说明 
:---|:---
_appkey_|注册E应用获取到的appkey
_appsecret_|注册E应用获取到的appsecret
_send_dingtalk_result_|Bool型变量，用于判断发送工作通知的结果
_send_work_notice(content, sender, recipients)_|发送钉钉工作通知
_send_group_message(self, content, chat_id)_|发送钉钉群消息
