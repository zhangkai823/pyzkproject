"""bookdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


# 路由 网址 每一个网址都需要绑定视图 视图函数给予页面返回
# 每一个路由都需要绑定视图函数



urlpatterns = [
    path('admin/', admin.site.urls),
    # 使用path将booktest的路由进行包含
    path('booktest/',include('booktest.urls'))

]
