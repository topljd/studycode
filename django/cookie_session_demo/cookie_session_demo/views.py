from django.http import HttpResponse
from datetime import datetime
from django.utils.timezone import make_aware
def index(request):
    response = HttpResponse('index')
    expires = datetime(year=2020,month=5,day=23,hour=18,minute=55,second=0)
    #response.set_cookie('username','zhiliao',max_age=180)
    expires = make_aware(expires)
    response.set_cookie('user_id','abc',expires=expires,path='/cms/')
    return response

def delete_cookie(request):
    response = HttpResponse('delete')
    response.delete_cookie('user_id')
    return response


def my_list(request):
    cookies = request.COOKIES  #获取cookies
    username = cookies.get('user_id')#当指定路径path时，就只有定义的路径才可以访问cookies
    return HttpResponse(username)
def cms_view(request):
    cookies = request.COOKIES
    user_id = cookies.get('user_id')
    return  HttpResponse(user_id)

def session_view(request):
    #request.session['username']='zhiliao'
    '''
    session_key:xu1sqci41tu9o8ti7euoek9mo88oborw
    session_data:MmVjMTQxMWZhZTliMGFhNzhiZDBmOTI0ZWFjMjFkOWZkZjJkOTA2Zjp7InVzZXJuYW1lIjoiemhpbGlhbyJ9
    expire_date:06:45:47.800084
    '''

    username = request.session.get('username')
    #此时可以访问到 zhiliao

    #从`session`中删除一个值
    #username = request.session.pop('username')
    #request.session['username']='zhiliao'
    #request.session['userid']=10

    #调用clear方法
    #request.session.clear()#可以清楚掉session，表里面的数据还是有的

    #request.session.flush()#执行这样的语句，就会数据表里的数据将会消失
    print(username)

    #request.session.set_expiry(0)#将会马上过期
    #request.session.set_expiry(None)#默认的过期日期，两周后

    #request.session.set_expiry(-1)

    request.session.clear_expired()
    #删除掉过期的session

    return HttpResponse('session view')