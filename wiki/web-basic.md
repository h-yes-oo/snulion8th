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

```
git reset HEAD 파일이름   <--add 후 commit 전인 파일 되돌리기
git reset HEAD^  <-- 최신 커밋 되돌리기
git reset 커밋해시 <-- 특정 커밋으로 되돌리기
git revert 커밋해시 <-- 커밋 삭제하지 않고 되돌리기
git restore / git checkout 
```

git branch <branch_name> #브랜치 만들기   
git checkout <branch_name>  #해당 브랜치로 이동   
git merge <branch_name>  #해당 브랜치를 현재 브랜치에 병합   
git log --oneline --branches --graph  #상황 모니터링   

