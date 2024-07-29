from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Tasks
from .pagination import CustomPagination
from .serializers import TaskListSerializer, TaskCreateSerializer,\
    TaskDetailSerializer, TaskUpdateSerializer, \
    TaskDeleteSerializer


class TaskListView(generics.GenericAPIView):
    """
        Представление для выдачи всех задач с пагинацией
        по 5 задач на странице
    """
    serializer_class = TaskListSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name='completed',
                description='Filter tasks by completion status (true/false)',
                required=False,
                type=bool,
            ),
        ]
    )
    def get(self, request):
        user = request.user
        completed = request.query_params.get('completed')

        if completed is not None:
            completed = completed.lower() in ['true', '1']
            tasks = Tasks.objects.filter(user=user, completed=completed)
        else:
            tasks = Tasks.objects.filter(user=user)

        serializer = self.serializer_class(
            tasks, many=True, context={"request": request}
        )

        self.paginator.page_size = 5
        # установка ограничения  количества задач на одной странице
        self.paginator.page_size_query_param = "page_size"
        self.paginator.message = "Задачи"
        page = self.paginator.paginate_queryset(serializer.data, request)

        return self.paginator.get_response(page)


class TaskCreateView(generics.CreateAPIView):
    """
        Представление для создания задачи
    """
    queryset = Tasks.objects.all()
    serializer_class = TaskCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetailView(generics.GenericAPIView):
    """
        Представление для детальной информации о задаче
    """
    serializer_class = TaskDetailSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        user = self.request.user
        try:
            task = Tasks.objects.get(user=user, pk=pk)
        except Tasks.DoesNotExist:
            return Response({"Ошибка": "Задача не найдена"}, status=404)

        serializer = self.serializer_class(task, context={"request": request})
        return Response(serializer.data)


class TaskUpdateView(generics.GenericAPIView):
    """
        Представление для обновления задачи
    """
    queryset = Tasks.objects.all()
    serializer_class = TaskUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        user = self.request.user
        task = self.get_object()
        if task.user != user:
            return Response({"Ошибка": "Нет доступа к задаче"}, status=403)

        serializer = self.get_serializer(task, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


class TaskDeleteView(generics.DestroyAPIView):
    """
        Представление для удаления задачи
    """
    queryset = Tasks.objects.all()
    serializer_class = TaskDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"Успешно": "Задача удалена"}, status=status.HTTP_204_NO_CONTENT)
