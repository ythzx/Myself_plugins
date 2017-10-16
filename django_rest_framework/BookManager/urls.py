from django.conf.urls import url,include
from BookManager import views


urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^publishers/$', views.Publisher_list.as_view(),name='publisher-list'),
    url(r'^publishers/(?P<pk>[0-9]+)/$', views.PublisherDetail.as_view(),name='publisher-detail'),
    url(r'^books/$', views.BookList.as_view(),name='book-list'),
    url(r'^books/(?P<pk>[0-9]+)/$', views.BookDetail.as_view(),name='book-detail'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]