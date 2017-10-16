from rest_framework import serializers
from BookManager import models


# class PublisherSerializers(serializers.Serializer):
#     """
#     类似Form需要自己写字段
#     使用Django rest framework的序列化
#     继承serializers.Serializer
#     """
#     id = serializers.IntegerField(read_only=True)  # 主键自增ID
#     name = serializers.CharField(max_length=32)
#     address = serializers.CharField(max_length=128)
#
#     def create(self, validated_data):
#         """
#         增加数据
#         rest framework 类似Django的Form valid_data 代表验证成功的数据
#         :param validated_data:
#         :return:
#         """
#         return models.Publisher.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         更新数据
#         :param instance:
#         :param validated_data:
#         :return:
#         """
#         instance.name = validated_data.get('name', instance.name) # instance代表原来的
#         instance.address = validated_data.get('name', instance.address)
#         instance.save()
#         return instance


class PublisherSerializers(serializers.ModelSerializer):
    """
    序列化
    类似ModelForm的方式，不用自己写每一个字段
    根据原来写的model配合字段自动生成
    """
    operator = serializers.ReadOnlyField(source='operator.username')  # 重写operator的序列化方法，显示关联的用户名

    class Meta:
        model = models.Publisher  # 声明自己的models
        fields = (
            'id',
            'name',
            'address',
            'operator'
        )


class BooksSerializers(serializers.HyperlinkedModelSerializer):
    """
    书籍的序列化
    其中publisher字段是
    HyperlinkedModelSerializer 是超链接API，同时要在URL中配置name反向查询的名字
    """
    # 使用超链接API将这个注释
    # publisher = serializers.StringRelatedField(source='publisher.name') # 将publisher显示成字符串

    class Meta:
        model = models.Book
        fields = (
            'id',
            'title',
            'publisher',
        )
