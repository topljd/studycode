from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
# Create your views here.
def index(request):
    #1.使用ORM添加一条数据到数据库中
    # book = Book(name='西游记',author='吴承恩',price=100)
    # book.save()
    # return HttpResponse("书籍添加成功")

    #2、查询
    #2.1根据主键进行查找
    #primary key 简称pk pk = 1 也可以写成id = 1
    # book = Book.objects.get(pk=2)
    # print(book)#Book object (1)

    #2.2根据其他条件进行查找
    #book = Book.objects.filter(name='西游记')  #返回全部为西游记的书籍
    #<QuerySet [<Book: <Book:(西游记,吴承恩,100.0)>>]>
    # book = Book.objects.filter(name='西游记').first()
    # #返回第一条 <Book:(西游记,吴承恩,100.0)>
    # print(book)

    #3.删除数据
    # book = Book.objects.get(pk=1)
    # book.delete()

    #4、修改数据
    book = Book.objects.get(pk=2)
    book.price = 200
    book.save()
    return HttpResponse('图书修改成功')