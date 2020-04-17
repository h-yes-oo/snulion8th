첫 세미나에서 웹의 기초에 대해 배웠습니다.

재밌는 자료로 가볍게 배웠지만 정말 중요한 개념입니다 :-)

그렇기에 여기에 새롭게 알게된 웹의 기초 내용을 정리해주세요-!

마크다운 문법에도 익숙해지시는 것을 권해드립니다.

하하하 나는 깃을 배웠지 하하하 멋쟁이 사자처럼 대만세

깃 = 백업, 버전 관리를 위한 툴
깃허브 = 협업을 위한 툴

git config --global user.name
git config --global user.email

mkdir hello-git
cat  #읽기
vim  #수정 

git init   #깃 시작
git status #깃 상태 확인
git log    # 로그 확인 (누가 커밋을 만들었는지, 만든 시간, 커밋 메시지)

Working directory --(add)-- Staging area --(commit)-- Repository
우리가 일하는 곳      파일이 대기(버전으로 만들고 싶은)  버전으로 만들어서 저장

처음 버전을 만들때는 git add 와 git commit 을 따로따로 해줘야 한다.
git add hello.txt
git commit -m "hello.txt created"  # -m 메시지를 같이 저장

두번째 버전을 만들때부터는 한번에 처리 가능
git commit -am    # -a add, -m 메시지

$ git reset HEAD 파일이름   <--add 후 commit 전인 파일 되돌리기
$ git reset HEAD^  <-- 최신 커밋 되돌리기
$ git reset 커밋해시 <-- 특정 커밋으로 되돌리기
$ git revert 커밋해시 <-- 커밋 삭제하지 않고 되돌리기
$ git restore / git checkout 
