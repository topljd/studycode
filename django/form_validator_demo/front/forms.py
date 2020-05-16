from django import forms
from django.core import validators
from .models import User
class BaseForm(forms.Form):
    def get_errors(self):
        errors = self.errors.get_json_data()
        new_errors = {}
        for key, message_dicts in errors.items():
            messages = []
            for message_dict in message_dicts:
                message = message_dict['message']
                messages.append(message)
            new_errors[key] = messages
        return new_errors


# {'telephone': ['请输入正确的手机号码'], 'pwd1': ['Ensure this value has at least 6 characters (it has 2).'], 'pwd2': ['Ensure this value has at least 6 characters (it has 2).']}



class MyForm(BaseForm):#继承了baseform（简化错误的提取)
    # email = forms.CharField(validators=[validators.EmailValidator(message='请输入正确格式邮箱')])
    # {'email': [{'message': '请输入正确格式邮箱', 'code': 'invalid'}]}
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d{9}', message='请输入正确的手机号码')])
    # {'telephone': [{'message': 'Enter a valid value.', 'code': 'invalid'}]}


class RegisterForm(BaseForm):
    username = forms.CharField(max_length=100)
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d{9}', message='请输入正确的手机号码')])
    pwd1 = forms.CharField(max_length=16,min_length=6)
    pwd2 = forms.CharField(max_length=16,min_length=6)

    def clean_telephone(self):  # clean_字段
        telephone = self.cleaned_data.get('telephone')
        exists = User.objects.filter(telephone=telephone).exists()
        if exists:
            raise forms.ValidationError(message='%s 手机号码已经被注册' % telephone)
        # 如果验证没有问题一定要将数据返回回去
        return telephone


    def clean(self):
        #如果来到了clean方法，说明之前每一个字段都验证成功了
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get('pwd1')
        pwd2 = cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError(message='密码输入不一致')
        return cleaned_data
