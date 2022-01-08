# CBV (8-3 P.187)

## ListView

여러 개의 값을 나열할 때는 `ListView`클래스를 활용하는 것이 더 좋다.

**Before**

```python
def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(request, 'blog/index.html', {'posts': posts, })
```

**After**

```python
from django.views.generic import ListView

class PostList(ListView):
    model = Post
```

### url 처리

ListView를 사용해서 값을 처리할 때는 url을 아래와 같이 처리해주면 된다.

In `urls.py`,

```python
urlPattern = [
    # Your other path here..
    path('', views.PostList.as_view())
]
```

### HTML 처리

`ListView`를 통해서 출력을 할 때에는 `..._list.html`을 생성해야 한다. 여기서 `...`은 모델의 값을 의미하며 `blog` 앱의 `post` 모델을 사용하려면 `post_list.html`을 생성해야 한다.

이를 처리하는 방법은 2가지가 있다.

1. `post_list.html` 만들기
2. `template_name`을 지정하기

   In `views.py`,

   ```python
   class PostList(ListView):
       model = Post
       template_name = 'blog/index.html`
   ```

In `blog/index.html`,

```html
{% for post in post_list %}
```

`HTML`에서 값을 가져올 때는 딕셔너리 변수 값을 `..._list` 값을 통해서 얻어와야 한다.

### ordering

`ListView`에서는 `ordering` 또한 제공한다. 이를 사용하는 방법은 클래스 내에 `ordering`만 정의 해주면 된다.

```python
class PostList(ListView):
    model = Post
    ordering = '-pk'
```
