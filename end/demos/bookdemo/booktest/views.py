from django.shortcuts import render
from django.template import loader
from .models import Book
# Create your views here.

# 编写对应的视图函数
from django.http import HttpResponse

def index(request):
    # return HttpResponse("这里是首页")
    # 获取模板
    # template = loader.get_template('index.html')
    # 渲染模板数据
    books = Book.objects.all()
    context = {"books":books}
    # result = template.render(context)
    # 将渲染结果使用HttpResponse返回
    # return HttpResponse(result)
    return render(request,"index.html",{"books":books})
def detail(request,bookid):
    # template = loader.get_template('detail.html')
    book = Book.objects.get(id=bookid)
    # context = {"book":book}
    # result = template.render(context)
    # return HttpResponse(result)

    return render(request,"detail.html",{"book":book})
def about(request):
    return HttpResponse("这里是关于")