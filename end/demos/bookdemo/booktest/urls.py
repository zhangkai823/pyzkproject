# 引入路由函数
from django.conf.urls import url
# 引入views文件
from . import views
# 每一个路由文件必须编写路由数组
urlpatterns = [
    url(r'^index/$',views.index),
    url(r'detail/(\d+)/',views.detail),
    url(r'^about/$',views.about)
]