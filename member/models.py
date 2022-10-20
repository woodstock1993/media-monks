from django.db import models
from django.core.validators import EmailValidator

# Create your models here.
class Member(models.Model):
    username    = models.CharField(max_length=128, verbose_name='id', primary_key=True)
    email       = models.EmailField(max_length=128, validator=EmailValidator, verbose_name='email', unique=True)
    password    = models.CharField(max_length=128, verbose_name='password')
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name='가입날짜', null=True)
    updated_at  = models.DateTimeField(auto_now=True, verbose_name='마지막수정일', null=True)
    visit_count = models.IntegerField(verbose_name='방문 횟수', default=1)
    color = models.CharField(max_length=128, verbose_name='color', null=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'members'