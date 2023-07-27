# Week 3 : Clone Coding (Bootstrap)
# Quest 04. OOP의 기본

## Introduction
* 이번 퀘스트에서는 바닐라 자바스크립트의 객체지향 프로그래밍에 대해 알아볼 예정입니다.

## Topics
* 객체지향 프로그래밍
  * 프로토타입 기반 객체지향 프로그래밍
  * 자바스크립트 클래스
    * 생성자
    * 멤버 함수
    * 멤버 변수
  * 정보의 은폐
  * 다형성
* 코드의 재사용

## Contents 1 : Bootsrap
### CDN (Content Delivery Network)
: 남이 만들은거 가져다쓰기
- 한줄의 크기를 12로 본다.
- ```class="col-lg-3 col-md-6``` 한 페이지에 콘텐츠를 어떤 사이즈로 보여줄지.


## Contents 2 : Python crawling
```
# 기사 웹 크롤링하기


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://news.naver.com/")

bsObject = BeautifulSoup(html, "html.parser")  

for link in bsObject.fineall('a'):  # 기사의 링크를 가져옴
    print(link.text.strip(), link.get('href'))
```

## Contents 3 : API





## Resources
* [MDN - Classes](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Classes)
* [MDN - Inheritance and the prototype chain](https://developer.mozilla.org/ko/docs/Web/JavaScript/Inheritance_and_the_prototype_chain)
* [MDN - Inheritance](https://developer.mozilla.org/ko/docs/Learn/JavaScript/Objects/Inheritance)
* [Polymorphism](https://medium.com/@viktor.kukurba/object-oriented-programming-in-javascript-3-polymorphism-fb564c9f1ce8)
* [Class Composition](https://alligator.io/js/class-composition/)
* [Inheritance vs Composition](https://woowacourse.github.io/javable/post/2020-05-18-inheritance-vs-composition/)

## Checklist
* 객체지향 프로그래밍은 무엇일까요?
: 현실 세계의 객체와 그 객체들 간의 상호작용에 초점을 둔 프로그래밍 방법론이다. 객체는 데이터와 이 데이터를 처리하는 메서드를 묶어놓은 개념적인 단위로 이해할 수 있다.
  
  * `#`로 시작하는 프라이빗 필드는 왜 필요한 것일까요? 정보를 은폐(encapsulation)하면 어떤 장점이 있을까요?
  : '#'로 시작하는 프라이빗 필드는 객체지향 프로그래밍에서 정보 은폐를 위해 사용되는 개념이다. 정보 은폐란, 객체의 내부 상태를 외부에서 직접 접근하지 못하도록 보호하고, 객체의 메서드를 통해서만 접근할 수 있도록 하는 것을 의미한다. 이를 통해 객체의 내부 구현 세부사항을 외부로부터 숨기고, 인터페이스를 통해서만 상호작용할 수 있도록 한다.
  
  * 다형성이란 무엇인가요? 다형성은 어떻게 코드 구조의 정리를 도와주나요?
  : 같은 이름의 메서드를 서로 다른 객체에서 다르게 동작하도록 하는 개념이다. 다형성은 하나의 인터페이스나 추상 클래스를 통해 여러 객체들을 일관성 있게 다룰 수 있도록 해주는 메커니즘이다.
    - 두 가지 주요 방법으로 다형성을 구현할 수 있다.   
    1. 상속과 메서드 오버라이딩 : 부모 클래스가 가지고 있는 메서드를 자식 클래스에서 재정의하는 것. 
    2. 인터페이스와 다형성: 인터페이스는 일종의 계약으로, 특정 메서드들의 원형을 정의한다. 클래스가 인터페이스를 구현하면, 인터페이스에서 정의한 메서드들을 반드시 구현해야한다.
    - 다형성은 다음과 같은 코드 구조의 정리를 도와준다.   
    1. 유연성과 확장성 : 새로운 클래스를 추가해도 기존 코드의 수정 없이 사용할 수 있다.
    2. 가독성 : 동일한 인터페이스를 구현하는 다양한 클래스들을 인터페이스 타입으로 다루므로, 코드가 더 간결하고 가독성이 좋아진다.
    3. 재사용성
    4. 유지보수성 : 기능 추가나 변경 시에 인터페이스나 부모 클래스를 수정하면 된다.

  * 상속이란 무엇인가요? 상속을 할 때의 장점과 단점은 무엇인가요?
  : 객체지향 프로그래밍에서 클래스 간에 공통된 특성과 동작을 물려주는 관계를 말한다. 하나의 클래스(부모 또는 상위 클래스)가 가지고 있는 특성과 동작을 다른 클래스(자식 또는 하위 클래스)가 물려받아 사용할 수 있게 된다.   
  
  **장점:**
1. 코드 재사용성: 부모 클래스에서 정의한 기능들을 자식 클래스가 물려받아 사용할 수 있기 때문에, 중복 코드를 피하고 코드의 재사용성을 높일 수 있다. 공통적인 기능은 한 곳에서 정의하고 유지보수할 수 있으며, 이로 인해 개발 생산성이 향상된다.

2. 유지보수성: 부모 클래스에서 수정된 기능은 자식 클래스들에게 자동으로 반영되므로, 코드를 변경할 때 발생할 수 있는 버그와 오류를 줄여준다.

3. 일관성과 가독성: 상속을 통해 클래스 간에 계층 구조가 만들어지므로, 유사한 클래스들을 일관성 있게 다룰 수 있다. 이로 인해 코드의 가독성이 향상된다.

4. 다형성 지원: 상속을 통해 다형성을 구현할 수 있다. 즉, 부모 클래스 타입으로 선언된 변수를 통해 여러 자식 클래스 객체들을 다룰 수 있게 된다.

**단점:**

1. 클래스 간의 강한 결합: 상속은 클래스 간에 강한 결합을 만들어내기 때문에, 부모 클래스의 변경이 자식 클래스들에게 영향을 미칠 수 있다. 이로 인해 코드를 수정하거나 확장하기 어려울 수 있다.

2. 상속의 오용: 상속은 클래스 간의 관계를 명확하게 설계해야 하며, 클래스 간의 "is-a" 관계가 아닌 경우 상속을 사용하는 것은 적절하지 않을 수 있다. 이러한 오용은 코드의 복잡성을 증가시킬 수 있다.
  
  * OOP의 합성(Composition)이란 무엇인가요? 합성이 상속에 비해 가지는 장점은 무엇일까요?
  : 객체지향 프로그래밍의 설계 원칙 중 하나로, 클래스가 다른 클래스의 객체를 포함하여 기능을 구현하는 방법이다. 즉, 한 클래스가 다른 클래스의 객체를 맴버 변수로 가지는 것을 의미한다. 합성은 "has-a"관계로 표현된다.

  **장점**
  - 다중 상속의 문제 회피: 합성은 다중 상속으로 인해 발생하는 문제를 회피할 수 있다. 다중 상속은 코드를 복잡하게 만들 수 있고, 충돌 문제를 일으킬 수 있다.

* 자바스크립트의 클래스는 어떻게 정의할까요?
1. 클래스 선언문
```
class MyClass {
  // 클래스 멤버(속성과 메서드) 정의
  constructor() {
    // 생성자 메서드
    // 객체가 생성될 때 실행되는 메서드
  }

  method1() {
    // 메서드1
  }

  method2() {
    // 메서드2
  }

  // ... 추가적인 멤버들 정의 가능
}
```
2. 클래스 표현식
```
const MyClass = class {
  constructor() {
    // 생성자 메서드
  }

  method1() {
    // 메서드1
  }

  method2() {
    // 메서드2
  }

  // ... 추가적인 멤버들 정의 가능
};
```

  * 프로토타입 기반의 객체지향 프로그래밍은 무엇일까요?
: Prototype-based Object-Oriented Programming은 객체지향 프로그래밍의 한 접근 방식으로, 클래스가 없고 프로토타입이라는 객체를 기반으로 객체를 생성하고 상속하는 개념이다. 이러한 방식은 자바스크립트와 같은 스크립트 언어에서 주로 사용되며, 객체들 간의 상속과 프로퍼티 공유를 프로토타입 체인을 통해 구현한다.   
  - 프로토타입 기반의 객체지향 프로그래밍에서 객체는 다른 객체를 기반으로 생성되며, 기반 객체를 프로토타입이라고 한다. 이러한 프로토타입 객체는 속성들의 집합으로 이루어져 있다. 객체를 생성할 때, 해당 객체의 프로토타입을 가리키는 내부 링크를 생성한다. 이 링크를 통해 해당 객체에서 프로토타입의 속성을 찾지 못하면, 자동으로 프로토타입 체인을 따라 상위 프로토타입으로 이동하여 속성을 찾는다.
```
# 리터럴 표기법
const obj = {
  property1: value1,
  property2: value2,
  // ...
};

# 생성자 함수
function MyClass() {
  this.property1 = value1;
  this.property2 = value2;
  // ...
}

const obj = new MyClass();

# Object.create() 메서드
const protoObj = {
  property1: value1,
  property2: value2,
  // ...
};

const obj = Object.create(protoObj);
```


  * 자바스크립트의 클래스는 이전의 프로토타입 기반의 객체지향 구현과 어떤 관계를 가지고 있나요?
: 자바 스크립트의 클래스는 이전의 프로토타입 기반의 객체지향 구현과 밀접한 관계가 있다. ES6에서 도입된 클래스 선언문은 사실 프로토타입 기반의 객체지향 프로그래밍을 구현하기 위한 문법적인 설탕(syntactic sugar)으로 볼 수 있다.   
ES6부터 클래스 선언문을 사용하여 클래스를 더 직관적이고 가독성 있게 정의할 수 있게 되었다. 
```
// 클래스 선언문을 이용한 클래스 구현
class MyClass {
  constructor(value) {
    this.property = value;
  }

MyClass.prototype.method = function() {
  // 생성자 함수를 이용한 클래스 구현
};

  method() {
    // 메서드 구현
  }
}

const obj = new MyClass(42);

```

## Quest
* 웹 상에서 동작하는 간단한 바탕화면 시스템을 만들 예정입니다.
* 요구사항은 다음과 같습니다:
  * 아이콘은 폴더와 일반 아이콘, 두 가지의 종류가 있습니다.
  * 아이콘들을 드래그를 통해 움직일 수 있어야 합니다.
  * 폴더 아이콘은 더블클릭하면 해당 폴더가 창으로 열리며, 열린 폴더의 창 역시 드래그를 통해 움직일 수 있어야 합니다.
  * 바탕화면의 생성자를 통해 처음에 생겨날 아이콘과 폴더의 개수를 받을 수 있습니다.
  * 여러 개의 바탕화면을 각각 다른 DOM 엘리먼트에서 동시에 운영할 수 있습니다.
  * Drag & Drop API를 사용하지 말고, 실제 마우스 이벤트(mouseover, mousedown, mouseout 등)를 사용하여 구현해 보세요!

## Advanced
* 객체지향의 역사는 어떻게 될까요?
* Smalltalk, Java, Go, Kotlin 등의 언어들로 넘어오면서 객체지향 패러다임 측면에서 어떤 발전이 있었을까요?
