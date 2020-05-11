from django.shortcuts import render,redirect,reverse
from django.db import connection
# Create your views here.
def get_cursor():
    return connection.cursor()

def index(request):
    cursor = get_cursor()
    #cursor.execute("select id,name,author from book")
    #books = cursor.fetchall()
    #返回的是[(1,'三国演义,'罗贯中'),(2,)....]
    #cursor.execute("insert into book(id,name,author) values(null,'三国演义','罗贯中')")
    #可以插入数据，但是不能获取数据
    cursor.execute('select * from book')
    books = cursor.fetchall()
    context = {
        'books':books,
    }
    return render(request,'index.html',context=context)

def add_book(request):
    '''
    传参的时候注意数据的格式有无数据！
    '''
    if request.method =='GET':
        return render(request,'add_book.html')
    elif request.POST.get('name') and request.POST.get('author'):
        name = request.POST.get("name")
        author = request.POST.get("author")
        cursor = get_cursor()
        cursor.execute("insert into book(id,name,author) values(null,'%s','%s')"% (name,author))
        return redirect(reverse('index'))
    else:
        return render(request,'add_book.html')


def book_detail(request,book_id):
    cursor = get_cursor()
    cursor.execute("select id,name,author from book where id = %s "% book_id)
    book = cursor.fetchone()
    context = {
        'book':book,
    }
    return render(request,'book_detail.html',context=context)
def delete_book(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        cursor = get_cursor()
        cursor.execute("delete from book where id=%s "% book_id)
        return redirect(reverse('index'))
    else:
        raise RuntimeError("删除图书的method错误")