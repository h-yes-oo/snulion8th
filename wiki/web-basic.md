# 웹의 기초
## 개발환경 세팅
### 가상환경, python
- mkvirtualenv <envname> :가상환경 생성
  - ex) mkvirtualenv seminar 이 다음부터 cmd 라인에는 (seminar) > 이렇게 나타남
- rmvirtualenv <envname> :가상환경 삭제
- workon: 가상환경 목록 확인
  - workon <envname> : 가상환경 활성화
  - deactivate : 가상환경 비활성화
- pip 파이썬 패키지 관리자 
  - pip install <package name>: 패키지 설치
    - ex) pip install Django
  - pip list : 패키지 목록 확인
  - django-admin startproject <project name> :프로젝트 생성
 
## GIT
Command Line Interface 

vs code 터미널을 bash로 바꾸고 명령어 입력 

- 버전관리
- 백업
- 협업

### git 명령어
$git init : 디렉터리에서 깃을 사용할 수 있도록 초기화 $ls -a 해보면 .git 이름의 repository 생성

$git config user.name "younjoo" 사용자 이름 세팅

$git config --global user.name "younjoo" 컴퓨터의 모든 저장소에서 같은 사용자 이름 사용

$git config user.email "younjoo0614@snu.ac.kr" 사용자 이메일 세팅
--global 사용하면 위와 똑같이 컴퓨터의 모든 저장소에서 같은 정보 사용

$dir / ls : 디렉터리에 있는 파일 하위 디렉터리 목록 확인
- $ls -a : (브랜치, 디렉토리 등에서) 숨겨진 파일까지 보기

$cd <filename> :change directory
  - $cd..: 한 단계 상위 폴더로 이동
  - $cd~ : 가장 홈 디렉터리로 이동
  
$mkdir <filename> :make directory
  
$rm <filename> :remove directory
  - $rm -r : 디렉터리 안에 있는 하위 디렉터리와 파일까지 삭제
  
$vim <textname> : 텍스트 파일 생성 
- 같은 이름 파일이 있으면 그 파일을 오픈 
- a, i, o 입력모드 esc-> 일반 모드
- ; 명령 모드 esc-> 일반 모드
  - 명령 모드에서 ;w ;q ;wq write, quit, write quit 한 번에
  
-$cat <textname> : 텍스트 파일 내용 확인
  
$git add : 파일을 스테이지로 보내 버전으로 만들기 위해 대기

$git commit : 스테이지에 있는 파일을 repository로 보내 버전으로 저장
- $git commit -m "changes" : 버전의 변경사항을 함께 기록
- $git commit -a : 한 번 $git add를 한 파일에 대해 스테이징과 커밋을 한 번에
- $git commit -am "changes":  한 번 $git add를 한 파일에 대해 스테이징과 커밋과 메세지를 한 번에

$git log: 버전 설명, 만든 사람, 시간 , 커밋 메세지 확인
-$git log --oneline : 버전, 커밋 메세지 커밋 간단하게 확인
-$git log --oneline --branches --graph : 브랜치들의 상황을 그래프로 확인 

$git reset HEAD^ : 마지막에 한 커밋 취소 수정된 채로 파일이 남고 스테이징되지 않은 상태
- $git restore : 작업트리에서도 수정내역 삭제 안 될 경우 $git checkout 사용(?)
- $git reset HEAD <filename> : add 후 commit 전인 파일 되돌리기 
  
$git branch : 브랜치 확인 옆에 * 표시되는 브랜치가 현재 있는 브랜치
- $git branch <branchname> : 브랜치 생성 
  
$git checkout <branchname> : 해당 브랜치로 이동
  
$git merge <branchname> *표시된 head 브랜치에 해당 브랜치 병합
- 같은 파일 이름 때문에 conflict가 일어나면 해당 파일을 열어 각 브랜치에 있는 내용을 원하는 대로 통합해서 저장
- 위 내용에서 파일을 다시 편집하고 저장할 때는 $git commit -am으로 스테이징, 커밋

### 스테이지와 커밋
1. 작업트리: .git repository를 포함하는 디렉터리

2. 스테이지: 작업 트리에서 만든 파일 중 버전으로 만들 파일을 스테이지로 넘겨 대기 .git index에 저장
- $git add

3. repository: 버전들이 저장되는 곳.git의 HEAD에 저장
- $git commit -m $git commit -a $git commit -am 

### 브랜치
브랜치를 생성하면 같은 파일을 여러 브랜치에서 각각 편집
- $git branch $git chechout <branchname> $git merge <branchname> 
