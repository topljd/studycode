from django.shortcuts import render
from .models import Category,Article,Tag
from frontuser.models import FrontUser,UserExtension
from django.http import HttpResponse
# Create your views here.
def index(request):
    # category = Category(name='最新文章')
    # category.save()
    # article = Article(title='abc',content='123')
    # article.category = category
    # article.save()

    article = Article.objects.first()
    print(article.category.name)
    return HttpResponse('success')
def delete_view(request):
    category = Category.objects.get(pk = 1)
    category.delete()
    return HttpResponse('delete success')

def one_to_many_view(request):
    #1对多的关联操作
    # article = Article(title= '钢铁是怎样炼成的',content='abc')
    # category = Category.objects.first()
    # author = FrontUser.objects.first()  #获取第一条数据
    # article.category = category
    # article.author = author
    # article.save()
    # return HttpResponse('yes')

    # 2、获取分类下的所有文章
    category = Category.objects.first()#获取分类的第一条数据  这边就表示category_id 为2
    #RelatedManager
    #article = category.article_set.first()#获取所以的文章，也可.all()
    #articles = category.article_set.all()#获取所以的文章，也可.all()
    #因为使用了外键就会生成category.article_set属性


    #在models加入related_name ='articles' article_set属性将会失效使用下面的代码
    #articles = category.articles.all()
    # for article in articles:
    #     print(article)
    article = Article(title='aaa',content='123')
    article.author = FrontUser.objects.first()
    article.save()

    category.articles.add(article)
    #也可以添加多个数据
    #category.articles.add(article1,article2,bulk=False)
    category.save()

    articles = category.articles.all()  #查询category_id 为2的所有数据
    for article in articles:
        print(article)

    return HttpResponse('success')

def one_to_one_view(request):
    # user = FrontUser.objects.first()
    # #print(user.id,user.username)#1 李白
    # extension = UserExtension(school ='清华')
    # extension.user = user
    # extension.save()

    #extension = UserExtension.objects.first()
    #print(extension.user)#<FrontUser:(id:1,username:李白)

    user = FrontUser.objects.first()
    #print(user.userextension)#这里的数据是根据user里面的数据提取的，因为是11对应

    #在models中定义了related_name= 'extension'
    print(user.extension)#此时userextension将会报错


    return HttpResponse('success')

def many_to_many_view(request):
    # article = Article.objects.first()
    # tag = Tag(name='冷门文章')
    # tag.save()
    # article.tag_set.add(tag)

    # tag = Tag.objects.get(pk=1)
    # article = Article.objects.get(pk=11)
    # tag.article.add(article)

    article = Article.objects.get(pk=11)
    tags = article.tags.all()
    for tag in tags:
        print(tag)


    return HttpResponse('sucess')