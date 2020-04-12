첫 세미나에서 웹의 기초에 대해 배웠습니다.

재밌는 자료로 가볍게 배웠지만 정말 중요한 개념입니다 :-)

그렇기에 여기에 새롭게 알게된 웹의 기초 내용을 정리해주세요-!

마크다운 문법에도 익숙해지시는 것을 권해드립니다.
================================================================
주요내용
0. 계정이름이 한글이면 Python 가상환경 설정후 deactivate 명령어가 되지 않는다.
1. Web 기초
2. Python
  2.1 Python
  2.2 Virtualenv
  2.3 Django
3. Git
  3.1 Git structure
  3.2 Git command
  
1. Web 기초
  웹사이트 < 웹페이지 by HTML(Hyper Text Markup Language)
  Client ----Request----> Server
  Server ----Responce----> client
  Frontend
    Framework : Vue.js , React.js, Angular.js .. Language : HTML, CSS, Javascript ..
  Backend
    Framework : Django, Node.js, Ruby on Rails .. Language : Python, Java, Ruby, C ..
  
2. Pyhton
  2.1 Python (cmd)
    python --version: Python 버전 확인(나: 3.8.2)
    pip --version: Python의 pip버전 확인 (나: 20.0.2)
  2.2 Virtualenv (cmd)
    pip install virtualenvwrapper-win: 가상환경 사용을 위한 사전 설치 파일
    mkvirtualenv <envname>: 가상환경 생성
    rmvirtualenv <envname>: 가상환경 삭제
    workon: 가상환경 리스트 확인
    workon <envname>: 해당 가상환경 활성화
    Deactivate: (가상환경 진입 후) 가상환경 비활성화
  2.3 Django
    가상환경 상태에서! ((cmd)pip install Django) -> ((cmd)django-admin startproject <projectname>)
    -> ((cmd)cd myproject) -> ((cmd)python manage.py runserver)
    주소창에 localhost:8000 입력시 로켓 나오면 성공.
3. Git
  3.1 Git structure
    프로그램 사용 vs CLI 중 VS CODE는 후자.
    Windows의 경우 VS CODE의 Terminal에서 cmd가 아닌 git bash를 사용.  
    3가지 공간 존재
    1. Working directory 2. Staging area 3. Repository
    Staging area가 버퍼같은 느낌임.
    브랜치는 공동작업 혹은 분할작업을 할때 유용한 기능.
  3.2 Git command (Git bash)
    pwd: 현재 디렉토리
    ls: 현재 디렉토리의 파일 확인 (-a 사용시 숨겨진 파일 표시)
    cd: 디렉토리 변경(.. 사용시 상위 디렉토리 ~사용시 홈 디렉토리)
    mkdir <name>: 폴더(디렉토리) 생성  <-> rm: 디렉토리 삭제(-r 사용시 하위 디렉토리까지 삭제)
    vim <file>: 파일 생성 or 편집. 입력모드-i 명령행 모드- :wq 사용시 저장 및 나가기
    cat <file>: 텍스트 파일 내용 확인
    git status: 현 디렉토리내의 파일 상태 확인
    git add: Working directory -> Staging area 이동
    git commit: Staging area -> Reposirory 이동 (-m랑 같이 사용해서 메시지입력 해줘야함 -am 사용시 add, commit 동시에 가능)
    git log: 버젼 기록 확인 (--oneline 사용시 커밋 간략하게 확인가능, --branches --graph사용시 브랜치 현황 파악 용이)
    git branch <branchname>: 브랜치 생성
    git checkout <branchname>: 브랜치 <-> 브랜치 이동
    git merge <branchname>: 브랜치간 내용 병합 - 충돌이 일어날 수 있으나 사용자가 해결 후 커밋가능
    
    
    
    
    
