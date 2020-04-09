### 멋사 8기 숙제 제출 방법

1. `hyesoo5115/snulion8th` Fork
2. 본인 노트북의 원하는 위치에서 터미널에 다음 명령 입력하여 snulion8th 폴더 생성 및 초기 세팅
```bash
$ git clone 레포지토리 주소
$ cd snulion8th
$ git pull
$ git checkout -b hyungseok origin/hyungseok      <-- 자기 이름으로 된 브랜치 가져오기
$ git remote add upstream https://github.com/hyesoo5115/snulion8th.git  <--원본 레포지토리를 upstream이라는 이름으로 추가
```
3. 본인의 레포지토리인 `hyungseok-choi/snulion8th`에 수업 내용 및 과제 commit & push
4. 과제 완료 시 `hyesoo5115/snulion8th`의 **hyungseok** 브랜치로 Pull Request 요청
5. 과제 미완료 시 `hyesoo5115/snulion8th`의 master 브랜치에 올라온 정답 코드를 다음 명령으로 내 레포지토리의 master 브랜치에 불러오기
```bash
$ git fetch upstream
$ git checkout master
$ git merge upstream/master
$ git push origin master
```
