from django.db import models

# Create your models here.
class Article(models.Model):
    #付过想要使用自己定义的Field来作为主键，那么必须设置primary_key=True
    id = models.BigAutoField(primary_key = True)

    #BooleanField 布尔类型
    #如果没有指定null=True，那么默认情况下，null=False
    #就是不能为空null
    #如果想要使用可以为null的BooleanField，那么使用NullBooleanField来代替
    #removed = models.BooleanField()
    removed = models.NullBooleanField()#改过字段要重新映射
    #charField如果是超过了254个字符就不建议使用了
    #就推荐使用TextField：longtext
    title = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)
    #自动获取当前对象auto_now_add=True
    #创建时间 auto_now_add=True 是在第一次添加数据进去的时候会自动获取当前的时间
    #更新时间 auto_now =True:每次这个对象条用save方法的时候都会将当前的方法更新
#python manage.py makemigrations
#migrate
class Person(models.Model):
    #ModelForm后面会根据模型生成表单，可判断是什么样的样式
    #EmailField在数据库层面并不会限制字符串一定要满足邮箱格式
    #只是以后再使用modelForm等表单相关操作的时候回起作用
    email = models.EmailField(max_length=200)
    #如果没有传max_lengh默认是254
    #创建了article_person表
    signature = models.TextField()

class Author(models.Model):
    username = models.CharField(max_length=100,null=True)#默认不能为空
    age = models.IntegerField(null = True)
    #db_column='author_age'加入这个参数，就会将数据表中的age改变为author_age
    #在类里面进行定义Meta类 Rename table for author to author
    def __str__(self):
        return "<(Author id:%s ,username:%s)>" % (self.id,self.username)
    class Meta:
        db_table = 'author'
        ordering = ['id']#可以多个参数
