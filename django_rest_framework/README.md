
中文文档：https://q1mi.github.io/Django-REST-framework-documentation/

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

## 基于类的视图 混合使用mins

```cython
from rest_framework import generics


class Publisher_list(generics.ListCreateAPIView):
    """
    ListCreateAPIView 中就是继承ListCreateAPIView中的
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView
    """
    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherSerializers


class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherSerializers
```

## 权限

在表中新加一个字段的时候，原来表中有数据，在`makemigrations`的时候,选择添加默认值。然后执行`migrate`

同时需要在序列化中添加相应的字段`operator`

在views中增加`permission_classes = (permissions.IsAuthenticated,) `,增加权限认证，未登录不会返回信息

### 创建一个新的用户abc

`createsuperuser` 

用户名：abc   
密码：admin123

当用abc登录的时候是不能修改的，创建者admin能够修改

### 在视图中增加Books

```cython
class BookList(generics.ListCreateAPIView):
    """
    获取全部的书籍信息
    """
    queryset = models.Book.objects.all()
    serializer_class = serializers.BooksSerializers
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    获取某一本书的细节
    """
    queryset = models.Book.objects.all()
    serializer_class = serializers.BooksSerializers # 对书籍信息进行序列化
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

```

### 配置urls

配置书籍的urls
```cython
    url(r'^books/$', views.BookList.as_view()),
    url(r'^books/(?P<pk>[0-9]+)/$', views.BookDetail.as_view()),
```

## 超链接API


1、在Books的序列化中增加超链接API--HyperlinkedModelSerializer
2、在url中增加name属性，用于反向查找，否则超链接API会报错


### HyperlinkedModelSerializer

```cython
class BooksSerializers(serializers.HyperlinkedModelSerializer):
    """
    书籍的序列化
    其中publisher字段是
    HyperlinkedModelSerializer 是超链接API，同时要在URL中配置name反向查询的名字
    """
    # 使用超链接API将这个注释
    # publisher = serializers.StringRelatedField(source='publisher.name') # 将publisher显示成字符串 
```

### URL 

```cython
    url(r'^publishers/$', views.Publisher_list.as_view(),name='publisher-list'),
    url(r'^publishers/(?P<pk>[0-9]+)/$', views.PublisherDetail.as_view(),name='publisher-detail'),
    url(r'^books/$', views.BookList.as_view(),name='book-list'),
    url(r'^books/(?P<pk>[0-9]+)/$', views.BookDetail.as_view(),name='book-detail'),
```


