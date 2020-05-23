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