from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Author,BookOrder
from django.db.models import Avg,Count,Max,Min,Sum,F,Q
#导入求并均值的方法
from django.db import connection
def index(request):
    #获取所有图书定价的平均价格
    #result = Book.objects.aggregate(Avg("price"))
    result = Book.objects.aggregate(price_avg = Avg("price"))
    #price_avg 交做它的别名

    print(result)#result 是一个字典类型
    #{'price_avg': 97.25}
    #字典调用方法 如下：
    print(result['price_avg'])
    print(connection.queries)
    #[{'sql': 'SELECT @@SQL_AUTO_IS_NULL', 'time': '0.000'}, {'sql': 'SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED', 'time': '0.000'}, {'sql': 'SELECT AVG(`book`.`price`) AS `price__avg` FROM `book`', 'time': '0.000'}]
    #django在执行sql语句的时候执行了其他的语句
    return HttpResponse('success')

def index2(request):
    #我要获取每一本图书销售的平均价格

    #result = Book.objects.aggregate(avg=Avg('bookorder__price'))
    #print(result)#{'avg': 91.0}
    #print(connection.queries)
    #[{'sql': 'SELECT @@SQL_AUTO_IS_NULL', 'time': '0.000'}, {'sql': 'SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED', 'time': '0.000'}, {'sql': 'SELECT AVG(`book_order`.`price`) AS `avg` FROM `book` LEFT OUTER JOIN `book_order` ON (`book`.`id` = `book_order`.`book_id`)', 'time': '0.000'}]

    books = Book.objects.annotate(avg=Avg('bookorder__price'))
    print(books)
    #<QuerySet [<Book: Book object (1)>, <Book: Book object (2)>, <Book: Book object (3)>, <Book: Book object (4)>]>
    print('+'*40)
    for book in books:
        print('%s/%s' % (book.name,book.avg))
    '''
    三国演义/89.33333333333333
    水浒传/93.5
    西游记/None
    红楼梦/None
    '''
    print(connection.queries)
#{'sql': 'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, `book`.`publisher_id`, AVG(`book_order`.`price`) AS `avg` FROM `book` LEFT OUTER JOIN `book_order` ON (`book`.`id` = `book_order`.`book_id`) GROUP BY `book`.`id` ORDER BY NULL LIMIT 21'
# {'sql': 'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, `book`.`publisher_id`, AVG(`book_order`.`price`) AS `avg` FROM `book` LEFT OUTER JOIN `book_order` ON (`book`.`id` = `book_order`.`book_id`) GROUP BY `book`.`id` ORDER BY NULL'
    return HttpResponse('index2')

def index3(request):
    #book表中总共有多少本书，（book表中总共有多少个书）
    result = Book.objects.aggregate(book_nums=Count('id',distinct=True))
    #distinct=True 表示不统计重复的值
    print(result)
    #{'book_nums': 4}
    print(connection.queries)
    #[ {'sql': 'SELECT COUNT(`book`.`id`) AS `book_nums` FROM `book`', 'time': '0.031'}]

    result1 = Author.objects.aggregate(email_nums = Count('email',distinct=True))
    #'SELECT COUNT(DISTINCT `book`.`id`) AS `book_nums` FROM `book`', 'time': '0.000'}, {'sql': 'SELECT COUNT(DISTINCT `author`.`email`) AS `email_nums` FROM `author`', 'time': '0.000'}
    print(result1)
    print(connection.queries)


    #===annotate 先分组
    #统计每本书的销量
    books = Book.objects.annotate(book_nums=Count('bookorder'))#默认bookorder__id
    for book in books:
        print('%s/%s'% (book.name,book.book_nums))
    '''
    三国演义/3
    水浒传/2
    西游记/0
    红楼梦/0
    '''
    print(connection.queries)
    #{'sql': 'SELECT COUNT(DISTINCT `author`.`email`) AS `email_nums` FROM `author`', 'time': '0.000'}, {'sql': 'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, `book`.`publisher_id`, COUNT(`book_order`.`id`) AS `book_nums` FROM `book` LEFT OUTER JOIN `book_order` ON (`book`.`id` = `book_order`.`book_id`) GROUP BY `book`.`id` ORDER BY NULL'}]
    return HttpResponse('index3')

def index4(request):
    result = Author.objects.aggregate(max=Max('age'),min = Min('age'))
    print(result)
#{'max': 46, 'min': 28}
    print(connection.queries)
#'sql': 'SELECT MAX(`author`.`age`) AS `max`, MIN(`author`.`age`) AS `min` FROM `author`

    #获取每一本图书售卖的时候最大的价格和最小的价格
    books = Book.objects.annotate(max=Max('bookorder__price'),min =Min('bookorder__price'))
    for book in books:
        print('%s/%s/%s'%(book.name,book.max,book.min))
    '''
    三国演义/95.0/85.0
    水浒传/94.0/93.0
    西游记/None/None
    红楼梦/None/None
    '''
    print(connection.queries)
    #'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, `book`.`publisher_id`, MAX(`book_order`.`price`) AS `max`, MIN(`book_order`.`price`) AS `min` FROM `book` LEFT OUTER JOIN `book_order` ON (`book`.`id` = `book_order`.`book_id`) GROUP BY `book`.`id` ORDER BY NULL'

    return HttpResponse('success')

