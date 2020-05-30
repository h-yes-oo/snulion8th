Git‘s Functions
1. version control
2. backups in GitHub
3. collaboration

Gitbash – 일종의 명령프롬포트; console

Git 환경설정
1. 버전을 저장할 때마다 사용자 정보를 함께 저장
2. $ git config : 저장 명령어
3. --global : 현재 컴퓨터의 모든 저장소에서 같은 사용자 정보를 사용하도록 설정
4. $ git config --global user.name "원하는 이름"
5. $ git config --global user.email "원하는 메일주소“

명령어
pwd : 현재 위치의 경로
ls : 현재 디렉터리 내 파일 및 디렉터리 확인
ls –a : 숨겨진 파일까지 확인 가능
cd .. : 상위 디렉터리로 이동
cd 이동할 디렉터리 이름 : 하위 디렉터리로 이동
mkdir A : A 디렉토리 생성
rm A : A 디렉토리 삭제
rm –r A : A 디렉토리 하위 디렉토리 및 파일까지 삭제
vim A.txt : vim 텍스트 편집 터미널에서 해당 디렉토리에서 A.txt 생성
	:w : 저장
	:q : 종료
	:wq : 저장 및 종료
cat A.txt : 터미널 창에서 vim 켜지 않고 문서 내용 확인 가능

Git으로 버전 관리
1. git init : 해당 디렉토리에서 깃을 사용할 수 있도록 초기화 => ls –a (.git디렉토리는 감춰져 있으므로 이로써 확인 가능)
2. working directiory = git add A.txt => staging area = git commit –m“message” (버전에 어떤 변경사항이 있었는지 확인하기 위한 meesage도 함께 기록) => repository
3. git status : 깃 상태 확인
4. git log : 버전 생성 및 메시지 확인
5. 한번이라도 커밋한 적이 있는 파일은 add와 commit을 한 번에 처리 할 수 있음
	git commit –am “message” 
6. git reset HEAD^ : 마지막 커밋 취소
7. git restore A.txt : 작업 트리에서의 수정 내역 지우기
8. git checkout A : A branch로 이동

브랜치 관리
1. git branch A : 깃에서 브랜치 A 생성 및 확인 
2. git log —oneline : 커밋 한 줄로 간략 확인 가능

브랜치 병합하기
git merge A : 현재 브랜치에서 A브랜치 병합 - 충돌 시 : txt 문서를 수정 후 병합 가능
