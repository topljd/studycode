from .models import User

#上下文处理器
#需要在settings中进行添加配置
def front_user(request):
    user_id = request.session.get('user_id')
    context ={

    }
    if user_id:
        try:
            user =User.objects.get(pk=user_id)
            context['front_user'] = user
        except:
            pass
    return context
