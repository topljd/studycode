from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from article.models import Article,Tag

# Create your views here.
def index(request):
    # article = Article(title='abc',content='1234')
    # author = User.objects.create(username='zhiliao',password='12334')
    # article.author = author
    # article.save()
    article =Article.objects.first()
    tag1 = Tag.objects.create(name='python')
    tag2 = Tag.objects.create(name='php')
    article.tags.add(tag1,tag2)
    article.save()

    return HttpResponse('success')