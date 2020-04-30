from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Author,BookOrder,Publisher
from django.db.models.manager import Manager
from django.db.models.query import QuerySet
from django.db.models import Q,F,Count,Prefetch
from django.db import connection
# Create your views here.

def index(request):
    books = Book.objects.filter(id__gte=2)
    for book in books:
        print(book.name)
    print(connection.queries[-1])
    #'sql': 'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, `book`.`publisher_id` FROM `book` WHERE `book`.`id` >= 2'
    return HttpResponse('success')

#filter annotate exclude
def index2(request):
    books = Book.objects.filter(id__gte=2).exclude(id=3)
    for book in books:
        print(f'书名为: {book.name},书的id为： {book.id}')
    '''
    书名为: 水浒传,书的id为： 2
    书名为: 红楼梦,书的id为： 4
    '''
    print(connection.queries[-1])#输出列表的最后一个
    #'sql': 'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, `book`.`publisher_id` FROM `book` WHERE (`book`.`id` >= 2 AND NOT (`book`.`id` = 3))'

    books = Book.objects.annotate(author_name = F('author__name'))
    #获取到作者里面的名字,author表下面的名字传给book表作为字段
    for book in books:
        print('%s/%s' % (book.name,book.author_name))
    '''
    三国演义/罗贯中
    水浒传/施耐庵
    西游记/吴承恩
    红楼梦/曹雪芹
    '''
    #'sql': 'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, `book`.`publisher_id`, `author`.`name` AS `author_name` FROM `book` INNER JOIN `author` ON (`book`.`author_id` = `author`.`id`)'
    print(connection.queries[-1])
    return  HttpResponse('index2')

def index3(request):
    #根据create_time从小到大进行排序
    orders = BookOrder.objects.order_by('price')
    for order in orders:
        print('%s/%s'% (order.id,order.price))
    '''
    2/85.0
    3/88.0
    5/93.0
    4/94.0
    1/95.0
    '''
    print(connection.queries[-1])
#'SELECT `book_order`.`id`, `book_order`.`price`, `book_order`.`book_id` FROM `book_order` ORDER BY `book_order`.`price` ASC'

    orders = BookOrder.objects.order_by('-price')#从大到小排序
    for order in orders:
        print(order.price)
    '''
    95.0
    94.0
    93.0
    88.0
    85.0
    '''
    print(connection.queries[-1])
    #'SELECT `book_order`.`id`, `book_order`.`price`, `book_order`.`book_id` FROM `book_order` ORDER BY `book_order`.`price` DESC'

    #首先根据book_id从大到小排序，如果一样那么根据price从大到小进行排序
    orders = BookOrder.objects.order_by('-book_id','-price')
    for order in orders:
        print(order.book_id,',',order.price)
    '''
    2 , 94.0
    2 , 93.0
    1 , 95.0
    1 , 88.0
    1 , 85.0
    '''

    #如果有两个order_by将会显示根据后边的一个order_by排序
    orders = BookOrder.objects.order_by('-book_id').order_by( '-price')
    for order in orders:
        print(order.book_id, ',', order.price)
    '''
    1 , 95.0
    2 , 94.0
    2 , 93.0
    1 , 88.0
    1 , 85.0
    '''

    #提取图书数据，根据图书的销量进行排序（从大到小进行排序）
    books = Book.objects.annotate(order_nums=Count('bookorder__id')).order_by('-order_nums')
    for book in books:
        print(book.name,book.order_nums)
    '''
    三国演义 3
    水浒传 2
    西游记 0
    红楼梦 0
    '''
    print(connection.queries[-1])
    #'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, `book`.`publisher_id`, COUNT(`book_order`.`id`) AS `order_nums` FROM `book` LEFT OUTER JOIN `book_order` ON (`book`.`id` = `book_order`.`book_id`) GROUP BY `book`.`id` ORDER BY `order_nums` DESC'
    return HttpResponse('index3')


