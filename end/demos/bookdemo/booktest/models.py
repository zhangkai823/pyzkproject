from django.db import models


# Create your models here.

class Book(models.Model):
    """
    book继承了Model类
    """
    title = models.CharField(max_length=20)
    pub_date = models.DateField(default="1983-06-01")
    price = models.FloatField(max_length=100,default=100)

    def __str__(self):
        return self.title


class Hero(models.Model):
    """
    hero继承了Model
    """
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=7, choices=(('male', '男'), ('female', '女')), default='male')
    content = models.CharField(max_length=100)
    # book是一对多中的外键 on_delete代表删除主数据是如何做
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name="heros")

    def __str__(self):
        return self.name

class UserManage(models.Manager):

    """
    自定义模型管理类
    该模型不再具有objects对象
    """
    # 自定义删除用户方法
    def deleteUser(self,tele):
        user = self.get(telephone = tele)
        user.delete()
    # 自定义创建用户方法
    def createUser(self,telephone):
        # self.model 可以获取模型类构造函数
        user = self.model()
        user.telephone = telephone
        user.save()





class User(models.Model):
    telephone = models.CharField(max_length=13,null=True,blank=True,verbose_name="手机号码")
    # 自定义管理字段之后不再有onjects对象 自定义了一个新的管理字段
    objects = UserManage()
    def __str__(self):
        return self.telephone
    class Meta:
        # 表名字
        db_table = "用户类"
        # 按照什么排序
        ordering = ["telephone"]
        # admin页面进入模型类显示名字
        verbose_name = "用户模型类"
        # admin 页面在应用下方显示的模型名
        verbose_name_plural = "用户模型类"


# 一找多  一方Book 实例b  多方 Hero 实例 h
# 一找多 b.hero_set.all()   如果定义过related_name = “heros”
# 则使用 b.heros.all
# 多找一 h.book、、、、



# 关联字段一对一
class Account(models.Model):
    username = models.CharField(max_length=20,verbose_name="用户名")
    password = models.CharField(max_length=20,verbose_name="密码")
    regist_date = models.DateField(auto_now_add=True,verbose_name="注册日期")

class Concact(models.Model):
    telephone = models.CharField(max_length=11,verbose_name="手机号")
    email = models.EmailField(default="2642990218@qq.com")
    # 定义关联字段
    account = models.OneToOneField(Account,on_delete=models.CASCADE,related_name="con")


class Article(models.Model):
    title = models.CharField(max_length=20, verbose_name="标题")
    sumary = models.TextField(verbose_name="正文")

class Tag(models.Model):
    name = models.CharField(max_length=10,verbose_name="标签名")
    articles = models.ManyToManyField(Article,related_name='tags')

