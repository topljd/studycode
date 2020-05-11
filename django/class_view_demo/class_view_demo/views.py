from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View,TemplateView
def index(request):

    return HttpResponse('index')

#输入 http://127.0.0.1:8000/book/ 同样会显示 book_list
class BookListView(View):
    def get(self,request,*args,**kwargs):
        #**kwargs  所有的关键字字段
        return HttpResponse('book_list')

class AddBookView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'add_book.html')
    def post(self,request,*args,**kwargs):
        #使用post提交的时候需要将csrf验证关闭掉
        book_name = request.POST.get('name')
        book_author = request.POST.get('author')
        print('name:{},author:{}'.format(book_name,book_author))
        return HttpResponse('success')

class BookDetailView(View):
    def get(self,request,book_id):
        print('图书的id是：%s' %book_id)
        return HttpResponse('bookdetailview')

    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse('不支持get以外的其他请求')

    #类似图首先会请求dispath方法，然后在根据不同的请求分配给其他方法
    def dispath(self,request,*args,**kwargs):
        print('dispath')
        return super(BookDetailView, self).dispath(request,*args,**kwargs)

class AboutView(TemplateView):
    template_name= 'about.html'
    def get_context_data(self,**kwargs):
        context ={
            'phone':'0523-8888888'
        }
        return context