def index5(request):
    #1.求所有图书的销售总额
    result = BookOrder.objects.aggregate(total=Sum('price'))
    print(result)
    #{'total': 455.0}
    print(connection.queries)
    #'SELECT SUM(`book_order`.`price`) AS `total` FROM `book_order`'


    #求每一本书的销售总额
    books = Book.objects.annotate(total=Sum("bookorder__price"))
    for book in books:
        print("%s/%s"%(book.name,book.total))
    '''
    三国演义/268.0
    水浒传/187.0
    西游记/None
    红楼梦/None
    '''
    print(connection.queries)
    #'sql': 'SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED', 'time': '0.000'}, {'sql': 'SELECT SUM(`book_order`.`price`) AS `total` FROM `book_order`', 'time': '0.016'}, {'sql': 'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, `book`.`publisher_id`, SUM(`book_order`.`price`) AS `total` FROM `book` LEFT OUTER JOIN `book_order` ON (`book`.`id` = `book_order`.`book_id`) GROUP BY `book`.`id` ORDER BY NULL'

    #3、求2020年度每一本图书销售总额
    result = BookOrder.objects.filter(create_time__year=2020).aggregate(total=Sum('price'))
    print(result)
    #{'total': 455.0}
    print(connection.queries)
    #'sql': 'SELECT SUM(`book_order`.`price`) AS `total` FROM `book_order`'
    #'sql': "SELECT SUM(`book_order`.`price`) AS `total` FROM `book_order` WHERE `book_order`.`create_time` BETWEEN '2020-01-01 00:00:00' AND '2020-12-31 23:59:59.999999'"
    #求每一本图书在2020年度销售总额
    books = Book.objects.filter(bookorder__create_time__year=2020).annotate(total=Sum("bookorder__price"))
    for book in books:
        print('%s/%s' % (book.name, book.total))
    '''
    三国演义/268.0
    水浒传/187.0
    '''
    print(connection.queries)
    #'sql': "SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, `book`.`publisher_id`, SUM(`book_order`.`price`) AS `total` FROM `book` INNER JOIN `book_order` ON (`book`.`id` = `book_order`.`book_id`) WHERE `book_order`.`create_time` BETWEEN '2020-01-01 00:00:00' AND '2020-12-31 23:59:59.999999' GROUP BY `book`.`id` ORDER BY NULL"
    return HttpResponse('index5')

def index6(request):
    #给每一本图书的售价增加10元
    Book.objects.update(price=F('price')+10)
    print(connection.queries[-1])

    authors = Author.objects.filter(name=F('email'))
    for author in authors:
        print('%s/%s'%(author.name,author.email))
    #wce@qq.com/wce@qq.com
    print(connection.queries[-1])
    #{'sql': 'SELECT `author`.`id`, `author`.`name`, `author`.`age`, `author`.`email` FROM `author` WHERE `author`.`name` = `author`.`email`', 'time': '0.016'}
    return HttpResponse('index6')

def index7(request):
    #1.获取价格大于100并且评分大于4.85的书籍
    books = Book.objects.filter(price__gte=100,rating__gte= 4.85)
    for book in books:
        print("%s/%s/%s"%(book.name,book.price,book.rating))
    '''
    西游记/125.0/4.85
    红楼梦/129.0/4.9
    '''

    #2.获取价格大于100并且评分大于4.85的书籍
    books1 = Book.objects.filter(Q(price__gte=100)&Q(rating__gte=4.85))
    for book in books1:
        print("%s/%s/%s" % (book.name, book.price, book.rating))
    '''
    西游记/125.0/4.85
    红楼梦/129.0/4.9
    '''
    #3.获取价格低于100元或者评分低于4分的图书
    books2 = Book.objects.filter(Q(price__lt=127)|Q(rating__lt=4.85))
    for book in books2:
        print("%s/%s/%s" % (book.name, book.price, book.rating))
    '''
    三国演义/128.0/4.8
    水浒传/127.0/4.83
    西游记/125.0/4.85
    '''
    print('+'*50)
    #4.价格大于100，并且图书名字中不包含'记'字的图书
    books = Book.objects.filter(Q(price__gte=100)&~Q(name__icontains='传'))
    for book in books:
        print("%s/%s/%s" % (book.name, book.price, book.rating))
    #水浒传/127.0/4.83  如果~ 这是 非
    '''
    三国演义/128.0/4.8
    西游记/125.0/4.85
    红楼梦/129.0/4.9
    '''
    return HttpResponse('index7')