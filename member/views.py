import random

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import Member, LoginForm, RegisterForm


def home(request):
	color = ['#C70039', '#3498DB']
	user_id = request.session.get('user')
	if user_id:
		content = {}
		member = Member.objects.get(pk=user_id)
		if member.color == "" or member.color is None:
			member.color = color[random.randint(0,1)]
			member.save()
		content['member'] = member
		content['visit_count'] = member.visit_count
		content['color'] = member.color
		return render(request, 'success.html', content)
	return HttpResponse('Home Without Login')


def login(request):
	if request.method=='POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			request.session['user'] = form.user_id
			try:
				member = Member.objects.get(username=form.user_id)
			except Member.DoesNotExist:
				member = None
			if member:
				member.visit_count += 1
				member.save()
			return redirect('/')
	else:
		form = LoginForm()
	return render(request, 'login.html', {'form': form})


def logout(request):
	if request.session.get('user'):
		del(request.session['user'])
	return redirect('/')

def register(request):
	res_data = {}
	if request.method == 'GET':
		return render(request, 'register.html')
	elif request.method == 'POST':
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)
		re_password = request.POST.get('re-password', None)
	
	if username == '' or password == '' or re_password == '':
		res_data['error'] = '모두 입력해주세요'
		render(request, 'register.html', res_data)
	elif password != re_password:
		res_data['error'] = '비밀번호가 다릅니다'
		render(request, 'register.html', res_data)
	elif username:
		if Member.objects.filter(pk=username).exists():
			res_data['error'] = '사용 중인 아이디입니다'
			render(request, 'register.html', res_data)
		else:
			member = Member(
							username=username,
							password=make_password(password),
						)
			member.save()		
			res_data['success'] = '회원가입에 성공했습니다 member/login으로 가서 로그인해주세요'
	return render(request, 'register.html', res_data)


	