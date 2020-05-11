from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Category  #导入article数据表
def index(request):
    # articles = Article.objects.all()
    # for article in articles:
    #     print(article.title)
    article = Article.objects.filter(id__exact=1)
    #  __exact这个写不写其实是无所谓的

    print(article.query)#输出Query语句
    #SELECT `article`.`id`, `article`.`title`, `article`.`content` FROM `article` WHERE `article`.`id` = 1

    article1 = Article.objects.filter(title__exact='Helloworld')
    print(article1.query)
    #SELECT `article`.`id`, `article`.`title`, `article`.`content` FROM `article` WHERE `article`.`title` = helloworld

    article2 = Article.objects.filter(title__exact=None)
    print(article2.query)
    #SELECT `article`.`id`, `article`.`title`, `article`.`content` FROM `article` WHERE `article`.`title` IS NULL

    article3 = Article.objects.filter(title__iexact='helloworld')
    print(article3.query)


    return HttpResponse('success')
def index1(request):
    #article = Article.objects.get(pk=1)
    #print(type(article))#<class 'front.models.Article'>

    article = Article.objects.filter(pk=1)
    #print(type(article))#<class 'django.db.models.query.QuerySet'>
    print(article.query)
    #SELECT `article`.`id`, `article`.`title`, `article`.`content` FROM `article` WHERE `article`.`id` = 1
    return HttpResponse('success')

def index2(request):
    article = Article.objects.filter(title__contains='Hello world')
    print(article.query)
    #SELECT `article`.`id`, `article`.`title`, `article`.`content` FROM `article` WHERE `article`.`title` LIKE BINARY %hello world%
    print(article)
    #<QuerySet [<Article: <Article:(title:hello world,content:你好世界！)>>]>

    article1 = Article.objects.filter(title__icontains='Hello')
    print(article1.query)
    # SELECT `article`.`id`, `article`.`title`, `article`.`content` FROM `article` WHERE `article`.`title` LIKE %Hello%
    print(article1)
    #<QuerySet [<Article: <Article:(title:hello world,content:你好世界！)>>]>

    return HttpResponse('success')

def index3(request):
    articles = Article.objects.filter(id__in=[1,2,3])
    for article in articles:
        print(article)
    '''
    <Article:(title:钢铁是怎样炼成的,content:XXX)>
    <Article:(title:中国高铁,content:高铁)>
    <Article:(title:hello world,content:你好世界！)>
    '''

    categories=Category.objects.filter(articles__id__in=[1,2,3])
    #如果写成article__in也表示article__id__in
    print(categories.query)
    #SELECT `category`.`id`, `category`.`name` FROM `category` INNER JOIN `article` ON (`category`.`id` = `article`.`category_id`) WHERE `article`.`id` IN (1, 2, 3)
    for category in categories:
        print(category)

    print('='*30)

    articles1 = Article.objects.filter(title__icontains='hello')
    categories1 = Category.objects.filter(articles__in=articles1)
    print(categories1.query)
    #SELECT `category`.`id`, `category`.`name` FROM `category` INNER JOIN `article` ON (`category`.`id` = `article`.`category_id`) WHERE `article`.`id` IN (SELECT U0.`id` FROM `article` U0 WHERE U0.`title` LIKE %hello%)
    for category in categories1:
        print(category)
    #Category object (2)
    return HttpResponse('success')

def index4(request):
    #查找id大于2的所有文章
    #gt: greater than 大于
    articles = Article.objects.filter(id__gt=2)
    print(articles)
    print(articles.query)
    #SELECT `article`.`id`, `article`.`title`, `article`.`content`, `article`.`category_id` FROM `article` WHERE `article`.`id` > 2

    #gte:greater than equal 大于等于
    articles1 = Article.objects.filter(id__gte=2)
    print(articles1)
    print(articles1.query)

    # lt:lower than 小于
    articles2 = Article.objects.filter(id__lt=2)
    print(articles2)
    print(articles2.query)
    #SELECT `article`.`id`, `article`.`title`, `article`.`content`, `article`.`category_id` FROM `article` WHERE `article`.`id` < 2

    # lte:lower than equal 小于等于
    articles3 = Article.objects.filter(id__lte=2)
    print(articles3)
    print(articles3.query)
    #SELECT `article`.`id`, `article`.`title`, `article`.`content`, `article`.`category_id` FROM `article` WHERE `article`.`id` <= 2


    return HttpResponse('index4')

