프리세미나 1주차(2020_04_11) Review
===

1.웹의 기초, 개발환경 세팅
---
먼저 파이썬을 설치한 후, 가상환경을 만들어주었다.
* 가상환경이란?
파이썬을 여러가지 용도로 사용할 때 파이썬의 패키지들이 충돌할 수 있기 때문에, 
사용하고자 하는 용도에 따라 가상환경을 만들어 패키지 간의 충돌을 막아준다.

가상환경 세팅 시 cmd에서 다음과 같은 순서를 거친다.

```> pip install virtualenvwrapper-win```
* virtualenvwrapper-win을 설치하는 과정
* virtualenvwrapper-win : 현재 작업 디렉토리와 가상환경을 매핑해주는 파이썬 패키지

```> mkvirtualenv seminar```
* 'seminar'라는 가상환경을 생성하고 진입

### 자주 쓰는 명령어 목록
  + 가상환경 생성 : 
  ```> mkvirtualenv <ENVNAME>```
  + 가상환경 삭제 :
  ```> rmvirtualenv <ENVNAME>```
  + 만들어진 가상환경 목록 확인 :
  ```> workon```
  + 가상환경 활성화 :
  ```> workon <ENVNAME>```
  + 가상환경 비활성화 :
  ```> deactivate```
  
실제로 어제 만들었던 seminar 가상환경은

```workon```과 ```deactivate```를 통해 활성화/비활성화 가능했다.

2.Django 시작
---
