from django.db import models

# Create your models here.
class Book(models.Model):
    #id会自动生成的 主键 自增
    name = models.CharField(max_length=100,null=False)
    author = models.CharField(max_length=100,null=False)
    price = models.FloatField(default=0)

    def __str__(self):
        #<Book:(name,author,price)>
        return '<Book:({name},{author},{price})>'.format(name=self.name,author=self.author,price=self.price)


#迁移文件 python manage,py makemigrations
#生成到数据库中 python manage.py migrate
