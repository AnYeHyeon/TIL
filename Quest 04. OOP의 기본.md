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
    3. 재사용성 : 

  * 상속이란 무엇인가요? 상속을 할 때의 장점과 단점은 무엇인가요?
  : 
  
  * OOP의 합성(Composition)이란 무엇인가요? 합성이 상속에 비해 가지는 장점은 무엇일까요?

* 자바스크립트의 클래스는 어떻게 정의할까요?
  * 프로토타입 기반의 객체지향 프로그래밍은 무엇일까요?
  * 자바스크립트의 클래스는 이전의 프로토타입 기반의 객체지향 구현과 어떤 관계를 가지고 있나요?

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
