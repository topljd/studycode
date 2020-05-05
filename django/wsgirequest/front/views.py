from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.core.handlers.wsgi import WSGIRequest

def index(request):
    print(type(request))
    #<class 'django.core.handlers.wsgi.WSGIRequest'>
    print(request.path)
    #访问首页 /


    print(request.get_host())
    #127.0.0.1:8000
    print(request.is_secure())
    print(request.is_ajax())
    #False

    return HttpResponse('index')
def login(request):
    print(request.path)
    #访问http://127.0.0.1:8000/login/   返回：/login/
    print(request.get_full_path())
    #访问http://127.0.0.1:8000/login/?username=topljd
    #返回 /login/?username=topljd
    #返回整个URL地址
    print(request.get_raw_uri())
    #http://127.0.0.1:8000/login/?username=topljd

    print(request.method)#GET

    print(request.GET['username'])
    #访问http://127.0.0.1:8000/login/?username=topljd
    #topljd

    for key,values in request.META.items():
        print(key,',',values)
    r'''
    ALLUSERSPROFILE , C:\ProgramData
    APPDATA , C:\Users\Administrator\AppData\Roaming
    COMMONPROGRAMFILES , C:\Program Files\Common Files
    COMMONPROGRAMFILES(X86) , C:\Program Files (x86)\Common Files
    COMMONPROGRAMW6432 , C:\Program Files\Common Files
    COMPUTERNAME , DESKTOP-O619S1I
    COMSPEC , C:\Windows\system32\cmd.exe
    DJANGO_SETTINGS_MODULE , wsgirequest.settings
    DRIVERDATA , C:\Windows\System32\Drivers\DriverData
    FPS_BROWSER_APP_PROFILE_STRING , Internet Explorer
    FPS_BROWSER_USER_PROFILE_STRING , Default
    HOMEDRIVE , C:
    HOMEPATH , \Users\Administrator
    IDEA_INITIAL_DIRECTORY , d:\Program Files\JetBrains\PyCharm 2020.1\bin
    LOCALAPPDATA , C:\Users\Administrator\AppData\Local
    LOGONSERVER , \\DESKTOP-O619S1I
    NUMBER_OF_PROCESSORS , 4
    ONEDRIVE , C:\Users\Administrator\OneDrive
    OS , Windows_NT
    PATH , G:\ENV\django_env\Scripts;D:\Program Files\Python38\Scripts\;D:\Program Files\Python38\;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\OpenSSH\;d:\Program Files\Git\cmd;D:\Program Files\nodejs\;C:\Users\Administrator\AppData\Local\Microsoft\WindowsApps;C:\Users\Administrator\AppData\Roaming\npm
    PATHEXT , .COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW
    PROCESSOR_ARCHITECTURE , AMD64
    PROCESSOR_IDENTIFIER , Intel64 Family 6 Model 42 Stepping 7, GenuineIntel
    PROCESSOR_LEVEL , 6
    PROCESSOR_REVISION , 2a07
    PROGRAMDATA , C:\ProgramData
    PROGRAMFILES , C:\Program Files
    PROGRAMFILES(X86) , C:\Program Files (x86)
    PROGRAMW6432 , C:\Program Files
    PROMPT , (django_env) $P$G
    PSMODULEPATH , C:\Program Files\WindowsPowerShell\Modules;C:\Windows\system32\WindowsPowerShell\v1.0\Modules
    PUBLIC , C:\Users\Public
    PYCHARM_DISPLAY_PORT , 63342
    PYCHARM_HOSTED , 1
    PYTHONIOENCODING , UTF-8
    PYTHONPATH , G:\django\wsgirequest;D:\Program Files\JetBrains\PyCharm 2020.1\plugins\python\helpers\pycharm_matplotlib_backend;D:\Program Files\JetBrains\PyCharm 2020.1\plugins\python\helpers\pycharm_display
    PYTHONUNBUFFERED , 1
    SESSIONNAME , Console
    SYSTEMDRIVE , C:
    SYSTEMROOT , C:\Windows
    TEMP , C:\Users\ADMINI~1\AppData\Local\Temp
    TMP , C:\Users\ADMINI~1\AppData\Local\Temp
    USERDOMAIN , DESKTOP-O619S1I
    USERDOMAIN_ROAMINGPROFILE , DESKTOP-O619S1I
    USERNAME , Administrator
    USERPROFILE , C:\Users\Administrator
    VIRTUAL_ENV , G:\ENV\django_env
    WINDIR , C:\Windows
    WORKON_HOME , G:\ENV
    _OLD_VIRTUAL_PATH , D:\Program Files\Python38\Scripts\;D:\Program Files\Python38\;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\OpenSSH\;d:\Program Files\Git\cmd;D:\Program Files\nodejs\;C:\Users\Administrator\AppData\Local\Microsoft\WindowsApps;C:\Users\Administrator\AppData\Roaming\npm
    _OLD_VIRTUAL_PROMPT , $P$G
    RUN_MAIN , true
    SERVER_NAME , activate.navicat.com
    GATEWAY_INTERFACE , CGI/1.1
    SERVER_PORT , 8000
    REMOTE_HOST , 
    CONTENT_LENGTH , 
    SCRIPT_NAME , 
    SERVER_PROTOCOL , HTTP/1.1
    SERVER_SOFTWARE , WSGIServer/0.2
    REQUEST_METHOD , GET
    PATH_INFO , /login/
    QUERY_STRING , username=topljd
    REMOTE_ADDR , 127.0.0.1
    CONTENT_TYPE , text/plain
    HTTP_HOST , 127.0.0.1:8000
    HTTP_CONNECTION , keep-alive
    HTTP_CACHE_CONTROL , max-age=0
    HTTP_UPGRADE_INSECURE_REQUESTS , 1
    HTTP_USER_AGENT , Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36
    HTTP_ACCEPT , text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
    HTTP_SEC_FETCH_SITE , none
    HTTP_SEC_FETCH_MODE , navigate
    HTTP_SEC_FETCH_USER , ?1
    HTTP_SEC_FETCH_DEST , document
    HTTP_ACCEPT_ENCODING , gzip, deflate, br
    HTTP_ACCEPT_LANGUAGE , zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7
    wsgi.input , <django.core.handlers.wsgi.LimitedStream object at 0x000002F0C1BAC9A0>
    wsgi.errors , <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>
    wsgi.version , (1, 0)
    wsgi.run_once , False
    wsgi.url_scheme , http
    wsgi.multithread , True
    wsgi.multiprocess , False
    wsgi.file_wrapper , <class 'wsgiref.util.FileWrapper'>
    '''

    return HttpResponse('login')
