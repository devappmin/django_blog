# Admin

## Import to admin.

```python
admin.site.register(SOMETHING)
```

## 자동등록

```python
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
```

`{'slug': ('name',)}`을 통해서 `name`에 필드 값이 입력이 됐을 떄 자동으로 `slug`이 만들어지게 할 수 있다.

ex) `category`가 `name`과 `slug`(url용)으로 구성돼 있을 떄

```python
name = '문화 & 예술' # 이면
slug = '문화-예술' # 로 치환 됨.
```
