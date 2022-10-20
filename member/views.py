import logging

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import Member


def home(request):
	user_id = request.session.get('user')

	if user_id:
		member = Member.objects.get(pk=user_id)
		return HttpResponse(member.username)
	return HttpResponse('Home')

def login(request):
	if request.method == 'GET':
		return render(request, 'login.html')
	elif request.method == 'POST':
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)

	res_data = {}
	if not (username and password):
		res_data['error'] = '모든 값을 입력하세요!'
	else:
		member = Member.objects.get(username = username)
		if check_password(password, member.password):
			logging.info(f"session: {request.session.get('user')}")
			request.session['user'] = member.id
			return redirect('/')
		else:
			res_data['error'] = '비밀번호가 다릅니다!'
	return render(request, 'login.html', res_data)

def logout(request):
	if request.session.get('user'):
		del(request.session['user'])
	return redirect('/')

def register(request):
	if request.method == 'GET':
		return render(request, 'register.html')
	elif request.method == 'POST':
		username = request.POST.get('username', None)
		email = request.POST.get('email', None)
		password = request.POST.get('password', None)
		re_password = request.POST.get('re_password', None)

	res_data = {}
	if not (username and email and password and re_password):
		res_data['error'] = '모든 값을 입력하세요'
	elif password != re_password:
		res_data['error'] = '비밀번호가 다릅니다'

	if password != re_password:
		res_data['error'] = '비밀번호가 다릅니다.'
	else:
		member = Member(
					username=username,
					password=make_password(password),
					email=email,
				)
		member.save()		

	return render(request, 'register.html', res_data)


	