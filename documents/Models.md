# Models

## Set Null

### null

```py
temp = models.YOUR_MODEL(..., null=true)
```

위를 통해서 null로 지정할 수 있다.

### blank

```py
temp = models.YOUR_MODEL(..., null=true, blank=true)
```

ForeignKey를 포함하여 몇 `model`에서는 null을 해도 값을 요구한다. 이 때는 `blank` 또한 `true`로 지정해주면 된다.
