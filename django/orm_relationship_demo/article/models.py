from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

#app.模型的名字
class Tag(models.Model):
    name = models.CharField(max_length=100)
    #标签名
    article = models.ManyToManyField("Article",related_name='tags')
    #会生成一个中间表


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey("Category",on_delete=models.CASCADE,null = True,related_name='articles')
    #cascade表示的是级别删除的意思 ForeignKey 表示外键
    author = models.ForeignKey("frontuser.FrontUser",on_delete=models.CASCADE,null = True)
        #models.PROJECT 等等
    def __str__(self):
        return '<Article:(id:%s,title:%s)>' % (self.id,self.title)
class Comment(models.Model):
    content = models.TextField()
    origin_comment = models.ForeignKey('self',on_delete=models.CASCADE)




#category: id ,name
#1,最新

#article
#id,title,category
#1,xxx,1