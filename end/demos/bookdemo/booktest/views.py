from django.shortcuts import render,redirect,reverse
from django.template import loader
from .models import Book,Hero
# Create your views here.

# 编写对应的视图函数
from django.http import HttpResponse,HttpResponseRedirect

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

def detele(request,bookid):
    book = Book.objects.get(id=bookid)
    book.delete()
    return HttpResponseRedirect(redirect_to="/")

def deletehero(request,heroid):
    hero = Hero.objects.get(id=heroid)
    bookid = hero.book.id
    hero.delete()
    url = reverse("booktest:detail",args=(bookid,))
    return redirect(to=url)


def edithero(request,heroid):
    hero = Hero.objects.get(id=heroid)
    if request.method == 'GET':
        return render(request,'edithero.html',{'hero':hero})
    elif request.method == 'POST':
        hero.name = request.POST.get('heroname')
        hero.content = request.POST.get("herocontent")
        hero.gender = request.POST.get("sex")
        hero.save()
        url = reverse("booktest:detail",args=(hero.book.id,))
        return redirect(url)




def addhero(request,bookid):
    if request.method == 'GET':
        return render(request,'addhero.html')
    elif request.method == 'POST':
        hero = Hero()
        hero.name = request.POST.get("heroname")
        hero.content = request.POST.get("herocontent")
        hero.gender = request.POST.get("sex")
        hero.book = Book.objects.get(id=bookid)
        hero.save()
        url = reverse("booktest:detail",args=(bookid,))
        return redirect(to=url)



def addbook(request):
    if request.method == 'GET':
        return render(request,'addbook.html')
    elif request.method == 'POST':
        book = Book()
        book.title = request.POST.get("booktitle")
        book.price = request.POST.get("bookprice")
        book.pub_date = request.POST.get("booktime")
        book.save()
        return redirect(to='/')


def editbook(request,bookid):
    book = Book.objects.get(id=bookid)
    if request.method == 'GET':
        return render(request,'editbook.html',{'book':book})
    elif request.method == 'POST':
        book.title = request.POST.get("booktitle")
        book.price = request.POST.get("bookprice")
        book.pub_date = request.POST.get("booktime")
        book.save()
        return redirect(to='/')



def about(request):
    return HttpResponse("这里是关于")