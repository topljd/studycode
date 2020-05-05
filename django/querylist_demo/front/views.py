from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #print(type(request.GET))
    #print(type(request.POST))
    '''
    <class 'django.http.request.QueryDict'>
    <class 'django.http.request.QueryDict'>
    '''
    #username = request.GET['username']
    #上面这个方法没有值就会报错，下面这个直接返回None
    #username = request.GET.get('uwername')
    username =request.GET.get('username',default='topljd')
    #topljd  如果没有username值，就默认返回topljd
    print(username)

    return HttpResponse('index1')
from django.views.decorators.http import require_http_methods
@require_http_methods(['GET','POST'])
def add_article(request):
    if request.method =='GET':
        return render(request,'add_article.html')
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        tags = request.POST.getlist('tags')
        print(f'title:{title},content{content},tags:{tags}')
        '''
        title:今日，为他们深切哀悼,contentbbb,tags:['python', 'Django']
        '''
        return HttpResponse('success')