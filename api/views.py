from rest_framework import generics, permissions
from .serializers import TodoSerializer
from todo.models import Todo


class TodoCompletedList(generics.ListAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # 요청 user에 연결된 데이터 전부 보여줘, datecompleted 값이 있는!(시간순으루)
        return Todo.objects.filter(user=user, datecompleted__isnull=False).order_by(
            '-datecompleted')
