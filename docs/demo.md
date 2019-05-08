下面以`发送工作通知`为例，演示SDK的使用，示例代码可以按需自行优化。（示例基于v0.2.4）

-------------------------------------------------------------------------------

###### STEP 1. 获取access_token
将`appkey`，`appsecret`以及`agent_id`配置到项目的`settings.py`文件当中，再将这两个变量导入相应模块。
以下给出示例代码，用appkey与appsecret换取钉钉接口密钥，其有效期为2小时，超时后刷新即可
```python
from your_project.settings import appkey, appsecret, agent_id
from dingtalk_sdk_gmdzy2010.authority_request import AccessTokenRequest


params = {"appkey": settings.appkey, "appsecret": settings.appsecret}
request = AccessTokenRequest(params=params)
request.get_json_response()
access_token = request.get_access_token()
print(access_token)
```
-------------------------------------------------------------------------------

###### STEP 2. 递归遍历部门成员
钉钉官方接口没有提供按名称获取各级部门ID的接口，所以我们只能按子部门逐级递归获取部门ID   

以下示例代码获取到`科技服务事业部`的所有子部门（包括子部门的子部门）的成员
```python
from dingtalk_sdk_gmdzy2010.department_request import (
    DeptsRequest, SubDeptIdsRequest, DeptUsersSimpleRequest
)


def recruit_dept_ids(init_ids=None, total_ids=None, access_token=None):
    if init_ids:
        sub_level_ids = []
        for id in init_ids:
            params = {"access_token": access_token, "id": id}
            get_new_ids = SubDeptIdsRequest(params=params)
            get_new_ids.get_json_response()
            new_ids = get_new_ids.get_sub_dept_ids()
            sub_level_ids.extend(new_ids)
            if not new_ids:
                continue
        total_ids.extend(sub_level_ids)
        return recruit_dept_ids(init_ids=sub_level_ids, total_ids=total_ids,
                                access_token=access_token)
    else:
        return total_ids


def get_sub_dept_users(dept_ids=None):
    if dept_ids:
        dept_users = []
        for id in dept_ids:
            params = {"access_token": access_token, "department_id": id}
            get_users = DeptUsersSimpleRequest(params=params)
            get_users.get_json_response()
            users = get_users.get_dept_users_brief()
            dept_users.extend(users)
        return dept_users


get_level_2_depts_params = {
    "access_token": access_token,
    "id": 1,
    "fetch_child": False,
}
get_level_2_depts = DeptsRequest(params=get_level_2_depts_params)
get_level_2_depts.get_json_response()

# 以下get_depts方法在0.2.4版本才有
level_2_depts = get_level_2_depts.get_depts(dept_name="科技服务事业部")
sub_dept_ids = recruit_dept_ids(init_ids=[level_2_depts["id"]],
                                total_ids=[level_2_depts["id"]],
                                access_token=access_token)
sub_dept_users = get_sub_dept_users(dept_ids=sub_dept_ids)
print(sub_dept_users)
```
-------------------------------------------------------------------------------

###### STEP 3. 发送钉钉工作通知

以下示例代码将工作通知发送至相应ID（user_id）的成员，注意data的userid_list字段传入的是一个成员id列表，实际使用时直接传入要发送的成员即可

```python
from dingtalk_sdk_gmdzy2010.message_request import WorkNoticeRequest


user_id = "0000000000"
params = {"access_token": access_token}
data = {
    "agent_id": settings.agent_id,
    "userid_list": user_id,
    "msg": {
        "msgtype": "text",
        "text": {
            "content": "【测试通知】测试消息"
        }
    }
}
request = WorkNoticeRequest(params=params, json=data)
request.request_method = "post"
request.get_json_response()
response = request.json_response
print(response)
```
-------------------------------------------------------------------------------

###### STEP 4. 查询发送进度与结果
待续

```python
# to be continued...

```

-------------------------------------------------------------------------------

