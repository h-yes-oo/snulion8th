# Javascript Introduction

자바스크립트 : 정적인 웹 문서에 동작을 부여하는 프론트엔드 개발 언어

> 자바스크립트 라이브러리/프레임워크 종류 
> 1. Jquery(라이브러리) : 자바스크립트의 함수들을 편하게 활용할 수 있도록 모아놓은 집합 
> 2. ReactJS(라이브러리) : UI구현을 위한 라이브러리, MVC 패턴에서 V에 집중
> 3. NodeJS(프레임워크): 웹 서버 프레임워크

> 라이브러리 vs 프레임워크?
>
> 1. 라이브러리 : 프로그램에서 필요로 하는 기능을 제3자가 사용할 수 있는 형태로 모아둔 것, 사용자가 활용하는 도구 
> 2. 프레임워크 : 애플리케이션의 전체 혹은 일부분의 형태를 규정 혹은 방침화, 사용자가 따라야 함 
 
## 콘솔 활용법
``` Javascript
console.log(5); 
console.log('Javascript study'); 
```
 콘솔 로그는 주로 개발하며 디버깅을 하기 위해서 사용
 
 저번 세미나에서도 ajax코드를 작성하면서 success, error 등의 단계에서 다른 콘솔 로그가 찍히게끔 코드를 작성한 후 개발자 도구를 통해 확인
 
 +) 자바스크립트는 큰따옴표와 작은따옴표의 겹침 오류를 주의해야 하며 string 내에 따옴표가 들어갈 경우 \\"와 같이 표기
 

## 주석 
``` Javascript
//한 줄 설명글인 경우 이렇게 처리
/*  
  설명글이 여러 줄인 경우
  이렇게 처리
*/
```


## 자료형
1. 문자형, 숫자형
``` Javascript
console.log('JavaScript'); //String 문자형
console.log(2011); //Number 숫자형
console.log('Woohoo! I love to code! #codecademy'); //String 문자형
console.log(20.49); //Number 숫자형
```
다른 언어와 다르게 integer, float의 구분이 없이 정수와 소수 모두 Number로 통일

2. 논리형
``` Javascript
var 변수이름 = true;
var 변수이름 = false;
var 변수이름 = Boolean(0); //false
var 변수이름 = Boolean("무언가 텍스트"); //true
```
Boolean() 메서드는 숫자0, null, undefined, 빈 문자("")를 제외한 모든 데이터에 대해 true 반환

3. null & undefined
``` Javascript
var 변수이름; //undefined
var n = "hello";
n = null;
```
undefined는 변수에 값이 등록되기 전의 기본값
null은 변수에 저장된 값이 null일 경우. null은 변수에 저장된 데이터를 비우고자 할 때 사용

## 연산자
``` Javascript
console.log(3 + 4); // Prints 7
console.log(5 - 1); // Prints 4
console.log(4 * 2); // Prints 8
console.log(9 / 3); // Prints 3
console.log(11 % 3); // Prints 2
console.log(12 % 3); // Prints 0
```
1. + : 더하기 
2. - : 빼기
3. * : 곱하기
4. / : 나누기
5. % : 나머지

## 문자열 연결
``` Javascript
console.log('hi' + 'ya'); // Prints 'hiya'
console.log('wo' + 'ah'); // Prints 'woah'
console.log('I love to ' + 'code.'); // Prints 'I love to code.'
```

## Property & Method
``` Javascript
console.log('Hello'.length); // Prints 5
console.log('hello'.toUpperCase()); // Prints 'HELLO'
console.log('Hey'.startsWith('H')); // Prints true
```
오브젝트의 property나 method는 오브젝트 뒤에 점을 찍고 접근


# 변수

## 변수 선언 방법: var, let, const
1. var : 자바스크립트 ES6 이전까지의 선언법
``` Javascript
var favoriteFood = 'pizza';
var numOfSlices = 8;
var numOfSlices = 10; // 변수의 재선언 가능
```

2. let : 자바스크립트 ES6 이후 재할당이 가능한 선언법
``` Javascript
let favoriteFood = 'pizza';
let numOfSlices = 8;
let numOfSlices = 10; // 변수의 재선언 불가 : Uncaught SyntaxError
  numOfSlices = 10; // 재할당은 가능
```

3. const : 자바스크립트 ES6 이후 재할당이 불가능한 상수 선언법
``` Javascript
const favoriteFood = 'pizza';
const numOfSlices; // 처음부터 변수 값 선언해야함 : Uncaught SyntaxError
const numOfSlices = 8;
const numOfSlices = 10; // 변수의 재선언 불가 : Uncaught SyntaxError
  numOfSlices = 10; // 변수의 재할당 불가 : Uncaught SyntaxError
```

var 이후에 let, const가 나온 이유?

var은 변수의 재선언이 가능함으로 긴 코드를 작성할 시에 실수로 이미 썼던 변수 이름을 다시 사용하는 경우 아무런 경고 없이 변경됨

이를 방지하기 위해 let, const로 재할당 가능 여부를 구분하여 새로운 선언법 등장

외에도 var은 function scope, let과 const는 block scope라는 차이점이 있음


## 대입 연산자
``` Javascript
levelUp += 5; // levelUp = levelUp + 5;
powerLevel -= 100; // powerLevel = powerLevel - 100;
multiplyMe *= 11; // multiplyMe = multiplyMe * 11;
quarterMe /= 4; // quarterMe = quarterMe / 4;
```

## 증감 연산자
``` Javascript
gainedDollar++; // gainedDollar = gainedDollar + 1;
lostDollar--; // lostDollar = lostDollar - 1;
```

## 변수와 문자열 연결
``` Javascript
let myPet = 'armadillo';
console.log('I own a pet ' + myPet + '.'); 
// Output: 'I own a pet armadillo.'
```
+를 활용해서 문자열과 변수 연결 가능

## 문자열 보간(String Interpolation)
``` Javascript
const myPet = 'armadillo';
console.log(`I own a pet ${myPet}.`);
// Output: 'I own a pet armadillo.'
```
문자열 내에 변수나 상수를 나타낼 때 사용하는 방법

연결보다 더 구조화된 형태로 여러 변수를 사용하는 하나의 템플릿을 작성할 때 사용

## typeof
``` Javascript
const unknown1 = 'foo';
console.log(typeof unknown1); // Output: string

const unknown2 = 10;
console.log(typeof unknown2); // Output: number

const unknown3 = true; 
console.log(typeof unknown3); // Output: boolean
```
변수의 자료형 반환
