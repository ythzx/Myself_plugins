
## 序列化

在app BookManager中创建serializers用于序列化，类似ModleForm的操作

## 请求和响应

`@api_view`

### 使用httpie模块测试

安装`httpie`模块 ,通过httpie模块发送请求  
- 这种请求会返回403，但是自己测试的时候返回全部的数据 http http://127.0.0.1:8000/publishers/
- 新建用户后通过密码进行请求 http -a admin:admin123  http://127.0.0.1:8000/publishers/
- 获取单一数据 http -a admin:admin123  http://127.0.0.1:8000/publishers/1/


```cython
HTTP/1.0 200 OK
Allow: OPTIONS, GET, POST
Content-Length: 160
Content-Type: application/json
Date: Sun, 15 Oct 2017 09:05:29 GMT
Server: WSGIServer/0.2 CPython/3.6.1
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

[
    {
        "address": "北京",
        "id": 1,
        "name": "北京出版社"
    },
    {
        "address": "上海",
        "id": 2,
        "name": "上海出版社"
    },
    {
        "address": "广州",
        "id": 3,
        "name": "广州出版社"
    }
]

```


### 创建用户

`python manage.py createsuperuser`   
用户名：admin
密码：admin123

### 登录

在哪url中配置之后，能够登录和注销,必选按照下面的方式写，`api-auth/`后面不要加`$`

`url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),`