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

@api_view(['GET', 'POST'])
def publisher_list(request):
    """
    GET:获取所有的出版社，
    POST：创建一个新的出版社
    """
    if request.method == 'GET':
        query = models.Publisher.objects.all()
        serializer = serializers.PublisherSerializers(query, many=True)  # 序列化数据 many=True 将所有的数据序列化
        return Response(serializer.data)  # 通过response返回
    elif request.method == "POST":
        """创建数据"""
        serializer = serializers.PublisherSerializers(data=request.data)  # 创建数据的时候 data是请求传递过来的数据
        if serializer.is_valid():
            serializer.save()  # 验证成功保存数据
            # 创建成功后返回json数据，状态码用rest framework中自带的，创建成功返回HTTP_201_CREATED
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # 状态码status需要从rest_frame中导入
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # 没有通过验证，将错误信息序列化 返回400


@api_view(['GET', 'PUT', 'DELETE'])
def publish_detail(request,pk):
    """
    获取、更新、删除一个实例的信息
    :param request:
    :return:
    """
    try:
        publisher = models.Publisher.objects.get(pk=pk)
    except models.Publisher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) # 不存在返回404

    if request.method == 'GET':
        serializer = serializers.PublisherSerializers(publisher) # 查询当前实例的信息
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.PublisherSerializers(publisher, data=request.data)
        if serializer.is_valid():
            serializer.save() # 验证成功后保存
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
