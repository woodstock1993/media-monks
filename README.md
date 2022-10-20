<div align="center"><img src="https://user-images.githubusercontent.com/67543838/197018360-0fdfa483-7bbc-42de-a7b5-316ca85b5f71.png"></div>

# 목차
- [media_monks 기업과제](#media_monks_기업과제)
- [구현 요구사항](#구현-요구사항)
- [구현](#구현)

# media_monks_기업과제

## 구현 요구사항
- [x] 유저가 홈페이지 방문 시 빨간공 또는 파란공을 1/2 확률로 보여주기
  - 로그인 기능 구현

- [x] 유저가 재방문 시 몇번 째 방문인지 페이지에 표시해주기
  - 로그인 기능 구현 시 세션 및 쿠키 적용
- [x] 유저가 재방문 시 처음봤던 공 색을 유지해서 보여주기
  - 로그아웃 기능 구현

- [x] cookie를 통해 방문한 횟수 체크하기


### 기술 스택
<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=HTML5&logoColor=white"/> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=JavaScript&logoColor=white"/> <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/Django-092E20?style=flat-square&logo=Django&logoColor=white"/> <img src="https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=SQLite&logoColor=white"/> 



### 개발 기간
- 2022.10.20 - 2022.10.21

### API 주소
- member/register : 회원가입
- member/login : 로그인
- member/logout : 로그아웃

### Step to run
```
$ python -m venv venv
$ source venv/bin/activate (Mac)일 경우
$ ./venv/Scripts/activate (Window)일 경우
$ python install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

### How to Test
```
$ /member/register url 가서 회원가입
$ /member/login url 가서 로그인
$ /member/logout url 가서 로그아웃
$ /member/login url 가서 다시 로그인
```
