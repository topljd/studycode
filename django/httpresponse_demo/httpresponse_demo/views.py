from django.http import HttpResponse

def index(request):
    # response = HttpResponse()
    # response.content='知了课堂'
    # response = HttpResponse('知了课堂1')
    # response.status_code = 400

    response = HttpResponse('<h1>知了课堂</h1>',content_type='text/plain;charset=utf-8')
    #<h1>知了课堂</h1> 被当做普通的代码处理
    response['PASSWORD']='zhile'

    response.write('知了')
    #<h1>知了课堂</h1>知了
    #用来写入content中
    return response
