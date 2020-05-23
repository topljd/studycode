from django.shortcuts import render
from django.views.generic import View
from django.http import  HttpResponse
from .models import Article
from .forms import ArticleForm
# Create your views here.
class IndexView(View):
    def get(self,request):
        return render(request,'index.html')

    # def post(self,request):
    #     myfile = request.FILES.get('myfile')
    #     # 【报错】'NoneType' object has no attribute'strftime'
    #     # 【原因】没有使用命令python manage.py makemigrations 和命令python manage.py migrate重新生成数据库表
    #
    #     with open('somefile2.txt','wb')as fp:
    #         for content in myfile.chunks():
    #             fp.write(content)
    #             print(content)
    #     return HttpResponse('上传成功')

    # def index(request):
    #     if request.method == 'GET':
    #         return render(request,'index.html')
    #     else:
    #         title = request.POST.get('title')
    #         content = request.POST.get('content')
    #         thumbnail = re

    # def post(self,request):
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     file = request.FILES.get('myfile')
    #     Article.objects.create(title=title,content=content,thumnail=file)
    #     return HttpResponse('success')

    def post(self,request):
        #用来验证表中的文件模型
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('sucess')
        else:
            print(form.errors.get_json_data())
            return HttpResponse('fail')

