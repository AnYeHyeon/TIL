# Week 2 : JavaScript+Jquery, DB SQL + DB Modelling
# Quest 03. 자바스크립트와 DOM

## Introduction
* 자바스크립트는 현재 웹 생태계의 근간인 프로그래밍 언어입니다. 이번 퀘스트에서는 자바스크립트의 기본적인 문법과, 자바스크립트를 통해 브라우저의 실제 DOM 노드를 조작하는 법에 대하여 알아볼 예정입니다.

## Topics
* 자바스크립트의 역사
* 기본 자바스크립트 문법
* DOM API
  * `document` 객체
  * `document.getElementById()`, `document.querySelector()`, `document.querySelectorAll()` 함수들
  * 기타 DOM 조작을 위한 함수와 속성들
* 변수의 스코프
  * `var`, `let`, `const`
* 현재의 동향
SPA (Single Page Application) 라이브러리나 프레임워크(React, View, Angular)를 통해 쉽게할 수 있음.
Web Assembly어로 다양한 언어로 웹브라우저에서 동작하도록 할 수 있음.

## Resources
* [자바스크립트 첫걸음](https://developer.mozilla.org/ko/docs/Learn/JavaScript/First_steps)
* [자바스크립트 구성요소](https://developer.mozilla.org/ko/docs/Learn/JavaScript/Building_blocks)
* [Just JavaScript](https://justjavascript.com/)

## Contents 1. Javescript
### 1. 변수
- 예약어 사용하지 않기
- 변수는 문자와 숫자, $와 _만 사용
- 첫글자는 숫자가 될 수 없다.
- 가급적 상수는 대문자로.
- `console.log(age)`
- `let` : 변할 수 있는 값. 이미 사용시 에러 발생
- `const` : 변하지 않는 값

### 2. 자료형
- 문자형 String :
``` "Mike", 'Mike', `Mike` ```
```
const name = "Mike";
const message3 = 'My name is ${name}`;

const message4 = `나는 ${30+1}살 입니다.`;
console.log(message4)

console.log(6 % 4) // 나머지
```
- booleam
- 객체형 typeof : null != 객체가 아니다
- 대화상자 : 
  - alert() : 띄워주기
  - prompt() : 입력받을 수 있음
    ```
    const name = prompt("예약일을 입력해주세요.", "2023-07-")
    ```
  - comfirm() : 확인과 취소버튼이 함께 있다.
    ```
    const isAdult = confirm("당신은 성인 입니까?");
    console.log(isAdult);
    ```

### 3. 형변환
- String() : 문자형으로 변환
- Number() : 숫자형으로 변환, 문자가 있으면 -> NaN
- Boolean() : 불린형으로 변환, 숫자 0, null, undefined false
-> 명시적 형변환을 통해서 지정해주는 것이 좋음.

### 4. 연산자
- %는 어디다가 쓸까? -> 홀짝
- 연산자의 전후
```
let num = 10;
let result = num++; // 증가시키지 전의 값
console.log(result);
```

### 5. 비교연산자
- == : 동등연산자
- === : 일치 연산자 (타입도 고려)
- !=

### 6. 조건문
- if-else : 
```
if(age>19) {
  console.log("환영합니다.")
} else {
  console.log("안녕히가세요.")
}
```

### 7. 논리연산자
- || : or
- && : and
- ! : not
```
const gender = 'F';
const name = 'Jane';
const isAdult = true;

if (gender==='M' && name==='Mike' || isAdult) {
  console.log('PASS')
} else {
  console.log('돌아가.')
}
>>> PASS -> and가 or보다 우선순위가 높다

if (gender==='M' && (name==='Mike' || isAdult)) {
  consule.log('PASS')
} else {
  console.log('돌아가.')
}
```

### 8. 반복문
- for
```
for (초깃값, 조건, 코드 실행 후 작업)
```
- while
```
let i = 0;

while(i<10) {
  console.log(i);
  i++;
}
```
- do.. while : 최소 1번은 코드를 실행함.
```
let i = 0;
do {
  i++
} while (i<10)
```
- break : 멈추고 빠져나옴
```
while(true) {
  let answer = confirm("계속 할까요?");
  if(!answer) {
    breake;
  }
}
```
- continue : 멈추고 다음 반복으로 진행
```
for (let i = 0, i < 10, i++) {
  if(i%2) {
    contine;
  }
  console.log(i)
}
```
### 9. switch
- 케이스가 많은 경우 if else보다 효율적으로 사용가능하다.
```
swich(평가항목) {
  case A : 
    console.log('')
    break;
  case B :
    break;
  default:
    console.log('')
}
```

### 10. 함수(function)
- 읽기 쉬고 어떤 동작인지 알 수 있게 네이밍
- `showError` : 에러를 보여줌
- `getName` : 이름을 얻어옴
- `createUserData` : 유저데이터 생성

```
function 함수 sayHello 함수명 (매개변수) {
  console.log('Hello, ${name}');
}
sayHello('Mike');
```
- 주의: 함수 내 지역변수는 외부에서 사용할 수 없다.
- 전역과 지역은 서로 간섭받지 않는다.
```
function sayHello(name = 'friend') { // default 값 주기
  let msg = 'Hello ${name}'
  console.log(msg)
}

sayHello();
sayHello('Jane');
```

### 11. 함수 표현식, 화살표 함수(arrow function)
함수 선언문 vs 함수 표현식
- 호출할 수 있는 타이밍이 다름
- 함수 선언문 : 어디서든 호출 가능
  호이스팅(hoistion) : JavaScript의 실행 전 초기화 상태에서 코드의 모든 함수 선언문을 찾아서 생성해준다. 
- 함수 표현식 : JavaScript가 한줄씩 실행하고 해당 코드에 도달해야만 실행된다. 
```
// 함수 표현식
let sayHello = function() {
  console.log('Hello');
}
```
**화살표 함수**
- return 문이 한줄이면 일반괄호 사용가능
```
let add = function(num1, num2) {
  return num1 + num2;
}
```
```
let add = (num1, num2) => {
  return num1 + num2;
}
let add = (num1, num2) => num1 + num2;
let sayHello = name => 'Hello, ${name}'; // 인수가 하나
let showError = () => { // 인수가 없는 경우
  alert('error!');
}
```

### 12. Object
![Js_Object](https://github.com/AnYeHyeon/img/blob/main/Js_object.png?raw=true)   
- Object 접근, 추가, 삭제
```
const superman = {
  name : 'clark',
  age : 33,
}
```
```
// 접근
superman.name
superman['age']

// 추가
superman.gender = 'male';
superman['hairColor'] = 'black';

// 삭제
delete superman.hairColor;
```
- Object 단축 프로퍼티
```
const name = 'clark';
const age = 33;

const superman = {
  name : name, => name;
  age : age,  => age;
  gender : 'male',
}
```
- Object 프로퍼티 존재 여부 확인
```
'birthDay' in superman;
'age' in superman;
```

### 13. for ... in 반복문
```
const superman = {
  name : 'Mike',
  age : 30,
}

for(key in Mike) {
  console.log(Mike[key])
}
```

### 14. Object Method와 this
- method : 객체프로퍼티로 할당된 함수
- 자신만의 this를 가질 수 있음
- 화살표 함수는 일반 함수와는 달리 자신만의 this를 가질 수 없으며, 화살표 함수 내부에서 this를 사용하면, 그 this는 외부에서 값을 가져온다.
```
const user = {
  name : 'Mike',
  sayHello : function() {
    console.log('Hello, I'm ${this.name}');
  }
}
```
```
let boy = {
  name : 'Mike',
  sayHello,
  }
let girl = {
  name : 'Jane',
  sayHello,
  }

sayHello : function(){
  console.log('Hello, I'm ${this.name}');
}
```

### 15. 배열
```
let students = ['Mike', 'Jane', 'Anne'];
console.log(student[0]);

student.length
student.push // 요소 추가
student.pop()  // 배열 끝 요소 제거
student.shift, unshift  // 배열 앞에 제거/추가
```
```
let days = ['월', '화', '수'];

for (let index = 0; index < days.lenth; index++) {
  console.log(days[index])
}

for (let day of days) {
  console.log(day)
}
```

## Contents 2. Jquery
- 라이브러리 : 자주 사용하는 코드들을 재사용할 수 있는 형태로 가공해서 프로그래밍 효율을 높여주는 코드들
- Jquery?
  1. 엘리먼트를 선택하는 강력한 방법과
  2. 선택된 엘리먼트들을 효율적으로 제어할 수 있는 다양한 수단을 제공하는
  3. 자바스크립트 라이브러리
  -> for문과 같이 JavaScript로 길게 짜야하는 코드를 간단하게 만들어 줄 수 있음.
  
```
// 주어       서술어
$(제어대상).method1().method2();
```

### 레퍼(wrapper)
- **jQuery(**엘리먼트 오브젝트 | 'CSS스타일 선택자'**)**
```
<script type="text/javascript">
//$ 대신 jQuery를 사용
jQuery('body').html('hello world');
</script>
```
```
<script type="text/javascript">
//$를 함수의 지역변수로 선언해서 외부에 있을지 모르는 타 라이브러리의 $와의 충돌을 예방
(function($){
    $('body').html('hello world');
})(jQuery)  // 함수를 정의하는 동시에 호출
</script>
```
- 제어대상을 지정하는 방법
  - jQuery(selector, [context])
  - jQuery(element)
```
<html>
    <body>
        <ul>
            <li>test2</li>
        </ul>
        <ul class="foo">
            <li>test</li>
        </ul>
        <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>
        <script type="text/javascript">
            (function($){            
                $('ul.foo').click( function() {  // event 호출
                    $('li', this).css('background-color','red'); // this: ul.foo
                });
            })(jQuery)
        </script>
    </body>
</html>
```





















## Checklist
* 자바스크립트는 버전별로 어떻게 변화하고 발전해 왔을까요?   
:  2008, 7 ECMAScript 6 -> 10. 각 브라우저별로 다른 표현을 통합하는 프로젝트를 시행.
  * 자바스크립트의 버전들을 가리키는 ES5, ES6, ES2016, ES2017 등은 무엇을 이야기할까요?    
  : ECMAScript는 자바스크립트의 표준화된 버전을 말하며, ECMA International에서 정의하고 유지보수 한다. 대체로 버전 5,6 에서 대대적인 변화가 일어났으며, 특히 6에서는 새로운 기능과 문법, 확장된 표준 라이브러리 등이 포함되어 있다. 이 버전에서는 let 및 const 키워드를 사용한 블록 스코프 변수 선언, 화살표 함수, 클래스, 모듈 등과 같은 많은 기능이 도입되었다.
  * 자바스크립트의 표준은 어떻게 제정될까요?   
  : ECMA International이라는 국제 표준화 기구에 의해 관리되며, 제안, 초안, 후보, 표준 단계를 거쳐 제정된다. ECMAScript의 표준은 개발자 커뮤니티와 산업의 요구, 기술적인 적용 가능성 등을 고려하여 결정된다. TC39 위원회는 이러한 다양한 요소를 고려하여 표준을 개발하며, 개발자들은 이를 참고하여 현대적인 자바스크립트 코드를 작성하고 브러우저나 다른 환경에서 호환성을 유지할 수 있다.
* 자바스크립트의 문법은 다른 언어들과 비교해 어떤 특징이 있을까요?
:
  * 자바스크립트에서 반복문을 돌리는 방법은 어떤 것들이 있을까요?
* 자바스크립트를 통해 DOM 객체에 CSS Class를 주거나 없애려면 어떻게 해야 하나요?
  * IE9나 그 이전의 옛날 브라우저들에서는 어떻게 해야 하나요?
* 자바스크립트의 변수가 유효한 범위는 어떻게 결정되나요?
  * `var`과 `let`으로 변수를 정의하는 방법들은 어떻게 다르게 동작하나요?
* 자바스크립트의 익명 함수는 무엇인가요?
  * 자바스크립트의 Arrow function은 무엇일까요?

## Quest
* (Quest 03-1) 초보 프로그래머의 영원한 친구, 별찍기 프로그램입니다.
  * [이 그림](jsStars.png)과 같이, 입력한 숫자만큼 삼각형 모양으로 콘솔에 별을 그리는 퀘스트 입니다.
    * 줄 수를 입력받고 그 줄 수만큼 별을 그리면 됩니다. 위의 그림은 5를 입력받았을 때의 결과입니다.
  * `if`와 `for`와 `function`을 다양하게 써서 프로그래밍 하면 더 좋은 코드가 나올 수 있을까요?
  * 입력은 `prompt()` 함수를 통해 받을 수 있습니다.
  * 출력은 `console.log()` 함수를 통해 할 수 있습니다.

```
number = prompt('숫자를 입력해주세요.');
jsStars(number);

function jsStars (number) {
    for(let i = 1, j = 0; i<=number-1; i++){
        console.log(" ".repeat(number-1-i) + "*".repeat(i + j));
        j++;
    }
}
```

* (Quest 03-2) skeleton 디렉토리에 주어진 HTML을 조작하는 스크립트를 완성해 보세요.
  * 첫째 줄에 있는 사각형의 박스들을 클릭할 때마다 배경색이 노란색↔흰색으로 토글되어야 합니다.
  * 둘째 줄에 있는 사각형의 박스들을 클릭할 때마다 `enabled`라는 이름의 CSS Class가 클릭된 DOM 노드에 추가되거나 제거되어야 합니다.
* 구현에는 여러 가지 방법이 있으나, 다른 곳은 건드리지 않고 TODO 부분만 고치는 방향으로 하시는 것을 권장해 드립니다.

## Advanced
* Quest 03-1의 코드를 더 구조화하고, 중복을 제거하고, 각각의 코드 블록이 한 가지 일을 전문적으로 잘하게 하려면 어떻게 해야 할까요?
* Quest 03-2의 스켈레톤 코드에서 `let` 대신 `var`로 바뀐다면 어떤 식으로 구현할 수 있을까요?
