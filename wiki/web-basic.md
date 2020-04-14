마크다운 문법에도 익숙해지시는 것을 권해드립니다.

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
$git config user.name "younjoo" 사용자 이름 세팅

$git config --global user.name "younjoo" 컴퓨터의 모든 저장소에서 같은 사용자 이름 사용

$git config user.email "younjoo0614@snu.ac.kr" 사용자 이메일 세팅
--global 사용하면 위와 똑같이 컴퓨터의 모든 저장소에서 같은 정보 사용

$dir / ls : 디렉터리에 있는 파일 하위 디렉터리 목록 확인
- $ls -a : 숨겨진 파일까지 보기
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
  



  
  
