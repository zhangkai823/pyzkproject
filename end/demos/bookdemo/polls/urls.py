# 引入路由函数
from django.conf.urls import url
# 引入views文件
from . import views
# 每一个路由文件必须编写路由数组

app_name = "polls"

urlpatterns = [
    # 以空开头 以空结尾  不需要打index 直接进入首页
    url(r'^pindex/$',views.pindex,name='pindex'),
    url(r'^pdetails/(\d)/$', views.pdetail, name='pdetails'),
    url(r'^result/(\d)/$', views.result, name='result'),

]