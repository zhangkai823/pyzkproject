# 引入路由函数
from django.conf.urls import url
# 引入views文件
from . import views
# 每一个路由文件必须编写路由数组

app_name = "booktest"

urlpatterns = [
    # 以空开头 以空结尾  不需要打index 直接进入首页
    url(r'^$',views.index,name='index'),
    url(r'detail/(\d+)/',views.detail,name='detail'),
    url(r'^about/$',views.about,name='about'),
    url(r'^delete/(\d+)/$',views.detele,name='delete'),
    url(r'^deletehero/(\d+)/$',views.deletehero,name='deletehero'),
    url(r'^addhero/(\d+)/$', views.addhero,name='addhero'),
    url(r'^edithero/(\d+)/$',views.edithero,name='edithero')

]