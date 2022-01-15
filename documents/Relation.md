# Relation

## ManyToMany

`model`내에서 `ManyToManyField`를 지정해서 `다대다 관계`를 구현할 수 있다.

```python
class MyModel(models.Model):
    mtm = models.ManyToManyField(AnotherModel, blank=True)
```

`ManyToManyField`는 `null=True`가 기본적으로 설정이 되어있기 때문에 `null=True`를 지정하지 않아도 된다.

### HTML에서 ManyToMany가 존재하는지 확인

`exists`를 통해서 존재하는지 확인할 수 있다.

```django
{% if mymodel.AnotherModel.exist %}
<!-- DO SOMETHING.. -->
{% endif %}
```

### HTML에서 ManyToMany를 반복하기

`iterator`혹은 `all`을 통해서 값을 반복하면서 넣을 수 있다.

```django
{% for tag in mymodel.tags.iterator %}
```

```django
{% for tag in mymodel.tags.all %}
```
