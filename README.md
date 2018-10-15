## 钉钉`非官方版`SDK

### 项目简介
--------------------  
本SDK非官方提供，代码简单，同时不必担心在SDK当中有什么恶意代码。   
钉钉官方只提供了java，node.js以及php版sdk，python版没有？恰好最近业务需要，遂准备给钉钉写一整套SDK，不过钉钉的全部API有200+，测试是个大工程，其中很多业务用不上，所以先把基本的功能实现，后续的更新会把所有的功能陆陆续续补全，放出更新计划   

### 使用帮助
1.[SDK文档](https://github.com/gmdzy2010/dingtalk_sdk_gmdzy2010/blob/master/docs.md)        
2.[使用示例](https://github.com/gmdzy2010/dingtalk_sdk_gmdzy2010/blob/master/doc_for_bms.md)      
    
### 目前进度
--------------------  
#### 用户认证

|接口名称|已完成/总数|  
|:---|:---:|  
|用户认证|1/1|  
    
    
#### 通讯录管理

|接口名称|已完成/总数|  
|:---|:---:|  
|通讯录权限范围|1/1|  
|用户管理|5/12|  
|部门管理|4/9|  
|角色管理||  
|外部联系人管理||  
|通讯录同步方案||  
    
    
#### 应用管理

|接口名称|已完成/总数|  
|:---|:---:|  
|应用管理|0/6|  
    
    
#### 消息通知

|接口名称|已完成/总数|
|:---|:---:|
|工作通知|3/3|
|群消息|5/5|
|普通消息|0/1|
|第三方个人应用发消息|0/1|
    
    
    
### 更新日志
--------------------  

#### v0.2.4 2018/10/15
1.更新所有类描述__doc__      
2.为目前版本的SDK写了所有文档

#### v0.2.3 2018/10/12
1.更新`DeptsRequest`模块按部门名称获取id的方法`get_depts`      
2.针对生产使用写了一个简单的[使用示例](https://github.com/gmdzy2010/dingtalk_sdk_gmdzy2010/blob/master/doc_for_bms.md)  

#### v0.2.2 2018/10/11
1.已发布至pypi，包名称`dingtalk-sdk-gmdzy2010`      
2.修复0.2.1发布版本settings模块导入的bug       

#### v0.2.1 2018/10/11
1.修复接口调用属性`call_status`总为否的bug    
2.更新README英文版文档   

#### v0.2.0 2018/10/10
1.修改接口的调用的逻辑，现在需要在类实例化的时候提供关键字参数    
2.完善__doc__注释   
3.`NEW!`新增群消息创建/修改/已读状态查询    
4.`NEW!`新增工作通知消息发送状态/结果查询    


### 致谢
--------------------     
感谢钉钉的官方文档，感谢大家的关注与耐心，当然还有自己的辛勤付出:)  
