from django.db import models
from django import forms
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
    # 입력받을 값 두개
    username = forms.CharField(error_messages={
        'required':'아이디를 입력하세요!'
    },max_length=100, label="사용자이름")
    password = forms.CharField(error_messages={
        'required':'비밀번호를 입력하세요!'
    },widget=forms.PasswordInput, max_length=100, label="비밀번호")

    # 처음 값이 들어왔다 는 검증 진행    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            member = Member.objects.get(username=username)

            if not check_password(password, member.password):
                self.add_error('password', '비밀번호가 다릅니다!')
            else:
                self.user_id = member.username


class RegisterForm(forms.Form):
    username = forms.CharField(error_messages={
        'required':'아이디를 입력하세요!'
    },max_length=100, label="사용자이름")
    password = forms.CharField(error_messages={
        'required':'비밀번호를 입력하세요!'
    },widget=forms.PasswordInput, max_length=100, label="비밀번호")


class Member(models.Model):
    username    = models.CharField(max_length=128, verbose_name='id', primary_key=True)
    password    = models.CharField(max_length=128, verbose_name='password', null=False)
    created_at  = models.DateTimeField(auto_now_add=True, verbose_name='가입날짜')
    updated_at  = models.DateTimeField(auto_now=True, verbose_name='마지막수정일')
    visit_count = models.IntegerField(verbose_name='방문 횟수', default=0)
    color = models.CharField(max_length=128, verbose_name='color', null=True, default='')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'members'