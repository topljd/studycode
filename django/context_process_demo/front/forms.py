#验证提交的数据是否正确

from django import forms
from .models import User
class SignupForm(forms.ModelForm):
    #这里面还需要补表单中的字段验证
    password_repeat = forms.CharField(max_length=16,min_length=6)

    #重写clean方法
    def clean(self):
        #清洗数据
        cleaned_data =super(SignupForm, self).clean()
        password = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')
        if password != password_repeat:
            raise forms.ValidationError(message='两次密码输入不一致')
        return cleaned_data


    class Meta:
        model = User

        #验证所有的字段
        fields = '__all__'

#验证登录的表单
class SigninForm(forms.ModelForm):
    class Meta:
        model =User

        #输入验证的字段
        fields =['username','password']

