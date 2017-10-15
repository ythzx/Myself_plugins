from django.shortcuts import render, HttpResponse, redirect
import json
from BookManager import models
from BookManager import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# def publisher(request):
#     publisher_list = models.Publisher.objects.all()
#     """
#     使用Django内部的序列化
#     from django.core import serializers
#     data = serializers.serialize('json',publisher_list) # 序列化成json数据
#     return HttpResponse(data,content_type='application/json')
#     """
#     from BookManager import serializers
#     serializer = serializers.PublisherSerializers(publisher_list,many=True) # many=True 代表的是多个对象
#     return HttpResponse(json.dumps(serializer.data),content_type='application/json') # 内部把通过json序列化后再返回
#

#
# @api_view(['GET', 'POST'])
# def publisher_list(request):
#     """
#     GET:获取所有的出版社，
#     POST：创建一个新的出版社
#     """
#     if request.method == 'GET':
#         query = models.Publisher.objects.all()
#         serializer = serializers.PublisherSerializers(query, many=True)  # 序列化数据 many=True 将所有的数据序列化
#         return Response(serializer.data)  # 通过response返回
#     elif request.method == "POST":
#         """创建数据"""
#         serializer = serializers.PublisherSerializers(data=request.data)  # 创建数据的时候 data是请求传递过来的数据
#         if serializer.is_valid():
#             serializer.save()  # 验证成功保存数据
#             # 创建成功后返回json数据，状态码用rest framework中自带的，创建成功返回HTTP_201_CREATED
#             return Response(serializer.data, status=status.HTTP_201_CREATED)  # 状态码status需要从rest_frame中导入
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # 没有通过验证，将错误信息序列化 返回400
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def publish_detail(request,pk):
#     """
#     获取、更新、删除一个实例的信息
#     :param request:
#     :return:
#     """
#     try:
#         publisher = models.Publisher.objects.get(pk=pk)
#     except models.Publisher.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND) # 不存在返回404
#
#     if request.method == 'GET':
#         serializer = serializers.PublisherSerializers(publisher) # 查询当前实例的信息
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = serializers.PublisherSerializers(publisher, data=request.data)
#         if serializer.is_valid():
#             serializer.save() # 验证成功后保存
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         publisher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


"""
基于类的视图
"""
#
# from rest_framework.views import APIView
# from django.http import Http404
#
#
# class Publisher_list(APIView):
#     """
#     列出所有的snippets或者创建一个新的snippet。
#     """
#
#     def get(self, request, format=None):
#         """
#         Get 请求
#         """
#         query = models.Publisher.objects.all() # 获取所有的数据
#         serializer = serializers.PublisherSerializers(query, many=True) # 将数据序列化
#         return Response(serializer.data) # 通过Response将数据返回
#
#     def post(self, request, format=None):
#         """
#         POST 请求
#         """
#         serializer = serializers.PublisherSerializers(data=request.data) # 增加数据
#         if serializer.is_valid():
#             serializer.save() # 验证通过后保存
#             return Response(serializer.data, status=status.HTTP_201_CREATED) # 成功后返回HTTP_201_CREATED
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 失败后返回400
#
#
# class PublisherDetail(APIView):
#     """
#     检索，更新或删除一个示例。
#     """
#
#     def get_object(self, pk):
#         """
#         先判断是否有这个对象，有就直接返回
#         没有就抛出异常 Http404
#         """
#         try:
#             return models.Publisher.objects.get(pk=pk)
#         except models.Publisher.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         publisher = self.get_object(pk) # 要获取的对象
#         serializer = serializers.PublisherSerializers(publisher) # 将获取对象的数据序列化
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         publisher = self.get_object(pk) # 要获取的对象
#         serializer = serializers.PublisherSerializers(publisher, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         publisher = self.get_object(pk) # 要获取的对象
#         publisher.delete() # 通过对象删除数据
#         return Response(status=status.HTTP_204_NO_CONTENT)

"""
基本混合型
"""

# from rest_framework import mixins
# from rest_framework import generics
#

# class Publisher_list(mixins.ListModelMixin,
#                      mixins.CreateModelMixin,
#                      generics.GenericAPIView):
#     """
#     ListModelMixin 列出查询的内容
#     CreateModelMixin 创建新的信息
#     generics.GenericAPIView 包含的是通用的
#     """
#     queryset = models.Publisher.objects.all()
#     serializer_class = serializers.PublisherSerializers # serializer_class 不能修改
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)  # self.list 调用ListModelMixin中的方法
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)  # # self.create 调用ListModelMixin中的方法
#
#
# class PublisherDetail(mixins.RetrieveModelMixin,
#                       mixins.UpdateModelMixin,
#                       mixins.DestroyModelMixin,
#                       generics.GenericAPIView):
#     queryset = models.Publisher.objects.all()
#     serializer_class = serializers.PublisherSerializers
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

"""
封装的混合mins使用
"""
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
