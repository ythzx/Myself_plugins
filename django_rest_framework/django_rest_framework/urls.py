"""django_rest_framework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from BookManager import views


# 基于函数的视图url
# urlpatterns = [
#
#     url(r'^publishers/$', views.publisher_list),
#     url(r'^publishers/(?P<pk>[0-9]+)/$', views.publish_detail),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     url(r'^admin/', admin.site.urls),
# ]

# 基于类的视图的url 调用了as_view方法
urlpatterns = [

    url(r'^publishers/$', views.Publisher_list.as_view()),
    url(r'^publishers/(?P<pk>[0-9]+)/$', views.PublisherDetail.as_view()),
    url(r'^books/$', views.BookList.as_view()),
    url(r'^books/(?P<pk>[0-9]+)/$', views.BookDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]