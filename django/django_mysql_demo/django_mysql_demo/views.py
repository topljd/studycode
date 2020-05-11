from django.shortcuts import render
from django.db import connection

def index(request):
    #连接游标
    cursor = connection.cursor()
    #cursor.execute("insert into book(id , name ,author) values(null,'三国演义','罗贯中')")
    cursor.execute('select * from book')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return render(request,'index.html')