def index5(request):
    #startswith 以什么开头，对大小写敏感
    article = Article.objects.filter(title__startswith='hello')
    print(article)
    print(article.query)
    #SELECT `article`.`id`, `article`.`title`, `article`.`content`, `article`.`category_id` FROM `article` WHERE `article`.`title` LIKE BINARY hello%

    # istartswith 以什么开头，对大小写不敏感 i ignore忽略
    article1 = Article.objects.filter(title__istartswith='Hello')
    print(article1)
    print(article1.query)
    #SELECT `article`.`id`, `article`.`title`, `article`.`content`, `article`.`category_id` FROM `article` WHERE `article`.`title` LIKE Hello%

    #endswith：以什么结尾，对大小写敏感
    article2 = Article.objects.filter(title__endswith='world')
    print(article2)
    print(article2.query)
    #SELECT `article`.`id`, `article`.`title`, `article`.`content`, `article`.`category_id` FROM `article` WHERE `article`.`title` LIKE BINARY %world

    #iendswith：以什么结尾，对大小不敏感
    article3 = Article.objects.filter(title__iendswith='woRld')
    print(article3)
    print(article3.query)
    #SELECT `article`.`id`, `article`.`title`, `article`.`content`, `article`.`category_id` FROM `article` WHERE `article`.`title` LIKE %woRld
    return HttpResponse('index5')
from datetime import datetime,time
from django.utils.timezone import make_aware
def index6(request):
    start_time = make_aware(datetime(year=2020,month=4,day=11,hour=5,minute=0,second=0))
    #end_time = datetime(year=2020,month=4,day=11,hour=17,minute=52,second=0)
    end_time = make_aware(datetime(year=2020,month=4,day=11,hour=17,minute=52,second=0))
    articles =Article.objects.filter(create_time__range=(start_time,end_time))
    print(articles.query)
    #SELECT `article`.`id`, `article`.`title`, `article`.`content`, `article`.`category_id`, `article`.`create_time` FROM `article` WHERE `article`.`create_time` BETWEEN 2020-04-10 21:00:00 AND 2020-04-11 09:52:00
    print(articles)
    #<QuerySet [<Article: <Article:(title:钢铁是怎样炼成的,content:XXX)>>]>返回数据

    return HttpResponse('index6')

def index7(request):
    articles = Article.objects.filter(create_time__date=datetime(year=2020,month=4,day=11))
    print(articles.query)
    #SELECT `article`.`id`, `article`.`title`, `article`.`content`, `article`.`category_id`, `article`.`create_time` FROM `article` WHERE DATE(CONVERT_TZ(`article`.`create_time`, 'UTC', 'Asia/Shanghai')) = 2020-04-10
    print(articles)

    articles1 = Article.objects.filter(create_time__year=2020)
    #articles1 = Article.objects.filter(create_time__year__gte=2020)
    #gte表示大于等于2020年的都可以
    #SELECT `article`.`id`, `article`.`title`, `article`.`content`, `article`.`category_id`, `article`.`create_time` FROM `article` WHERE `article`.`create_time` BETWEEN 2019-12-31 16:00:00 AND 2020-12-31 15:59:59.999999
    print(articles1.query)
    print(articles1)


    articles2 = Article.objects.filter(create_time__week_day=7)
    print(articles2.query)
    #SELECT `article`.`id`, `article`.`title`, `article`.`content`, `article`.`category_id`, `article`.`create_time` FROM `article` WHERE DAYOFWEEK(CONVERT_TZ(`article`.`create_time`, 'UTC', 'Asia/Shanghai')) = 7
    print(articles2)
    #<QuerySet [<Article: <Article:(title:钢铁是怎样炼成的,content:XXX)>>, <Article: <Article:(title:中国高铁,content:高铁)>>, <Article: <Article:(title:hello world,content:你好世界！)>>, <Article: <Article:(title:最新电影分析,content:222)>>]>

    start_time = time(hour=21,minute=46,second=21)
    end_time = time(hour=21,minute=46,second=22)
    articles3 = Article.objects.filter(create_time__time__range=(start_time,end_time))
    print(articles3.query)
    print(articles3)


    return HttpResponse('index7')

def index8(request):
    articles = Article.objects.filter(create_time__isnull=False)#True
    #SELECT `article`.`id`, `article`.`title`, `article`.`content`, `article`.`category_id`, `article`.`create_time` FROM `article` WHERE `article`.`create_time` IS NULL
    print(articles.query)
    print(articles)

    articles1 = Article.objects.filter(title__regex=r'^hello')
    #大小写区分
    print(articles1.query)
    #SELECT `article`.`id`, `article`.`title`, `article`.`content`, `article`.`category_id`, `article`.`create_time` FROM `article` WHERE `article`.`title` REGEXP BINARY ^hello
    print(articles1)

    return HttpResponse('index8')