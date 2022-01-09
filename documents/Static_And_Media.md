## Static File.

### 정적 파일 관리하기

정적인 파일을 추가하기 위해서는 `html` 파일 `<!DOCTYPE html>` 아래 해당 라인을 추가해야 한다.

```html
<!DOCTYPE html> {% load static %}
```

### 정적 파일 추가하기

그 이후에 파일을 불러올 때는 `{% static VALUE %}`을 이용하여 정적인 파일을 가져올 수 있다.

```html
<link rel="stylesheet" href="{% static 'blog/bootstrap/bootstrap.min.css' %}" />
```
