from django.contrib import admin

# 定义后端显示界面

from django.contrib.admin import ModelAdmin

# Register your models here.

from .models import Book, Hero ,User

# 定义关联类
class HeroInline(admin.StackedInline):
    """
    定义关联类
    """
    model = Hero
    #添加一本书 需要添加几个人
    extra = 1



class HeroAdmin(ModelAdmin):
    """
    定义模型管理类
    该类可以修改后台管理界面
    """
    #后台显示列
    list_display = ("name","gender","content","book")
    # 定义后端搜索字段
    search_fields = ("name","gender","content")
    # 制定过滤字段
    list_filter = ("name","book")

admin.site.register(Hero,HeroAdmin)

class BookAdmin(ModelAdmin):
    """
    定义模型管理类
    该类可以修改后台管理界面
    """
    # 更改后端显示列
    list_display = ("title", "price", "pub_date")
    # 每页显示
    list_per_page = 9
    # 定义搜索字段
    search_fields = ("title","price","pub_date")

    inlines = [HeroInline]

admin.site.register(Book,BookAdmin)

admin.site.register(User)