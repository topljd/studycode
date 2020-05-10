from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View
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
        return render(reque st,'add_book.html')