## 프리세미나 1주차

  ### 웹의 기초
    웹(World Wide Web)
    웹 페이지(html)이 hyperlink를 통해 연결되어 웹 사이트를 구성
    
    서버와 클라이언트가 요청과 응답으로 통신
    
    프레임워크는 웹 프로그래밍의 뼈대 역할,
    사용하는 프레임워크에 맞는 언어를 이용하여 프로그래밍
    
  ### 개발환경 세팅
    패키지들의 충돌 방지를 위해 seminar 가상환경에서 프로그래밍
    가상환경 명령어
    - mkvirtualenv <ENVNAME> / rmvirtualenv
    - workon <ENVNAME> / deactivate
    
    VS Code: Python, Django 설치
  
  ### 깃을 이용한 버전관리
    깃의 핵심 기능: 우리는 프로그램 말고 CLI 이용
    - 버전 관리
    - 백업
    - 협업
    
    터미널 명령어
    - pwd: 현재 위치의 경로
    - ls(dir): 디렉터리 파일 확인
    - cd: change directory
    - mkdir / rm (-r 하위 디렉터리와 파일도 삭제)
    - vim: 텍스트 편집기
      + 입력모드: a, i, o / 명령행모드: 콜론
    - cat: 텍스트 파일 내용 확인
    
    스테이지와 커밋
    1. 작업 트리
    2. 스테이지
    3. 저장소
      - git add: 스테이징
      - git commit: 스테이지에서 저장소로 (-m 함께 저장하는 메세지)
        (git commit -am으로 한꺼번에)
      - git reset: 커밋 취소
      - git restore: 작업 트리에서 수정내역도 삭제
      
    브랜치 이해하기
    - git branch: 브랜치 형성
    - git oneline: 커밋 확인 (git log --oneline --branches --graph)
    - git checkout: 브랜치로 이동
    - git merge: 브랜치 병합
