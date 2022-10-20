from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Member(models.Model):
    username    = models.CharField(max_length=128, verbose_name='id')
    email       = models.EmailField(max_length=128, verbose_name='email')
    password    = models.CharField(max_length=128, verbose_name='password')
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name='가입날짜')
    updated_at  = models.DateTimeField(auto_now=True, verbose_name='마지막수정일')
    color = models.CharField(max_length=128, verbose_name='color')

    def __str__(self):
        return self.username

    class Meta:
        db_table            = 'members'