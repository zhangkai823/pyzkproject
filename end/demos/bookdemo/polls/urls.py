# 引入路由函数
from django.conf.urls import url
# 引入views文件
from . import views
# 每一个路由文件必须编写路由数组

app_name = "polls"

urlpatterns = [
    # 以空开头 以空结尾  不需要打index 直接进入首页
    # 调用视图函数 直接调用 views.函数名
    # url(r'^pindex/$',views.pindex,name='pindex'),
    # 调用视图类 views.类名.as_view()  name 是解除硬编码所用的函数名
    # 解除硬编码 {% url 'polls:detail' 传递的参数 %}
    url(r'^pindex/$',views.IndexView.as_view(),name='pindex'),
    url(r'^pdetails/(\d)/$', views.pdetail, name='pdetails'),
    url(r'^result/(\d)/$', views.result, name='result'),
    # 调用视图类
    # url(r'^pdetails/(\d)/$',views.DetailsView.as_view(),name='pdetails'),
    url(r'^login/$',views.login,name='login'),
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^logout/$', views.logout, name='logout'),

]