# Django Tips

## Create Django Project.

```terminal
$ django-admin startproject PROJECT_NAME .
```

## Create Superuser.

```terminal
$ python3 manage.py createsuperuser
```

## Create App.

```terminal
$ python3 manage.py startapp APP_NAME
```

## Create Model.

### Basic Model

```python
class Post(models.Model):
    # Put Your Models here..

    def __str__(self):
        return self.title
```

### Basic Model Field

```python
models.CharField() # Can add max_length
models.TextField()
models.DateTimeField() # Can add auto_now_add or auto_now
```

## Create View.

### Add view into url

In `urls.py`, add your `view` with `path`.

```python
urlpatterns = [
    path('', views.index)
]
```

### Create view

In `views.py`,

```python
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'blog/index.html', {'posts': posts, })
```

`models`에서 값을 가져와서 `views`에서 값을 호출함.

```python
# Get objects from model and show it
# all() 이외에도 filter(), order_by(), create(), delete() 등이 있음.
posts = Post.objects.all()
```

`order_by()`를 통해서 값 ordering하기

```python
# Order by value.
posts = Post.objects.all().order_by('-created_at')
```

`view` 함수에서 `render()`를 통해서 렌더링을 할 수 있음.

```python
render(request, TEMPLATE, QUERY)
```

## HTML Randering

for loop등 명령에 해당하는 부분은 `{% %}`로 감싸고 변수를 의미하는 곳은 `{{ }}`로 감싸줄 것

```html
{% for post in posts %}
<hr />
<h2>{{ post.title }}</h2>
<h4>{{ post.created_at }}</h4>
<p>{{ post.content }}</p>
{% endfor %}
```
