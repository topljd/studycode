from django.db import models

# Create your models here.
#如果要将一个普通的类变成一个可以映射到数据库中的模型
#那么必须要将父类设置为models.Model或者其他的子类
class Book(models.Model):
    #1、id：int类型自增长
    id = models.AutoField(primary_key = True)#自动增长，主键
    #2、name：varchar(100)图书的名字
    name = models.CharField(max_length=100,null=False)#长度最长不超过100,不能为空
    #3、author：varchar(100) 图书的作者
    author = models.CharField(max_length=100,null=False)
    #4、price:float 图书的价格
    price = models.FloatField(null=False,default=0)#不能为空，默认为0
#对应好了之后就要映射到数据库,添加app到installed_apps中
#python manage.py makemigrations 使用makemigrations生成迁移脚本文件
#python manage.py migrate 使用migrate将文件生成的迁移脚本文件映射到数据库中

class Publisher(models.Model):
    #默认生成id主键的
    name = models.CharField(max_length=100,null=False)
    address = models.CharField(max_length=100,null=False)
    #python manage.py makemigrations
    #python manage.py migrate



