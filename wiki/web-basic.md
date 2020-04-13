

1주차 세미나 숙제
======
#####  배운 내용을 정리

웹기초
------
##### 웹 : World Wide Web : 인터넷(네트워크)에 연결된 사용자들이 문자, 영상, 음성 등이 혼합된 멀티미디어를 공유할 수 있는 공간 
##### 웹페이지 : 우리가 보는 한 면의 화면 
##### 웹사이트 : 웹페이지들이 연결되어 만들어진 하나의 완전체. 웹페이지가 말그대로 책의 한 페이지라면, 웹사이트는 제본된 책(?) / 수많은 웹 페이지들이 Hyperlink를 통해 서로 연결되어 웹 사이트를 구성한다. 
##### HTML : HyperText Markup Language : 웹 페이지를 만드는 데 가장 기초적이면서 필수적이라고 한다. 
##### 웹 브라우저 : 사용자가 웹 사이트에 접근할 수 있도록 해주는 응용 프로그램 

------
##### 서버(Server): 제공자(Provider) 서비스를 제공하는 컴퓨터, 저장하고 있는 정보(데이터베이스)를 Client에게 제공한다. 
##### 클라이언트(Client): 이런 서비스를 요청하는 요청자 
##### 웹 서비스는 서버와 클라이언트의 요청(Request) - 응답(Response)의 반복을 기능한다! 
##### URI : Uniform Resource Identifier 인터넷에 있는 **자원의 위치** 를 나타내는 주소 (URL은 URI의 일종)<br>
https:// -> **접근 방식**         www.youtube~~~ -> **네트워크 상의 위치** <br>
https와 http의 차이? https는 데이터를 주고 받을때 *보안요소*가 추가된다. (s: secure socket) <br>

##### 웹 서비스 개발: 웹이라느 공간에서 서비스하는 프로그램을 만드는 것
------
##### Front-end : Client 쪽엣 실행되는 사용자 **눈에 보이는** 부분 개발 <br>
##### Back-end : Server 쪽에서 실행되는 **눈에 보이지 않는** 부분 개발 <br>
##### 데이터 베이스 : 백 엔드가 다루는 데이터를 보관하고 검색해 오는 기술 : 데이터는 서로 엮여 있다!
##### 프레임워크 : 웹 프로그래밍에 있어서 뼈대 역할을 해준다.  
##### 프로그래밍 언어는 어떤 프레임워크를 사용하냐에 따라서 달라질 수 있다.
##### 
1. Html : 웹 문서의 본문을 적는 텍스트 포맷
2. Css : Html로 만든 웹 문서의 스타일을 다루는 속성
3. Javascript : 웹 브라우저가 이해하고 실행할 수 있는 프로그래밍 언어

개발 환경 셋팅
--------
##### homebrew : 패키지 관리자, 개발에 필요한 패키지들을 편리하게 설치하고 관리.  
1. brew -v : homebrew의 버전 확인
2. brew list : homebrew가 관리하는 패키지 목록 확인

##### pyenv : python 버전 관리자, 이걸 설치하면 의존성(dependency)도 함께 설치된다. -> 시스템 내에 여러 버전의 파이썬을 설치하고 관리할 수 있게 한다. 따라서 특정 프로젝트는 2.7버전을, 다른 프로젝트는 3.6버전을 사용하는 것이 가능하다.
1. pyenv versions : python 버전 확인 가능
2. pyenv global x.x.x : x.x.x를 기본 버전으로 설정

##### virtualenv : pyenv-virtualenv라는 가상환경 플러그인을 설치함으로써 각각의 프로젝트가 사용하는 패키지들이 충돌하지 않도록 개발 환경을 분리함. —> 결과적으로 특정 프로젝트만을 위한 python 버전과 패키지 버전을 격리된 가상공간에서 사용 가능.
1. brew install pyenv-virtualenv : 가상환경 설치
2. pyenv virtualenv 3.6.8 name : 파이썬 3.6.8을 기반으로하는 name이라는 이름의 가상환경 만들기
3. pyenv versions을 통해 잘 만들어졌는지 확인
4. pyenv activate seminar : Django 가상환경 활성화
5. pyenv deactivate 가상환경 비활성화

##### Django : 장고는 파이썬으로 만들어진 웹 프레임워크다.
1. pip list : 이미 설치되어 있는 Python 패키지 확인
2. pip install django : 장고 설치
3. django-admin startproject testForInstallation : test~라는 이름의 장고 프로젝트 생성
4. python manage.py runserver 개발용 서버 켜줌 -> 닫고 싶으면 컨트롤c 이후 가상환경 비활성화 해주기. 

git
---------

