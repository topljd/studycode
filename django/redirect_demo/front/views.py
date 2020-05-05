from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
# Create your views here.
def index(request):
    #如果没有登录，那么就重定向到注册页面
    #如果在URL中传递了username参数，那么久认为是登录了，否则就没有
    #/?username=xxx
    #request.GET 获取的是一个字典，get是方法
    username = request.GET.get("username")
    if username:
        return HttpResponse(f'您的用户名为：{username}')
    else:
        return redirect(reverse('signup'))
    #reverse('signup') 翻转到signup名字的url地址

def signup(request):
    return HttpResponse('注册页')