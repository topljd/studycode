from django.shortcuts import render,redirect,reverse
from django.http import  HttpResponse
# Create your views here.
def index(request):
    username = request.GET.get('username')
    if not username:
        return redirect(reverse('error:403'))
    return HttpResponse('shouye')