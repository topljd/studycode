from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Person,Author
from django.utils.timezone import now,localtime
#localtime可以根据timezone时间转换
# Create your views here.
def index(request):
    # import pytz
    # from datetime import datetime
    # now = datetime.now()
    # utc_timezone = pytz.timezone("UTC")
    # utc_now = now.astimezone(utc_timezone)
    # print(utc_now)#2020-04-06 10:20:42.961093+00:00

    #插入了两条数据
    # # article = Article(title='abc',create_time=now())
    # # article.save()
    #
    # article = Article.objects.get(pk=7)
    # #如果数据库中没有id =7 的数据就会报错
    # create_time = article.create_time
    # print('='*30)
    # print(create_time)
    # print(localtime(create_time))
    # print('=' * 30)
    # '''
    # ==============================
    # 2020-04-08 08:37:06.122458+00:00
    # [08/Apr/2020 16:45:04] "GET / HTTP/1.1" 200 7
    # 2020-04-08 16:37:06.122458+08:00
    # ==============================
    # '''
    # #return HttpResponse('success')
    # context = {
    #     'create_time':create_time,
    # }
    #
    # return  render(request,'index.html',context=context)
    article = Article(title='bcd')
    article.save()
    return HttpResponse('success')
def email_view(request):
    p = Person(email = 'aaaaa')
    p.save()
    return HttpResponse('Email')

def null_text_field(request):
    author = Author()
    author.save()
    return HttpResponse('null')

def order_view(request):
    authors = Author.objects.all()
    for author in authors:
        print(author)
    return HttpResponse('success')