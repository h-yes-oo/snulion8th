첫 세미나에서 웹의 기초에 대해 배웠습니다.

재밌는 자료로 가볍게 배웠지만 정말 중요한 개념입니다 :-)

그렇기에 여기에 새롭게 알게된 웹의 기초 내용을 정리해주세요-!

마크다운 문법에도 익숙해지시는 것을 권해드립니다.

---------------------------------------------


웹의 기초
==========
#### 웹 
인터넷에 연결된 사용자들이 문자, 영상, 음성 등이 혼합된 멀티미디어를 공유할 수 있는 공간
웹사이트는 웹페이지(html 파일)들이 하이퍼링크를 통해 연결된 구조
여기서 html이란 HyperText Markup Language로 웹 페이지를 만드는 기초적 언어

#### 브라우저
브라우저란 사용자가 웹 사이트에 접근할 수 있도록 해주는 응용 프로그램
한국에서는 크롬 - 익스플로러 - 엣지 - 웨일 - 사파리 - 파이어폭스 순의 점유율

#### 서버와 클라이언트
서버 : 서비스를 제공하는 컴퓨터로, 저장하고 있는 정보를 클라이언트에게 제공
클라이언트 : 서비스를 요청하는 요청자
서버와 클라이언트는 요청(Request)과 응답(Response)으로 통신

#### URL
URL은 Uniform Resource Identifier, 즉 URI의 일종으로 인터넷에서 자원의 위치를 나타냄
주소는 접근 방식(https://)과 네트워크 상의 위치(www.youtobe.com/~)로 이루어짐
+ http와 https의 차이는 보안 여부

웹 프로그래밍 이모저모 
====================

#### 프론트엔드와 백엔드
프론트엔드 : 클라이언트 쪽에서 실행되는, 사용자 눈에 보이는 부분을 개발
백엔드 : 서버 쪽에서 실행되는, 눈에 보이지 않는 부분 개발
데이터베이스 : 백엔드가 다루는 데이터를 보관하고 검색해 오는 기술

#### 프레임워크
프레임워크 : 웹 프로그래밍에서 뼈대 역할을 해주는 소프트웨어 환경
대표적인 프론트엔드 프레임워크로는 React.js, Angular.js, Vue.js가 있음
대표적인 프론트엔드 언어로는 html, css, javascript가 있음

대표적인 백엔드 프레임워크로는 Django, Node.js, Ruby on Rails가 있음
백엔드 언어는 Python, Java, Ruby, C 등 다양

깃 버전 관리
=============

깃의 핵심 기능은 버전 관리, 백업 협업

> #### 리눅스 명령어 연습
> > <pre><code>$ pwd</code></pre>
> > print workind directory의 약자로 현재 위치의 경로 표시
> >
> > <pre><code>$ ls</code></pre>
> > list의 약자로 현재 디렉터리의 디렉터리, 파일 목록 표시
> >
> > <pre><code>$ ls-a</code></pre>
> > 숨겨진 파일까지 표시
> >
> > <pre><code>$ cd</code></pre>
> > change directory의 약자로 디렉터리 사이를 이동할 때 사용
> >
> > <pre><code>$ cd ..</code></pre>
> >현재 위치의 상위 디렉터리로 이동
> >
> > <pre><code>$ cd 이동할 디렉터리 이름</code></pre>
> > 해당 디렉터리로 이동
> >
> ><pre><code>$ cd ~</code></pre>
> >가장 홈 디렉터리로 이동

> 터미널에서 디렉터리 만들기 및 삭제하기
> ><pre><code>$ cd 디렉터리 만들 위치</code></pre>
> ><pre><code>$ mkdir 디렉터리 이름</code></pre>
> ><pre><code>$ rm -r 지울 디렉터리 이름</code></pre>
> >
> 빔에서 텍스트 문서 만들기
> ><pre><code>$ cd 디렉터리 이름</code></pre>
> ><pre><code>$ vim 만들 파일 이름.txt</code></pre>
> >파일 이름과 같은 파일이 없다면 해당 이름으로 새로운 텍스트를 만들고 파일이 있다면 해당 파일 오픈
> >
> > 빔 일반 모드에서 a,i,o를 누르면 입력 모드, esc로 돌아감
> >빔 일반 모드에서 콜론(:)누르면 명령행 모드, esc로 돌아감
> >
> > :wq 저장하고 나가기 (write & quit)
> >
> 텍스트 문서 내용 확인하기
> ><pre><code>$ cat 문서 이름.txt</code></pre>
> >catch의 약자로 문서 내용을 확인 가능

>스테이지와 커밋 이해하기
> >깃의 작업 공간
> >1. 작업 트리 : 우리 눈에 보이고 파일 수정, 저장 등의 작업을 하는 디렉터리
> >2. 스테이지 : 버전으로 만들 파일이 대기하는 곳
> >3. 저장소 : 스테이지에서 대기하고 있던 파일들을 버전으로 만들어 저장하는 곳
>
>파일 스테이징하기
> ><pre><code>$ git status</code></pre>
> >깃의 상태를 확인하고 스테이징 할 파일 결정 (untracted files)
> >
> ><pre><code>$ git add 스테이징 할 파일.txt
> >$ git status</code></pre>
> >untracted files가 스테이지에 올라가 changes to committed로 바뀜
>
>스테이지에 올라온 파일 커밋하기
> ><pre><code>$ git commit -m "커밋과 함께 저장할 메세지"</code></pre>
> >커밋 메세지와 함께 파일 커밋
> >
> ><pre><code>$ git log</code></pre>
> >방금 커밋한 버전에 대한 설명
> >
> ><pre><code>$ git log --oneline</code></pre>
> >커밋을 간략하게 확인
>
>스테이징과 커밋 한번에 처리하기
> >이미 커밋한 적이있는 파일은 add와 commit 한 번에 처리 가능
> ><pre><code>$ git commit -am "커밋과 함께 저장할 메세지"
> >$ git log</code></pre>
> >확인해보면 새로운 버전이 만들어짐
> >
> 작업 되돌리기
> ><pre><code>$ git reset HEAD^
> >$ git log</code></pre>
> >확인해보면 가장 최근에 커밋한 내역이 사라짐
> >
> ><pre><code>$ git checkout 수정내역 지울 문서.txt
> >$ cat 수정내역 지울 문서.txt</code></pre>
> >깃 저장소 뿐만 아니라 작업 트리에서도 수정 내역이 사라짐

> 브랜치 : 버전 관리 시스템에서 여러 갈래로 퍼지는 데이터 흐름
>
> 브랜치 만들기
> ><pre><code>$ git branch </code></pre>
> >현재 브랜치 확인
> >
> ><pre><code>$ git branch 새로운 브랜치 이름</code></pre>
> >새 브랜치 만들기
> >
> ><pre><code>$ git checkout 넘어갈 브랜치 이름
> >$ git branch</code></pre>
> >확인해보면 원하는 브랜치로 넘어감
> >
> ><pre><code>$ git log --oneline --branches --graph</code></pre>
> >브랜치별 커밋 상황을 간략하게 그래프로 보여줌
>
>브랜치 병합하기
> ><pre><code>$ git checkout master
> >$ git merge 합칠 브랜치</code></pre>
> >마스터 브랜치에 합칠 브랜치의 문서가 반영, 합칠 브랜치에도 마스터 반영
