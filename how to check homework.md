### 멋사 8기 숙제 제출 & 확인 방법

#### 학생 Lion의 입장
1. `hyesoo5115/snulion8th` Fork
2. 본인의 노트북의 원하는 위치에서 터미널에 다음 명령 입력하여 snulion8th 폴더 생성 및 초기 세팅
```bash
$ git clone 레포지토리 주소
$ cd snulion8th
$ git pull
$ git checkout -b Lion origin/Lion       <-- 자기 이름으로 된 브랜치 가져오기
$ git remote add upstream https://github.com/hyesoo5115/snulion8th.git  <--원본 레포지토리를 upstream이라는 이름으로 추가
```
3. 본인의 레포지토리인 `Lion/snulion8th`에 수업 내용 및 과제 commit & push
4. 과제 완료 시 `hyesoo5115/snulion8th`의 **본인** 브랜치로 Pull Request 요청
5. 과제 미완료 시 `hyesoo5115/snulion8th`의 master 브랜치에 올라온 정답 코드를 다음 명령으로 내 레포지토리의 master 브랜치에 불러오기
```bash
$ git fetch upstream
$ git checkout master
$ git merge upstream/master
$ git push origin master
```

#### 운영진의 입장
1. `Pull Request 보낸 사람 == 브랜치 주인` 인지 확인
2. 과제 확인 후 Pull Request 승인
3. 매주 `hyesoo5115/snulion8th`의 master 브랜치에 정답 코드 commit & push (커밋 메세지 "nth seminar answer")
