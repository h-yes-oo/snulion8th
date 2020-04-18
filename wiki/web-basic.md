# 웹의 기초
***
## 가상환경 설정

가상환경의 사용 이유: 프로젝트마다 필요로 하는 패키지의 버전이 달라서 충돌할 수 있기 때문
```
pip install virtualenvwrappper-win  #설치   
mkvirtualenv <envname>  #가상환경 만들기   
rmvirtualenv <envname>  #가상환경 삭제   
workon <envname>   #가상환경 활성화   
workon #가상환경 리스트 확인   
deactivate  #가상환경 비활성화   
 *deactivate: command not found 에러는 계정이 한글이어서 생김
```
***
## Django 시작하기   
```
pip install Django
django-admin startproject myproject
cd myproject
python manage.py runserver
```
***
## 깃 사용법
깃 = 백업, 버전 관리를 위한 툴
깃허브 = 협업을 위한 툴
```
 Working directory    우리가 일하는 곳     
  --(add)--    
 Staging area         파일이 대기하는 곳    
  --(commit)--   
 Repository           버전으로 만들어서 저장되는 곳    
```

기초 명령어
```
git config --global user.name   #username 지정
git config --global user.email  #user_email 지정
git init   #깃 시작   
git status #깃 상태 확인   
git log    # 로그 확인 (누가 커밋을 만들었는지, 만든 시간, 커밋 메시지)   
```
  

처음 버전을 만들때는 git add 와 git commit 을 따로따로 해줘야 한다.   
```
git add hello.txt   
git commit -m "hello.txt created"  # -m 메시지를 같이 저장   
```

두번째 버전을 만들때부터는 한번에 처리 가능   
```
git commit -am    # -a add, -m 메시지
```

기타 여러가지 깃 명령어
```
git reset HEAD 파일이름   <--add 후 commit 전인 파일 되돌리기
git reset HEAD^  <-- 최신 커밋 되돌리기
git reset 커밋해시 <-- 특정 커밋으로 되돌리기
git revert 커밋해시 <-- 커밋 삭제하지 않고 되돌리기
git restore / git checkout 
```

브랜치 명령어
```
git branch <branch_name> #브랜치 만들기   
git checkout <branch_name>  #해당 브랜치로 이동   
git merge <branch_name>  #해당 브랜치를 현재 브랜치에 병합   
git log --oneline --branches --graph  #상황 모니터링   
```
