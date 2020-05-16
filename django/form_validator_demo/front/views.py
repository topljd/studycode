from django.shortcuts import render
from django.views.generic import View
from .forms import MyForm,RegisterForm
from django.http import HttpResponse
from .models import User
# Create your views here.
class IndexView(View):
    def get(self,request):
        return render(request,'index.html')

    def post(self,request):
        form = MyForm(request.POST)
        if form.is_valid():
            return HttpResponse('success')
        else:
            print(form.errors.get_json_data())
            return HttpResponse('error')
class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            telephone = form.cleaned_data.get('telephone')
            User.objects.create(username=username,telephone=telephone)
            return HttpResponse('注册成功')
        else:
            print(form.get_errors())
            return HttpResponse('注册失败')