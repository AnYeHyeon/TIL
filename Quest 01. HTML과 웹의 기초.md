# Week 1 : Github + Coding Environment, HTML, CSS
# Quest 01. HTML과 웹의 기초
## Introduction
---
HTML은 HyperText Markup Language의 약자로, 웹 브라우저에 내용을 표시하기 위한 가장 기본적인 언어입니다. 이번 퀘스트를 통해 HTML에 관한 기초적인 사항들을 알아볼 예정입니다.   
- HTML: HyperText Markup Language   

## Contents
### <태그 속성>
- 링크걸기: `<a href='link'>도널드 커누스</a>`
- 새로운 탭에서 열기 링크 뒤에 `target=_blank` 추가해주기
- 미리보기 title="설명"
- `<li>` : 항목 표시
- `<ul>` : 그룹핑
- `<ol>` : 순서가 있는 항목
- `<h1>` : 제목 양식
- `<meta charset-"utf-8">` : 글자 깨질 때
- `<head>` : 부가적인 정보, html 문서에 대한 설명, **meta data**
- `<body>` : 본문
- `<html>` : 전체를 감싸주기
- `<!DOCTYPE html>` : html의 버전을 알려줌
- `<br>` : 강제로 줄바꿈 (boid element)
- `<p>` : 단락 -> CSS로 간격을 조절해 줄 수 있다
- `<div>` : 웹페이지를 꾸며줄대 그룹핑 해주는 태그. 줄 바꿈이 된다.
- ++`<span>` : div와 같이 특별한 기능을 갖고있지는 않는다. 줄 바꿈이 되지 않는다.
- `<img>` : 이미지 `<img src="img.jpg" width="200" height="300" alt="산 이미지" title="산 이미지">`
- `<table>` : 표
- `<form action="">` 
- `<input type="text" name="id" value="default value">` : 사용자로부터 text를 입력받음
- `<textares 속성은 에디터가 추천>` : 테스트를 입력할 수 있는 박스가 나옴. 태그 사이에 기본 값을 넣을 수 있다.
- `<select> <option>` : dropdown list 콤보박스


```
<!DOCTYPE html>
<html>
<head>
    <title>HTML - 수업소개</title>
    <meta charset-"utf-8">
</head>
<body>
<h1>HTML</h1>
<ol>
<li>기술소개</li>
<li>기본문법</li>
<li>하이퍼텍스트와 속성</li>
<li>리스트와 태그의 중첩</li>
</ol>

<h2>선행학습</h2>
선행학습 내용은 다음과 같습니다.
</body>
</html>
```



## Checklist
---
- HTML 표준의 역사는 어떻게 될까요?   
: GML -> SGML -> SGMLguid -> HTML   
1.0 부터 현재의 HTML5까지 발전해옴. HTML5는 다양한 기능과 API를 제공하며, 반응형 웹 디자인과 모바일 기기 지원 등을 강조하고 있다. 

- HTML 표준을 지키는 것은 왜 중요할까요?   
웹 페이지가 다양한 브라우저와 기기에서 일관되고 올바르게 표시될 수 있다는 점이다. 또한 향후 HTML의 버전 업데이트와 호환성을 유지할 수 있다. 

- XHTML 2.0은 왜 세상에 나오지 못하게 되었을까요?   
복잡성과 엄격한 문법: 호환성없이 완전히 새로운 규칙과 문법을 도입했기에 기존 HTML로 이루어진 웹 페이지나 애플리케이션들이 전환되기 어려웠다.

- HTML5 표준은 어떤 과정을 통해 정해질까요?     
작업 초안(WHATWG + W3C)-> 작업 진행 -> 후보 추천 -> 추천 후보 -> 표준화 및 유지 관리

- 브라우저의 역사는 어떻게 될까요?
Mosaic -> Netscape Navigator -> Internet Explorer -> Mosilla Firefox -> Google Chrome, Safari, Opera, Microsoft Edge

- Internet Explorer가 브라우저 시장을 독점하면서 어떤 문제가 일어났고, 이 문제는 어떻게 해결되었을까요?
1. 웹 표준 준수: 표준에 따르지 않는 독자적인 기능과 구현을 갖추고 있었다. -> 호환성 문제를 야기, 다른 브라우저에서 잘 작동되지 않음
2. IE6의 오래된 버전 유지
해결: 웹 표준 중요성 인식, 브라우저 다양화에 따른 경쟁력 강화를 위한 기술혁신, IE6 지원 중단 및 현대적인 표준을 따른 웹 개발

- 현재 시점에 브라우저별 점유율은 어떻게 될까요? 
2023년 6월 기준, Chrome 61.92%, Safari 25.09%, Edge 5.28, Firefox 2.45%, Samsung Internet 2.43, Other 2.84%

- 이 브라우저별 점유율을 알아보는 것은 왜 중요할까요?
웹 사이트, 웹 애플리케이션을 개발할 때, 다양한 브라우저를 고려해야하므로 점유율을 분석하여 가장 우선적으로 사용되는 브라우저들을 우선적으로 지원할 수 있다. 또한 점유율이 높은 브라우저들은 표준을 준수하고 최신기술과 개선 사항을 빠르게 채택하는 경향이 있다. 따라서 개발자들을 더 현대적이고 효율적인 기술을 사용할 수 있다.

- 브라우저 엔진(렌더링 엔진)이란 무엇일까요? 
브라우저 엔진(랜더링 엔진)은 웹 페이지의 HTML, CSS 및 JavaScript 등의 코드를 해석하고, 해당 내용을 브러우저 창에 표시하는 소프트웨어 컴포넌트이다. 브러우저 엔진은 웹 브라우저의 핵심 기능을 담당하며, 웹 페이지의 렌더링, 인터페이스의 구성, 데이터의 로딩, 자바스크립트의 실행 등을 처리한다.