def index4(request):
    books = Book.objects.values('id','name').all()
    #queryset里面存储的是 字典
    for book in books:
        print(book['id'],book['name'])
    '''
    1 三国演义
    2 水浒传
    3 西游记
    4 红楼梦
    '''
    books = Book.objects.values('id', 'name',author_name = F('author__name')).all()
    # queryset里面存储的是 字典
    #  F表达式经常用于动态的查找
    for book in books:
        print(book)
    '''
    {'id': 1, 'name': '三国演义', 'author__name': '罗贯中'}
    {'id': 2, 'name': '水浒传', 'author__name': '施耐庵'}
    {'id': 3, 'name': '西游记', 'author__name': '吴承恩'}
    {'id': 4, 'name': '红楼梦', 'author__name': '曹雪芹'}
    
    利用F表达式后：
    {'id': 1, 'name': '三国演义', 'author_name': '罗贯中'}
    {'id': 2, 'name': '水浒传', 'author_name': '施耐庵'}
    {'id': 3, 'name': '西游记', 'author_name': '吴承恩'}
    {'id': 4, 'name': '红楼梦', 'author_name': '曹雪芹'}
    '''
    #使用count聚合函数
    books = Book.objects.values('id','name',order_nums=Count('bookorder__id'))
    for book in books:
        print(book)
    '''
    {'id': 1, 'name': '三国演义', 'order_nums': 3}
    {'id': 2, 'name': '水浒传', 'order_nums': 2}
    {'id': 3, 'name': '西游记', 'order_nums': 0}
    {'id': 4, 'name': '红楼梦', 'order_nums': 0}
    '''
    print(connection.queries[-1])
#'SELECT `book`.`id`, `book`.`name`, COUNT(`book_order`.`id`) AS `order_nums` FROM `book` LEFT OUTER JOIN `book_order` ON (`book`.`id` = `book_order`.`book_id`) GROUP BY `book`.`id` ORDER BY NULL'
    print('+'*50)
    books = Book.objects.values_list()
    print(type(books))
    #<class 'django.db.models.query.QuerySet'>
    for book in books:
        print(book)
    '''返回的是元组数据
    (1, '三国演义', 987, 98.0, 4.8, 3, 1)
    (2, '水浒传', 967, 97.0, 4.83, 4, 1)
    (3, '西游记', 1004, 95.0, 4.85, 2, 2)
    (4, '红楼梦', 1007, 99.0, 4.9, 1, 2)
    '''
    print('=' * 50)
    books = Book.objects.values_list('name',flat=True)
    #只获取到name这个字段
    print(type(books))
    # <class 'django.db.models.query.QuerySet'>
    for book in books:
        print(book)
    '''返回的是元组数据,如果元组只有一个元素，那么后边就会有一个逗号
   ('三国演义',)
    ('水浒传',)
    ('西游记',)
    ('红楼梦',)
    使用flat=True后的数据，如果有两个字段就会出现错误
    三国演义
    水浒传
    西游记
    红楼梦
    '''
    return HttpResponse('index4')

def index5(request):
    books = Book.objects.all()
    for book in books:
        print(book)#Book object (1)输出的是一个对象
        print(book.id,book.name)#这里可以输出数据 4 红楼梦等
    return HttpResponse("index5")

#select_related 只会产生一查询，但是能实现多对多
def index6(requeset):
    #books = Book.objects.all()#应该是book关联的author字段中的名字，此时每次都需要查询语句有点浪费资源
    books = Book.objects.select_related("author","publisher")#在一次查询中讲author查询出来了,这个地方只能使用外键的字段
    for book in books:
        #print(book.name)
        print(book.author.name)
        print(book.publisher.name)
    '''
    罗贯中
    中国邮电出版社
    施耐庵
    中国邮电出版社
    吴承恩
    清华大学出版社
    曹雪芹
    清华大学出版社
    '''
    print(connection.queries[-1])
    #'SELECT `author`.`id`, `author`.`name`, `author`.`age`, `author`.`email` FROM `author` WHERE `author`.`id` = 1 LIMIT 21'
    return HttpResponse('index6')

