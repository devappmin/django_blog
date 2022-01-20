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

```django
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

## DetailView

`list`에 대한 세부적인 화면을 보여줄 때는 `DetailView`를 활용하는 것이 더 좋다.

**Before**

```python
def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(request, 'blog/single_post_page.html', {'post': post})
```

**After**

```python
class PostDetail(DetailView):
    model = Post
```

### url 처리

DetailView를 사용해서 값을 처리할 때는 url을 아래와 같이 처리해주면 된다.

In `urls.py`,

```python
urlPattern = [
    # Your other path here..
    path('', views.PostDetail.as_view())
]
```

## Create View

`Post`를 하기 위해서 CreateView를 활용할 수 있음.

```python
from django.views.generic import CreateView

class PostCreate(CreateView):
    model = Post
    fields=['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']
```

`Create View`는 `<PATH>/post_form.html`을 요구한다.

### HTML 처리

```html
<form method="post" enctype="multipart/form-data"></form>
```

`enctype`는 파일도 같이 전송하겠다는 의미다.

```django
{% csrf_token %}
```

위 값을 `<form>` 태그 안에다가 넣어주어 CSRF 공격으로부터 보호를 받을 수 있다.

```django
{{form}}
```

`{{form}}`을 통해서 `views`의 `fields`에 존재하는 값을 폼 형태로 넣을 수 있다.

#### Full Code

```django
<form method="post" enctype="multipart/form-data">{% csrf_token %}
    <table>
        {{form}}
    </table>
    <button type="submit" class="btn btn-primary float-end">Submit</button>
</form>
```

## Auth

### 인증된 사용자만 들어올 수 있게 하기

```python
from django.contrib.auth.mixins import LoginRequiredMixin

class PostCreate(LoginRequiredMixin, CreateView):
    # Your Code Here..
```

`LoginRequiredMixin`을 통해서 인증된 사용자만 보이게 할 수 있다.

### 자동으로 유저 인증하기

`LoginRequiredMixin`과 `CreateView`를 통해 만들어진 클래스에서 `form_valid`를 통해서 자동으로 필드 값을 채울 수 있다. 아래의 예제는 `author`를 채우는 부분이다.

```python
def form_valid(self, form):
    current_user = self.request.user
    if current_user.is_authenticated:
        form.instance.author = current_user
        return super(PostCreate, self).form_valid(form)
    else:
        return redirect('/blog/')
```

1. `self.request.user`는 방문자를 의미
2. `is_authenticated`는 로그인한 상태인지 확인
3. `form.instance`는 새로 생성한 포스트에 `author` 필드를 현재 유저로 채움
4. 방문자가 로그인하지 않으면 `redirect`로 `blog`로 이동

## Override Context

`CBV`에서는 기본적으로 `get_context_data` 메서드를 내장하고 있다. 그렇기 떄문에 `model = Post`라고 선언하면 해당 메서드에서 `post_list = Post.objects.all()`을 명령하고 그 덕분에 `{% for p in post_list %}` 또한 가능한 것이다. 이를 오버라이딩하여 수정하려고 하면 다음과 같이 해야한다.

```python
class PostList(ListView):
    # Overriding 하는 부분
    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(
            category=None).count()
        return context
```

이를 했다면 `html`에서 다음과 같이 활용할 수 있다.

**ex.**

```django
{% for category in categories %}
```
