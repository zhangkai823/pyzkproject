from django.contrib import admin

# 定义后端显示界面

from django.contrib.admin import ModelAdmin

# Register your models here.

from .models import Book, Hero

# 定义关联类
class HeroInline(admin.StackedInline):
    """
    定义关联类
    """
    model = Hero
    extra = 1



class HeroAdmin(ModelAdmin):
    """
    定义模型管理类
    该类可以修改后台管理界面
    """
    list_display = ("name","gender","content","book")

class BookAdmin(ModelAdmin):
    """
    定义模型管理类
    该类可以修改后台管理界面
    """
    # 更改后端显示列
    list_display = ("title", "price", "pub_date")
    # 每页显示
    list_per_page = 1
    # 定义搜索字段
    search_fields = ("title","price")

    inlines = [HeroInline]


admin.site.register(Book,BookAdmin)
admin.site.register(Hero,HeroAdmin)