- 어떤 브라우저들이 어떤 엔진을 쓸까요?
    - Blink (Google Chrome, Microsoft Edge)
    - WebKit (Apple Safari)
    - Gecko (Mozilla Firefox)
    - Trident (Internet Explorer의 이전 버전)

- 모바일 시대 이후, 최근에 출시된 브라우저들은 어떤 특징을 가지고 있을까요?
1. 모바일 최적화
2. 성능 개선
3. 보안 강화
4. 웹 표준 준수
5. 개발자 도구와 확장 기능

- HTML 문서는 어떤 구조로 이루어져 있나요?
주요 태그에 대한 설명은 상단에 있음. HTML 문서의 구조는 트리 형태로 이루어져 있으며, 태그들은 중첩 관계를 가지며 계층 구조로 구성된다. 시작 태그와 종료 태그로 구성되며, 시작 태그와 종료 태그 사이에 콘텐츠가 위치할 수 있다. 또한, 태그에는 속성(attribute)을 사용하여 추가 정보를 전달할 수 있다. 

  - `<head>`에 자주 들어가는 엘리먼트들은 어떤 것이 있고, 어떤 역할을 할까요?
    - <meta> : 메타 데이터를 정의, 문자 인코딩
    - <title> : 웹 페이지 제목 정의
    - <link> : 외부 스타일 시트(CSS) 파일이나 파비콘 등을 연결하는 엘리먼트
    - <style> : HTML 문서 내에 직접 CSS 스타일을 정의하는 엘리먼트
    - <script> : JavaScript 파일을 로드하는 엘리먼트
    - <base> : 문서 내에서 상대적인 URL 경로를 해석할 때 사용할 기준 URL을 설정한다.
    - <noscript> : JavaScript가 비활성화 되었을 때 대체 콘텐츠를 제공한다.
    - <meta http-equiv="refresh"> : 일정 시간이 지난 후에 페이지를 자동으로 새로고침한다.

  - 시맨틱 태그는 무엇일까요?
  의미론적인. HTML5에서 도입된 태그로, 웹 페이지의 구조와 의미를 명확하게 전달하는 역할을 한다.
    - 시맨틱 엘리먼트를 사용하면 어떤 점이 좋을까요?
    각각의 태그는 그 자체로 특정한 의미를 가지며, 콘텐츠의 의도와 의미를 개발자와 검색 엔진에 전달한다. 이는 검색 엔진 최적화(SEO)에 도움이 되고, 검색 결과에서의 가시성을 향상시킬 수 있다.
    - `<section>`과 `<div>, <header>, <footer>, <article>` 엘리먼트의 차이점은 무엇인가요?
        - `<section>` : 역할이 분명하지 않음.독립적인 구획, 주제나 콘텐츠의 그룹을 의미적으로 구분한다.
        - `<div>` : 문서의 구획을 나눌 때 사용되며, 아무런 의미를 가지고 있지 않은 일반적인 컨테이너이다. 의미부여가 아니라 레이아웃 요소로 주로 사용된다.
        - `<header>` : 웹 페이지나 섹션의 헤더(머리말)를 나타낸다. 상단에 위치하며 웹 페이지의 제목, 로고, 네비게이션 메뉴 등의 콘텐츠를 포함한다.
        - `<footer>` : 웹 페이지나 섹션의 푸터(바닥글)를 나타낸다. 주로 저작권 정보, 연락처 정보, 관련 링크 등의 푸터 콘텐츠를 포함한다.
        - `<article>` : 본문. 블로그 글, 뉴스 기사, 포험 게시물 등과 같이 독립적으로 구성되거나 재사용 가능한 콘텐츠를 그룹화한다.
        - 추가 `<nav>` : 어떤 것이 웹 페이지를 탐색할 때 사용하는 네비게이션인지 의미를 부여.
  - 블록 레벨 엘리먼트와 인라인 엘리먼트는 어떤 차이가 있을까요?
    HTML 요소의 특성과 렌더링 방식에 대한 차이가 있다.
    - 블록 레벨 엘리먼트 : 새로운 블록을 형성하여 콘텐츠를 묶는 데 사용된다.
        - 한 줄을 전부 처지하며, 가로 폭을 사용 가능한 최대로 늘린다.
        - 예시) `<div>, <p>, <h1>~<h6>, <section>, <article>, <footer>`
        - 기본적으로 새로운 줄에서 시작하고 종료된다. 따라서 자동으로 줄 바꿈이 적용된다.
        - 다른 블록 레벨 엘리먼트와 인라인 엘리먼트를 포함할 수 있다.

    - 인라인 엘리먼트: 문장이나 텍스트의 일부를 감싸는 데 사용된다.
        - 문장 내에서 콘텐츠를 표현하며, 가로 폭을 필요한 만큼만 차지한다. 
        - 예시) `<span>, <a>, <strong>, <em>, <img>`
        - 문장 내에서 표현되기 때문에 자동으로 줄 바꿈이 일어나지 않는다.
        - 다른 인라인 엘리먼트를 포함할 수 있지만, 블록 레벨 엘리먼트를 직접 포함할 수는 없다.

<!--ex-->
![HTML Block and Inline Elements](https://github.com/AnYeHyeon/img/blob/main/html%20block%20level%20inline%20elements.jpg)   

[HTML Block and Inline Elements](https://parkminseob.github.io/html/css/htmlCss-08/)

## Quest
---
![html skeleton](https://github.com/AnYeHyeon/img/blob/main/html%20skeleton.png)   
### 과제 코드
[quest1 html code](https://github.com/AnYeHyeon/2023-SME-SW-Bootcamp/blob/main/Yehyeon/Quest01_skeleton.html)