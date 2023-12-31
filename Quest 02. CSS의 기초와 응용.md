# Week 1 : Github + Coding Environment, HTML, CSS
# Quest 02. CSS의 기초와 응용
## Contents
### **CSS란?**
Cascading Styel Sheet: 위에서 연속적으로 떨어지며 디자인 양식을 물어봄
Author style(CSS) -> User style(사용자 지정) -> Browser(html)
- ! important: 나쁜 아키텍쳐이므로 되도록 쓰지말것

### **6가지 선택자**

- selectors
```
selector{
  property: value;
}
```

  - Universal `*` : 모든 태그를 고름
```
{
  color: green;
}
```

  - type `Tag` : 특정 태그를 고름
  ```
li {
  color: blue;
}  ## 태그 가까이에 설정하면 우선순위가 높아짐
  ```

  - ID `#id` : 해당 ID만 고름
  ```
  #special {  # 앞에 태그를 붙여주면 해당 태그만 적용됨
    color: pink;  # id가 special 인 것만 핑크색으로 바뀜
  ```
  - Class `.class`
  ```
.red {
  width: 100px;
  height: 100px;
  padding: 20px 20px 20px 20px;  # 컨텐츠 안에 들어가는 space
  border: 2px dashed red;
  margin: 20px; # 컨탠츠 밖에 들어가는 space
  background: yellow;  # div의 컨테이너를 꾸며줌
}
  ```

  - State `:` 
```
button:hover {
  color: red;
  background: beige;
}
a[href="naver.com"] {
  color: purple;
}
```

  - Attribute `[]`

### **Position**
```
div {
  width:
  height:
  margin-botton:
  background:
}

.container {
  background:
  left:
  top:
  position: relative; /*해줘야 전체 div의 위치가 이동됨. */
}

.box {
  background:
  left:
  top:
  position: relative;  /* 박스의 개체가 옮겨감, absolute : 컨테이너에서(상자안에서) 움직임, fixed: 윈도우 페이지 안에서 움직임. sticky : 스크롤해도 없어지지 않음.*/
}
```

### **Flexbox**
### 1. container, item에 속성값이 존재   
- container
  - display
  - flex-direction: (row(-reverse), column(-reverse))
  - flex-wrap: (nowrap, wrap 자동으로 내려감, reverse 가능)
  - flex-flow 위에 두 가지 합한거
  - justify-content: 아이템배치 (flex-start, flex-end, center, space-around, space-evenly, space-betwwn)
  - align-tiems: 반대축!!
  - align-content
  <br> 
  <br> 
- item 
  - order: 아이템별로 순서를 정할 수 있다. 잘쓰지는 않음
  - flex-grow: 컨테이너를 채우려고 함.
  - flex-shrink: 컨테이너 사이즈 변경시, 줄어드는 정도
  - flex : `flex-basis: auto;`
  - align-self : 아이템별로 위치 선정

### 2. 중심축과 반대축이 있다.
- main axis ->
- cross axis v

### 색상 HEX 값을 알려주는 사이트
[COLOR TOOL](https://www.google.com/search?q=color+tool&oq=color+tool&aqs=chrome..69i57.3937j0j7&sourceid=chrome&ie=UTF-8)



























## Checklist
- CSS를 HTML에 적용하는 세 가지 방법은 무엇일까요?
  - 세 가지 방법 각각의 장단점은 무엇일까요?
- CSS 규칙의 우선순위는 어떻게 결정될까요?
- CSS의 박스모델은 무엇일까요? 박스가 화면에서 차지하는 크기는 어떻게 결정될까요?
- float 속성은 왜 좋지 않을까요?
- Flexbox(Flexible box)와 CSS Grid의 차이와 장단점은 무엇일까요?
- CSS의 비슷한 요소들을 어떤 식으로 정리할 수 있을까요?

## Quest
- Quest 01에서 만들었던 HTML을 바탕으로, 네이버 모바일 그림의 레이아웃과 CSS를 최대한 비슷하게 흉내내 보세요. 꼭 완벽히 정확할 필요는 없으나 align 등의 속성은 일치해야 합니다.
- 주의사항: 되도록이면 원래 페이지의 CSS를 참고하지 말고 아무것도 없는 백지에서 시작해 보도록 노력해 보세요!   



  - 시간이 없는 관계로 일단 여기까지.   
     
![Quest2](https://github.com/AnYeHyeon/img/blob/main/20230713_041039_2.png?raw=true)

## Advenced
- 왜 CSS는 어려울까요?
- CSS의 어려움을 극복하기 위해 어떤 방법들이 제시되고 나왔을까요?
- CSS가 브라우저에 의해 해석되고 적용되기까지 내부적으로 어떤 과정을 거칠까요?
- 웹 폰트의 경우에는 브라우저 엔진 별로 어떤 과정을 통해 렌더링 될까요?