from django.db import models

# Create your models here.
class FrontUser (models.Model):
    username = models.CharField(max_length=100)

    def __str__(self):
        return "<FrontUser:(id:%s,username:%s)"%(self.id,self.username)
class UserExtension(models.Model):
    school = models.CharField(max_length=100)

    #OneToOneField 就相当于外键的作用
    user = models.OneToOneField("FrontUser",on_delete=models.CASCADE,related_name='extension')
    #因为定义了onetoone索引用户只能是一个

    def __str__(self):
        return "<UserExtension:(id:%s,school:%s,user_id:%s)>"%(self.id,self.school,self.user_id)
