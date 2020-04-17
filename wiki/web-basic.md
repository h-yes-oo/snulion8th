**멋쟁이 사자처럼 1주차 세미나**
**2020.04.11 토요일**   

## 1. Web 기초
### 1.1. Web = **W**orld **W**ide **W**eb     
인터넷에 연결된 사용자들이 서로의 정보를 공유할 수 있는 공간     
텍스트, 그림, 소리, 영상 등의 정보를 제공하며 웹 페이지들이 모여 웹 사이트를 이룬다. 
* hyperlink: 문서 내부에서 또 다른 문서로 연결되는 참조    
### 1.2. Web Site, Web Browser     
Web Site: 서로 관련된 웹 페이지들의 집합     
Web Browser: 인터넷 망에서 정보를 검색하는 데 사용하는 응용 프로그램     
ex) Chrome, IE, Safari etc.     
### 1.3. HTML     
Hyper Text Markup Language, 기본 웹 프로그래밍 언어     
### 1.4. Server vs Client     
클라이언트의 정보 요청(Request)과 서버 응답(Response)로 서로 통신한다.    
서버는 DB(data base)에 저장된 정보를 돌려준다.     
Database: back-end가 다루는 데이터를 보관하고 있다가 전송한다.     
Client <-> Server <-> Database     
### 1.5. http vs https     
‘s’ 즉, secure의 유무,     
### 1.6. Frontend vs Backend     
Front-end: **Client**, 사용자 눈에 보이는 부분 개발     
Back-end: **Server**, 사용자 눈에 보이지 않는 부분 개발     
### 1.7. Framework    
구현되어 있는 프로그래밍 틀이자 뼈대 역할을 한다.     
**Frontend Framework : React.js, Anfular.js, Vue.js**   
1. React.js: 자유자래로 현란하게 내용의 변동 가능   
2. Vue.js: 비교적 간단    
3. Anfular.js: 무겁고 어렵다    

**Frontend Language : HTML, CSS, Javascript**    
1. HTML: structural 뼈대, 웹 페이지의 구조    
2. CSS:  presentational 디자인     
3. Javascipt: behavioral 주요 기능 구현    

**Frontend Framework : 다양하다.**    
**Backend Language : Python, C, C++ etc.**    

## 2. Git의 기초       
### 2.1.  깃(Git) 사용법    
버전 관리 Version Control: 하나의 code file의 수정내역 변경사항 관리 용이     
백업 Backup: GitHub라는 원격저장소에 백업 파일 저장 가능     
협업 Calloaboration: 다른 이들과의 협업 용이    

### 2.2. 깃(Git) 환경 설정하기    
+ 이름과 메일 주소의 설정시 -> git config 명령    
+ 현재 컴퓨터 내 같은 사용자 정보 사용 -> --global    
~~~ 
$ git config --global user.name "원하는 이름"
$ git config --global user.email "원하는 메일주소“
~~~ 

### 2.3. 깃(Git)으로 버전 관리하기    
### 2.3.1. 깃 저장소 만들기
**저장소(repository)** 
+ 원격저장소(깃허브-Gitbub)
+ 로컬저장소(컴퓨터)   
+ 디렉토리 초기화 -> git init    
+ 현재 디렉토리 살펴보기 -> ls –a (숨겨진 .git 디렉토리를 보는 옵션) 
~~~ 
$ git init
$ ls –a 
~~~ 
### 2.3.2. Stage(스테이지)와 Comit(커밋)이해   
>1. 작업트리(working tree)     
>2. 스테이지(staging area)       
>3. 저장소(repository)        
 
1. 작업트리(working tree)     
**작업 디텍토리**로, 파일 수정 저장 등의 작업을 한다.     

2. 스테이지(staging area)       
파일이 **대기** 하는 곳으로 .git 디렉토리의 index 파일에 저장된다.     

3. 저장소(repository)      
대기하는 파일을 버전으로 만들어 저장하는 곳으로 .git 디렉토리의 HEAD 파일에 저장된다.     

### File Staging         
**git add**     
+ 깃의 상태 확인 -> git status     
+ 스테이징 -> git add    
~~~    
$ git add hello.txt
$ git status 
~~~  

### File Commit     
**git commit**      
+ 저장소에 올리기 -> git commit     
+ 변경 메시지 기록 -> -m     
+ 만들어진 버전 확인 -> git log    
~~~     
$ git commit -m "hello.txt created“
$ git log
~~~ 

### Staging + Commit     
+ add와 commit을 한 번에 처리! -> git commit –am      
~~~ 
$ git commit -am "second text in hello.txt" 
$ git log 
~~~    

### 작업 되돌리기    
+ 마지막 커밋 취소 -> git reset HEAD^     
~~~    
$ git reset HEAD^
$ git log
~~~   
작업트리 수정 내역 지우기(작동하지 않을 시 git checkout 사용)    
버전이 원래로 돌아간다.      
~~~
$ git restore hello.txt   
~~~    

~~~   
$ git reset HEAD 파일이름   <--add 후 commit 전인 파일 되돌리기
$ git reset HEAD^  <-- 최신 커밋 되돌리기
$ git reset 커밋해시 <-- 특정 커밋으로 되돌리기
$ git revert 커밋해시 <-- 커밋 삭제하지 않고 되돌리기    
~~~    

### 2.3.3. 브랜치(Branch) 이해     
버전 관리 시스템의 여러 갈래의 흐름. 즉, 데이터 흐름을 의미한다.     
여러 가지의 작업을 독립적으로 수행가능 – 합치거나 합치지 않거나!     
기능 별 버전 작업으로 오류나 기능 제거 시의 관리 편리함.     

#### 브랜치(Branch) 만들기     
현재 위치한 master branch는 저장소 생성시 기본적으로 만들어짐.    


~~~ 
$ git branch    
~~~ 
+ 브랜치 추가 후에 생성 확인 -> git branch      
~~~ 
$ git branch eumjoo
$ git branch jinjoo
$ git branch 
~~~ 
+ commit 확인 -> git log —oneline     
커밋, 브랜치 등을 한눈에 확인 -> git log —oneline —branches —graph    
~~~
$ git log —oneline
$ git log —oneline —branches —graph   
~~~ 
+ branch 이동 -> git checkout
git branch로 확인 시에 브랜치 이름 앞에 별표(*)가 찍힌다면 성공! 
~~~ 
$ git checkout eumjoo
$ git branch 
~~~ 


#### 브랜치(Branch) 병합하기 
+ 하나로 합친다 -> git merge     
~~~ 
$ git checkout master
$ git merge eumjoo
~~~ 

conflict가 발생할 경우에는 vim으로 파일을 열고,      
사용자가 직접 충돌 부분을 해결하고, 다시 커밋을 진행한다.    
~~~ 
$ git commit -am "merge eumjoo branch"
$ git log --oneline —branches --graph
~~~ 

## 3. 리눅스 명령어 

~~~ 
$ pwd            <-- 현재 디렉토리 표시
$ ls             <-- 현재 파일 목록 표시
$ mkdir test     <-- test라는 디렉토리 생성 
$ cd ~           <-- 홈 디렉토리로 이동
$ cd test        <-- 하위 디렉토리(test)로 이동 
$ cd ..          <-- 상위 디렉토리로 이동
$ vim hello.txt  <-- 파일 생성
$ rm hello.txt   <-- 파일 삭제
$ rm -rf test    <-- test 디렉토리 삭제 -rf는 파일의 존재유무에 상관없이 디렉토리 삭제 
~~~
 