# prefetch_related的用法 需要查询两次，只会产生两次查询
def index7(request):
    # books = Book.objects.all()
    # for book in books:
    #     print('='*30)
    #     print(book.name)
    #     orders = book.bookorder_set.all()#sql语句查询的次数多了
    #     #对象.模型类小写_set.all 访问1对多模型
    #     for order in orders:
    #         print(order.id)
    #     '''
    #     三国演义
    #     1
    #     2
    #     3
    #     ==============================
    #     水浒传
    #     4
    #     5
    #     ==============================
    #     西游记
    #     ==============================
    #     红楼梦
    #     '''
    # print('*'*80)
    # books = Book.objects.prefetch_related("bookorder_set")
    # #将所有的book查询出来，更具book ID将订单查询出来！做了两次查询
    # for book in books:
    #     print('='*30)
    #     print(book.name)
    #     orders = book.bookorder_set.all()#sql语句查询的次数多了
    #     #对象.模型类小写_set.all 访问1对多模型
    #     for order in orders:
    #         print(order.id)
    # #print(connection.queries)
    # #{'sql': 'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, `book`.`publisher_id` FROM `book`', 'time': '0.000'}, {'sql': 'SELECT `book_order`.`id`, `book_order`.`price`, `book_order`.`book_id` FROM `book_order` WHERE `book_order`.`book_id` IN (1, 2, 3, 4)', 'time': '0.000'}
    #
    # books = Book.objects.prefetch_related('author')
    # for book in books:
    #     print(book.author.name)
    #     '''
    #     罗贯中
    #     施耐庵
    #     吴承恩
    #     曹雪芹
    #     '''
    # print(connection.queries)
    #'SELECT `author`.`id`, `author`.`name`, `author`.`age`, `author`.`email` FROM `author` WHERE `author`.`id` IN (1, 2, 3, 4)'

    #过滤价格大于90元的
    #传统做法
    # books =Book.objects.prefetch_related('bookorder_set')
    # #如果使用prefetch_related的时候，就不能使用类似filter产生新sql语句的方法
    # for book in books:
    #   print('='*50)
    #   print(book.name)
    #   orders = book.bookorder_set.filter(price__gte=90)#因使用filter，所以prefetch_related失效
    #   for order in orders:
    #     print(order.id)
    # print(connection.queries)
    '''
    三国演义
    1
    ==================================================
    水浒传
    4
    5
    ==================================================
    西游记
    ==================================================
    红楼梦
    [{'sql': 'SELECT @@SQL_AUTO_IS_NULL', 'time': '0.000'}, {'sql': 'SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED', 'time': '0.000'}, {'sql': 'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, `book`.`publisher_id` FROM `book`', 'time': '0.000'}, {'sql': 'SELECT `book_order`.`id`, `book_order`.`price`, `book_order`.`book_id` FROM `book_order` WHERE `book_order`.`book_id` IN (1, 2, 3, 4)', 'time': '0.000'}, {'sql': 'SELECT `book_order`.`id`, `book_order`.`price`, `book_order`.`book_id` FROM `book_order` WHERE (`book_order`.`book_id` = 1 AND `book_order`.`price` >= 90.0e0)', 'time': '0.000'}, {'sql': 'SELECT `book_order`.`id`, `book_order`.`price`, `book_order`.`book_id` FROM `book_order` WHERE (`book_order`.`book_id` = 2 AND `book_order`.`price` >= 90.0e0)', 'time': '0.000'}, {'sql': 'SELECT `book_order`.`id`, `book_order`.`price`, `book_order`.`book_id` FROM `book_order` WHERE (`book_order`.`book_id` = 3 AND `book_order`.`price` >= 90.0e0)', 'time': '0.000'}, {'sql': 'SELECT `book_order`.`id`, `book_order`.`price`, `book_order`.`book_id` FROM `book_order` WHERE (`book_order`.`book_id` = 4 AND `book_order`.`price` >= 90.0e0)', 'time': '0.000'}]
        '''
    #解决办法，使用Prefetch类
    prefetch = Prefetch('bookorder_set',queryset=BookOrder.objects.filter(price__gte=90))
    books = Book.objects.prefetch_related(prefetch)
    for book in books:
      print('='*50)
      print(book.name)
      orders = book.bookorder_set.all()
      for order in orders:
        print(order.id)
    print(connection.queries)
    #{'sql': 'SELECT `book`.`id`, `book`.`name`, `book`.`pages`, `book`.`price`, `book`.`rating`, `book`.`author_id`, `book`.`publisher_id` FROM `book`', 'time': '0.000'}, {'sql': 'SELECT `book_order`.`id`, `book_order`.`price`, `book_order`.`book_id` FROM `book_order` WHERE (`book_order`.`price` >= 90.0e0 AND `book_order`.`book_id` IN (1, 2, 3, 4))', 'time': '0.000'}

    return HttpResponse('index7')