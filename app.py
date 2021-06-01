from flask import Flask, render_template, request, session, redirect
import bdb #내가 만든 데이터베이스 함수들
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("main.html")

@app.route('/hello')
def hello():
    return render_template("main.html")


@app.route('/login', methods=['GET','POST'])
def login():
        if request.method == 'GET':
             return render_template("login.html")
        else:
        #여기 POST로 들어오는 데이터를 받아보자
            Email = request.form['Email']
            pwd = request.form['pwd']
            print("전달된값:", Email, pwd)
            #만약에 이메일과 패스워드 같다면 
            #if Email =='a@a.com' and pwd =='1234':
            ret = bdb.get_emailpw(Email, pwd)
            #로그인 성공
            if ret != 'None':
                session['email'] = Email
                     return("로그인 성공")
            #아니면 아이디 패스워드 확인
                else:
                 return("아이디, 패스워드 확인")
    
@app.route('/naver')
def naver():
    #로그인 상태값 체크
    if 'email' in session:
        #네이버 검색 페이지 사용
        return render_template("naver.html")
    else:
        #로그인 페이지로 강제 이동
        return redirect('login') 
#로그아웃(session)제거


@app.route('/signin', methods=['GET','POST'])
def signin():
    if request.method == 'GET':
         return render_template("signin.html")
    else:
        #여기 POST로 들어오는 데이터를 받아보자
        Email = request.form['Email']
        pwd = request.form['pwd']
        print("전달된값:", Email, pwd)
        #전달된 값을 그대로 db에 저장
        bdb.insert_data(Email, pwd)
        return '회원가입 데이터(POST)'

if __name__ == '__main__':
    app.run()