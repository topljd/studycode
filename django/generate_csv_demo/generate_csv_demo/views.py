from django.http import HttpResponse,StreamingHttpResponse
#内置的csv模块
import csv

def index(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']="attachment;filename=abc.csv"
    #指定为附件，并且下载名为abc.csv
    '''
    #with open('xxx.csv') as fp:
        #csv.write(fp)
    '''
    write = csv.writer(response)#write 句柄或者对象
    write.writerow(['username','age'])
    write.writerow(['zhiliao','18'])

    return response

from django.template import loader,Context
def template_views_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment;filename=123.csv"
    context = {
        'rows':[
            ['username','age'],
            ['zhiliao',18],
        ]
    }
    template = loader.get_template('abc.txt')
    csv_template = template.render(context)
    response.content = csv_template
    return response

def laege_csv_view(request):
    #response = StreamingHttpResponse(content_type = 'text/csv')
    #response['Content-Disposition'] = "attachment;filename=large.csv"
    #rows = ('Row {},{}\n'.format(row,row) for row in range(0,10000))
    #print(type(rows))
    #<class 'generator'>
    #response.streaming_content=("username,age\n","zhiliao,18\n","zhiliao1,18\n")
    #response = HttpResponse('sucess')

    #response.streaming_content = rows
    #return response

    response =HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename = "large.csv"'
    write = csv.writer(response)
    for row in range(0,10000):
        write.writerow(['Row{}'.format(row),'{}'.format(row)])
    return response

