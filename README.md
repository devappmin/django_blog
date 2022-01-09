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

app을 만든 뒤에는 `urls.py`가 바로 생성이 안되기 때문에 필요 시 직접 생성해야 한다.

```python
from django.urls import path
from . import views

urlpatterns = [
    # Put your path here..
]
```

많이 쓸 두 `module`을 `import`해주고 `urlpattern`을 삽입한다.

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

### 절대 url 얻기

```python
def get_absolute_url(self):
    return PATH
```

위 값을 `models`에 추가하면 해당 모델의 url을 얻을 수 있다.

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

## Create view with parameter

`path`는 아래의 형식을 가짐

```python
path(url, VIEWS_FUNCTION)
```

`url`에 `<int:pk>`가 들어갈 경우 정수 형태의 값을 pk라는 변수에 담아서 해당 함수에 넘기겠다는 의미.

```python
path('<int:pk>/', views.single_post_page)
```

형식으로 보냈을 경우 `views`에서는 인자에 `pk`를 받을 변수를 하나 더 추가하면 된다.

```python
def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(request, 'blog/single_post.html', {'post': post})
```

## Lorem Sites

[Korean Lorem Ipsum](https://hangul.thefron.me)
[Lorem Picsum](https://picsum.photos/)

## References

[CBV](documents/CBV.md)

[Static And Media](documents/Static_And_Media.md)

[Template](documents/Template.md)

[Test](documents/Test.md)
