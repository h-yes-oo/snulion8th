프리세미나 1주차(2020_04_11) Review
===

웹이란?
---
World Wide Web.

수많은 웹 페이지들이 Hyperlink를 통해 연결되어 웹사이트를 이룬다.

* HTML이란

Hyper Text Markup Language로 웹 페이지를 만드는 데 가장 기초적이면서 필수적인 프로그래밍 언어를 뜻한다.


* 웹 브라우저란

사용자가 웹 사이트에 접근할 수 있도록 해주는 응용 프로그램


* 서버와 클라이언트

클라이언트는 정보를 서버에게 요청.
서버는 정보를 저장하고 클라이언트에게 정보 제공.
요청과 응답으로 서로 통신.


* URL

Uniform Resource Identifier(URL은 URI의 일종이라고 한다.). 인터넷에 있는 자원의 위치를 나타내는 주소.


* http와 https의 차이

보안여부. https는 정보가 서버로 갈때 중간과정에서 보안을 유지해주는데, http는 정보가 서버로 넘어갈때

보안과정이 없어서 개인정보 유출의 우려가 존재.
***
웹 프로그래밍
---
* 프론트엔드
우리 눈에 보이는 부분 개발


* 백엔드
server 관련 개발(눈에 보이지 않는 부분)


* 프레임워크
웹 프로그래밍에 있어 뼈대 역할.
vue.js나 react.js 이용하자.

***
웹의 기초, 개발환경 세팅
---
먼저 파이썬을 설치한 후, 가상환경을 만들어주었다.
* 가상환경이란?
파이썬을 여러가지 용도로 사용할 때 파이썬의 패키지들이 충돌할 수 있기 때문에, 
사용하고자 하는 용도에 따라 가상환경을 만들어 패키지 간의 충돌을 막아준다.

가상환경 세팅 시 cmd에서 다음과 같은 순서를 거친다.

```> pip install virtualenvwrapper-win```
* virtualenvwrapper-win을 설치하는 과정
* virtualenvwrapper-win : 현재 작업 디렉토리와 가상환경을 매핑해주는 파이썬 패키지

```> mkvirtualenv seminar```
* 'seminar'라는 가상환경을 생성하고 진입

### 자주 쓰는 명령어 목록
  + 가상환경 생성 : 
  ```> mkvirtualenv <ENVNAME>```
  + 가상환경 삭제 :
  ```> rmvirtualenv <ENVNAME>```
  + 만들어진 가상환경 목록 확인 :
  ```> workon```
  + 가상환경 활성화 :
  ```> workon <ENVNAME>```
  + 가상환경 비활성화 :
  ```> deactivate```
  
실제로 어제 만들었던 seminar 가상환경은

```workon```과 ```deactivate```를 통해 활성화/비활성화 가능했다.
***

Django 시작
---
```pip install Django```

가상환경 상에서 django 설치

```pip list```

설치 여부 확인. Django의 버젼을 확인할 수 있다.

```django-admin startproject myproject```

프로젝트 생성

```python manage.py runserver```

서버 시작
***

깃
---
깃 = 지옥에서 온 관리자

### 깃으로 할 수 있는것
> 1.버전 관리
>
> 2.백업
>
> 3.협업

1. 버전 관리
깃은 언제 어떤 것을 수정했는지 기록이 남는다.

2. 백업
깃허브는 원격 저장소로 쓰일 수 있다. 

3. 협업
어떤 팀원이 어떻게 자료를 수정했는지 기록이 남아 협업 툴로도 좋다.

### 깃 환경 설정
```git config --global user.name "원하는 이름"``` 내 이름 설정
```git config --global user.email "원하는 메일주소"``` 내 이메일주소 설정

### 리눅스 명령 연습
```pwd```

print working directory의 줄임말로 현재 위치 경로 나옴

```ls```

list의 줄임말. 현재 위치 경로의 파일들 목록을 보여준다.

```ls -a```

list all의 줄임말. 현재 위치 경로의 파일들 중에서 숨겨진 목록까지 모두 보여준다.

```cd```

change directory의 줄임말. 디렉토리 간 이동

```cd ..```

상위 디렉토리로 이동.

```cd 이동할 디렉토리 이름```

해당 위치 경로에서 하위 디렉토리로 이동할때 사용가능.

```cd ~```

~는 가장 홈 디렉토리로 돌아간다.

### 터미널에서 디렉터리 만들기 및 삭제
```mkdir hello-git```

mkdir은 make directory의 줄임말. hello-git 디렉터리 생성.

```rm```

remove 줄임말. 파일삭제가능

```rm -r```

폴더 삭제시 -r까지 붙여준다.

```vim hello.txt```

vim은 입력한 파일 이름과 같은 파일이 없다면 그 이름으로 새로운 문서 생성. 있다면 그 파일을 연다.

vim 일반모드 -> 입력모드

* a:커서 뒤에 입력

* i:커서 앞에 입력

* o:커서 다음줄에 입력

vim 입력모드 -> 일반모드

esc

vim 일반모드 -> 명령행 모드

콜론(:)

vim 명령행 모드 -> 일반모드

esc

