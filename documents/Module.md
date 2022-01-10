# Module

## Block and extends.

블럭을 지정하여 `template`을 모듈화할 수 있다.

```django
{% block main_area %}

{% endblock %}
```

모듈화 시킬 `html`에 블록을 지정한다.

그리고 사용할 블럭에서도 똑같이 적용을 하되, 최상단에 모듈을 `extend`하는 것을 명시해야 한다.

```django
{% extends 'MODULE' %}

{% block main_area %}
<!-- Your codes here... -->
{% endblock %}
```

## include

코드를 바로 읽어올 때는 `include`를 사용해서 얻어올 수 있음.

```django
{% include 'blog/navbar.html' %}
```
