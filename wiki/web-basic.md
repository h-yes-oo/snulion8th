## 1주차: 웹기초, 개발환경 세팅, 깃 세미나
## 1.1 웹 기초
### 1.1.1 웹(WWW)이란? <br/>
- 인터넷에 연결된 사용자들이 문자, 영상, 음성 등이 혼합된 멀티미디어를 공유할 수 있는 공간을 [**W**orld **W**ide **W**eb](https://en.wikipedia.org/wiki/World_Wide_Web)이라 한다.
- 수많은 웹 페이지들(html 파일들)이 연결되어 하나의 웹 사이트가 이루어지며 이들은 서로 [hyperlink](https://en.wikipedia.org/wiki/Hyperlink)를 통해 연결된다. 

### 1.1.2 HTML이란?<br/>
- [HyperText Markup Language](https://ko.wikipedia.org/wiki/HTML)의 약어로 웹 페이지를 만들어내는 마크업 언어이다. 
### 1.1.3 브라우저란?<br/>
- 사용자가 웹 사이트에 접근할 수 있도록 해주는 응용 프로그램이다.
### 1.1.4 서버와 클라이언트
- 서버(Server): 제공자(provider) 서비스를 제동하는 컴퓨터. 저장하고 있는 정보를 클라이언트에게 제공한다.
- 클라이언트(client): 서비스를 요청하는 요청자.

> 예시) <br/>
클라이언트: 이거 내 id/pw야. 로그인 시켜줘 *(요청 보내기)*<br/>
서버: *(요청 받음)* 너한테 받은 id/pw로 DB에서 널 찾아 결과를 보내줄게.<br/>
서버: 로그인을 성공적으로 시켜줄게. *(응답 보냄)* 첨부: (사용자_로그인_결과.json)<br/>
클라이언트: *(응답 받음)* 로그인 완료!

- 위와 같이 서버와 클라이언트는 **요청**(**reguest**)과 **응답**(**response**)로 통신한다. 
### 1.1.5 웹 서비스 개발
- Front-end: Clinet 쪽에서 실행되는 사용자 눈에 보이는 부분 개발
- Back-end: Server 쪽에서 실행되는 사용자 눈에 보이지 않는 부분 개발
- Database: 백엔드가 다루는 데이터를 보관하고 검색해 오는 기술
### 1.1.6 프레임워크
**프레임워크(framework)는 프로그래밍에서 있어서 뼈대 역할을 해준다.**
- Front-end 프레임워크와 언어:<br/>

<img src="https://user-images.githubusercontent.com/33405572/79206567-79098b80-7e7a-11ea-958b-24863a63fc83.png" alt="React vs Angular vs Vue" width="450">

> React.js: 흔히 보는 웹사이트들보다 우아하고 현란하게 바뀔 내용이 많은 경우. Facebook에서 개발 <br/>
Angular.js: 덩치크고 어려운 놈... Google에서 개발 <br/>
Vue.js: Angular.js의 쉬운 버전. 간단한 화면 요소들만 필요하다면 비교적 간단한 Vue.js 추천 <br/>

<img src="https://user-images.githubusercontent.com/33405572/79206558-76a73180-7e7a-11ea-9277-60c2c3cf5d58.jpeg" alt="html, css, js" width="450">

> HTML: 웹 문서의 본문을 적는 text 포맷 <br/>
CSS: HTML로 만든 웹 문서의 스타일을 다루는 속성 <br/>
Javascript: 웹 브라우저가 이해하고 실행할 수 있는 프로그래밍 언어 <br/>

- Back-end 프레임워크와 언어: <br/>

<img src="https://user-images.githubusercontent.com/33405572/79206447-4f506480-7e7a-11ea-9a4a-ee421ddee09a.jpg" alt="Backend frameworks" width="450">

> Back-end frameworks: 다양하다...!

> Back-end 언어: Python, C, C++ 등등 you name it.

### 1.1.7 앞으로 멋사에서!
- 프론트엔드는 프레임워크 없이 HTML, CSS, js로 개발!
- 백엔드는 Django이용하여 개발!

<br/>[웹 기초 세미나 자료](https://drive.google.com/file/d/1Jz9U_Pg_qR-oNSTR3MyeX7_s-hg-z2PQ/view)

## 1.2 깃(git) 기초

<img src="https://user-images.githubusercontent.com/33405572/79422127-3d480080-7ff7-11ea-9561-1a9d7f4e00f9.png" alt="git logo">

### 1.2.1 Git 소개
>1. 버전 관리 Version control
>2. 백업 Backup
>3. 협업 Collaboration

위 세 가지를 편하게 해주는 git. ~~여기에 [갓소](https://namu.wiki/w/%EB%A7%88%EC%9D%B4%ED%81%AC%EB%A1%9C%EC%86%8C%ED%94%84%ED%8A%B8)의 github까지 있으면 금상첨화!~~

[Github Desktop](https://desktop.github.com/)이나 [TortoiseGit](https://tortoisegit.org/)같은 GUI를 이용하면 초보자도 손쉽게 복잡한 git을 이용할 수 있다. 

그러나 현업에선 CLI(Command Line Interface)를 더 많이 쓴다고 하니 CLI 사용법을 잘 알아두도록 하자. 

### 1.2.2 Git 초기 설정하기
Git을 먼저 사용자 컴퓨터에 설치를 했으면 다음을 실행하여 사용자 정보를 저장하자. 
~~~
$ git config --global user.name "원하는 이름"
$ git config --global user.email "원하는 메일주소"
~~~

### 1.2.3 Git 버전 관리하기
#### Git 저장소 만들기 
Git을 사용하고자 하는 디렉토리로 이동한 후 git을 초기화해보자. 
~~~
$ git init
~~~
이제부터 이 디렉토리에서 git을 사용할 수 있다. 
#### Stage, commit 이해하기
Git은 파일의 모든 수정 내역들을 저장하기 위해 3개의 공간을 사용한여 데이터를 저장한다. 이 3개의 공간을 각각 Working directory, staging area, repository라고 한다.

<img src="https://user-images.githubusercontent.com/43427306/78852322-f2f2dc80-7a56-11ea-8c56-12cc754d449a.png" alt="git stage">

1. Working directory<br>
사용자가 작업하는 공간이다. 사용자가 어떻게 수정을 하든 모든 데이터가 있는 repository에는 영향을 미치지 않는다. 
2. Staging area<br>
말 그대로 모든 데이터가 있는 repository에 넘겨주기 전 파일들이 대기하는 곳이다. Working directory에서 `$ git add` 명령어로 이곳에 수정된 파일을 추가할 수 있다. 
3. Repository<br>
보통 사용자 컴퓨터가 아닌 github나 bitbucket 같은 원격 저장공간에 위치한다. 모든 데이터 히스토리가 저장되는 곳이라고 보면 된다. Staging area에 있는 파일들을 `$ git commit` 명령어로 commit을 해주면 repository에 저장된다. 

#### Branch 
Branch란, 버전 관리 시스템에서 여러 갈래로 퍼지는 데이터 흐름을 가리키는 말이다. <br>
Branch를 이용하므로써 개발 프로세스를 세분화하고 협업할 수 있게 해준다.
간략한 사용법은 아래와 같다. 
~~~
$ git branch intro  # making a new branch named 'intro'
$ git checkout intro    # moving to 'intro' branch
$ git commit -am "something"    # doing something on the branch
$ git checkout master   # moving to 'master' branch
$ git merge intro   # merging'intro' branch to 'master' branch
~~~
아래 사이트에서 banch를 연습해보도록 하자. <br>
[Learn git branching!](https://learngitbranching.js.org/)