from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.views.generic import ListView
# Create your views here.
def add_article(request):
    articles =['article1','article2']
    print(articles)
    # for x in range(0,102):
    #     article = Article(title='标题：%s'%x,content='内容：%s'%x)
    article1 = Article(title='标题：123', content='内容：abc')
    articles.append(article1)
    article2 = Article(title='标题：345', content='内容：3c')
    articles.append(article2)
    print(articles)
    #     articles.append(article)
    #     print(article)
    #Article.objects.bulk_create(articles)

    return HttpResponse('success')

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    content_object_name ='articles'
    paginate_by = 10
    ordering = 'create_time'
    page_kwarg = 'p'


