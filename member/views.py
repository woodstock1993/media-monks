from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import Member

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
					password=password,
					email=email,
				)
		member.save()		

	return render(request, 'register.html', res_data)


	