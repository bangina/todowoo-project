from rest_framework import serializers
from todo.models import Todo

# todo model(api밖에 있음)


class TodoSerializer(serializers.ModelSerializer):
    #장고 자동생성되는 날짜 정보는 읽기전용으로 선언
    created = serializers.ReadOnlyField()
    datecompleted = serializers.ReadOnlyField()

    class Meta:
        model = Todo
        fields = ['id', 'title', 'memo', 'created',
                  'datecompleted', 'important']

    # Todo 모델은 아래와 같음.
    # 메타정보의 필드를 보면 기존 모델에 없는 'id' 추가해주고 'user'는 생략함
    # why? 어차피 user만이 todo 자신의 정보를 볼 수 있기 때문에

    # title = models.CharField(max_length=100)
    # memo = models.TextField(blank=True)
    # created = models.DateTimeField(auto_now_add=True)
    # datecompleted = models.DateTimeField(null=True, blank=True)
    # important = models.BooleanField(default=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
