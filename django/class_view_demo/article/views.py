from django.shortcuts import render,redirect,reverse
from .models import Article
from django.http import HttpResponse
from django.views.generic import ListView,View
from django.core.paginator import Paginator,Page
from django.utils.decorators import method_decorator
# Create your views here.
def add_article(request):
    articles =[]
    print(articles)
    for x in range(0,102):
        article = Article(title='标题：%s'%x,content='内容：%s'%x)
        articles.append(article)
    Article.objects.bulk_create(articles)
    return HttpResponse('success')

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name ='articles'
    paginate_by = 10
    ordering = 'create_time'
    page_kwarg = 'p'
    def get_context_data(self,  **kwargs):
        #首先调用父类的方法
        context = super(ArticleListView, self).get_context_data(*kwargs)
        context['username'] = 'zhiliao'
        paginator = context.get('paginator')#获取这个类
        page_obj = context.get('page_obj')
        print(page_obj.has_next())#False


        print(paginator.count)#会打印出总计102条
        print(paginator.num_pages)#总计有11页
        print(paginator.page_range)#range(1, 12)
        pagination_data = self.get_pagination_data(paginator,page_obj)
        context.update(pagination_data)#将字段自动放入context字典中
        return context

    #def get_queryset(self):
        #return Article.objects.filter(id__lte=9)
    #只会返回9以内的数据


    #自定义的函数
    def get_pagination_data(self,paginator,page_obj,around_count=2):
        #获取当前的页码
        current_page = page_obj.number
        num_pages = paginator.num_pages
        left_has_more = False
        right_has_more = False
        if current_page <= around_count+2:
            left_pages = range(1,current_page)
        else:
            left_has_more = True
            left_pages = range(current_page-around_count,current_page)#左边两条数据

        if current_page >= (num_pages -around_count-1):
            right_pages = range(current_page+1,num_pages+1)
        else:
            right_has_more = True
            right_pages = range(current_page+1,current_page+around_count+1)#右边的两条数据
        return {
            'left_pages':left_pages,
            'right_pages':right_pages,
            'current_page':current_page,
            'left_has_more':left_has_more,
            'right_has_more':right_has_more,
        }


#登录验证
def login_required(func):
    def wrapper(request,*args,**kwargs):
        #?username=zhiliao
        username = request.GET.get('username')
        if username:
            return func(request,*args,**kwargs)
        else:
            return redirect(reverse('article:login'))
    return wrapper

@method_decorator(login_required,name='dispatch')#装饰器
class ProfileView(View):
    def get(self,request):
        return HttpResponse('个人中心界面')

    # @method_decorator(login_required)#装饰器
    # def dispatch(self, request, *args, **kwargs):
    #     #调用父类
    #     return super(ProfileView,self).dispatch(request,*args,**kwargs)

def login(request):
    return HttpResponse('login')