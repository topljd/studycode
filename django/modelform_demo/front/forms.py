from django import forms
from .models import Book
class AddBookForm(forms.ModelForm):
    def clean_page(self):
        page =self.cleaned_data.get('page')
        if page > 100:
            raise forms.ValidationError('页码不能大于100')
        return page
    class Meta:
        model = Book
        #fields = '__all__'   这个表示的是全部字段
        fields = ['title','page','price']#这个和上面必须要有一个
        #排除法
        #exclude = ['price']
        error_messages = {
            'page':{'required':'请输入page参数',
                    'invalid':'请s输入一个可用额参数'
                    },
        'title':{
            'required':'请输入title参数',
            'max_length':'title不能超过100个字符'
        },
            'price':{
                'max_value':'图书价格不能超过1000元'
            }
        }
