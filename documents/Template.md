# Template

## if-else in Template.

아래의 코드를 통해서 `if-else`를 사용할 수 있다.

```django
{% if SOMETHING %}
<!-- Do something.. -->
{% elif SOMETHING_ELSE %}
<!-- Do another thing -->
{% else %}
<!-- Do another thing!! -->
{% endif %}
```

## Text

### 글자 수 제한

`truncatewords` 혹은 `truncatechars`를 사용해서 문자열 크기를 제한할 수 있다.

```django
<!-- truncatewords: 와 숫자 사이에 공백이 있으면 안됨! -->

<!-- 문자열을 단어 수 기준으로 자름 -->
{{ p.content | truncatewords:45 }}

<!-- 문자열을 글자 수 기준으로 자름 -->
{{ p.content | truncatechars:45 }}
```

## Value

### 값이 존재하는지 확인

`dictionary`에 값이 존재하는지 확인을 할 수 있다.

```python
dic.exists
```

이를 `template`에 적용시킬 수 있다.

#### 예제

```django
{% if post_list.exists %}
<!-- Do something.. -->
{% endif %}
```
