from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category =models.ForeignKey("Category",on_delete=models.CASCADE,null=True,related_query_name='articles')
    create_time = models.DateTimeField(auto_now_add=True,null=True)
    #保存的时候直接输入创建时间
    def __str__(self):
        return"<Article:(title:%s,content:%s)>"%(self.title,self.content)

    class Meta:
        db_table = 'article'
    #如果没有这个类 则生成 front_article数据表
    # 有Meta这个类就会生成 article这个名字的表



