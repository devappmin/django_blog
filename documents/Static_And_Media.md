## Static File.

### 정적 파일 관리하기

정적인 파일을 추가하기 위해서는 `html` 파일 `<!DOCTYPE html>` 아래 해당 라인을 추가해야 한다.

```html
<!DOCTYPE html>

{% load static %}
```

### 정적 파일 추가하기

그 이후에 파일을 불러올 때는 `{% static VALUE %}`을 이용하여 정적인 파일을 가져올 수 있다.

```html
<link rel="stylesheet" href="{% static 'blog/bootstrap/bootstrap.min.css' %}" />
```

## Media File.

### Setting에서 Media url 지정하기

`settings.py`에서 해당 코드를 입력하여 미디어가 저장될 위치를 지정해야 한다.

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '_media')
```

### models에 이미지 필드 추가

```python
img = models.ImageField(upload_to='PATH', blank=True)
```

`upload_to`는 이미지가 저장될 위치를 지정하는 것이고, blank는 값이 필수로 들어가지 않아도 된다는 것을 의미한다.

### models에 파일 필드 추가

```python
img = models.FileField(upload_to='PATH', blank=True)
```

### 미디어 파일을 위한 url 지정하기

프로젝트의 `url.py`에서 media를 처리하는 url을 설정해야 한다.

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Your path here..
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### HTTP에서 이미지 풀러오기

값을 가져올 때 `p.img`가 이미지 오브젝트라고 하자. 그럼 그 이미지의 `url`을 넣어주어야 한다.

```html
{{ p.img.url }}
```
