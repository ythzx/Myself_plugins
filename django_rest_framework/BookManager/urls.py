from django.conf.urls import url, include
from BookManager import views

# 指定book_list book_detail 的各种方法，都是绑定到BookViewSet
book_list = views.BookViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
book_detail = views.BookViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^publishers/$', views.Publisher_list.as_view(), name='publisher-list'),
    url(r'^publishers/(?P<pk>[0-9]+)/$', views.PublisherDetail.as_view(), name='publisher-detail'),
    # url(r'^books/$', views.BookList.as_view(),name='book-list'),
    # url(r'^books/(?P<pk>[0-9]+)/$', views.BookDetail.as_view(),name='book-detail'),

    # 使用视图集合
    url(r'^books/$', book_list, name='book-list'),
    url(r'^books/(?P<pk>[0-9]+)/$', book_detail, name='book-detail'),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
